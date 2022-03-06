import pickle
import numpy as np

def inputObtainer(): #obtains input and converts it into a useable format where number of characters in string is multiple of 2

    inputStr=input("Enter your input with lowercase characters only ->")
    
    while inputStr.islower()==False:
        inputStr=input("Please enter valid input")

    if len(inputStr)%2==1:
        inputStr=inputStr+'a'

    return inputStr


def matrixMaker(string): #converts the input of a string into its matrix format

    randomMatrix=[[2],[2]]

    for i in range (2):

        for j in range(1):

            randomMatrix[i][j]=ord(string[i])%96

    return randomMatrix


def encrypt(matrix): #multiplies the message matrix with the key matrix to obtain the encrypted matrix

    placeholderMatrix=[[0],[0]]
    
    for i in range(2):

        for j in range(1):

            for x in range(2):
                placeholderMatrix[i][j] += (keyMatrix[i][x] * matrix[x][j])

            placeholderMatrix[i][j] = placeholderMatrix[i][j] % 26

    return placeholderMatrix

    
def matrixToText(matrix): #converts matrix to text

    text=''

    for i in range(2):

        for j in range(1):

            text+=chr(matrix[i][j]+96)

    return text
            

def inputProcessorForEncryption(inputToEncrypt): #splits the text into blocks of 2 and then encrypts each block

    placeholder1=''

    k=int(len(inputToEncrypt)/2)

    for i in range(1,k+1):

        placeholder2=''
        
        for j in range((i-1)*2,i*2):
            placeholder2+=inputToEncrypt[j]

        messageMatrix=matrixMaker(placeholder2)

        placeholder1+=matrixToText(encrypt(messageMatrix))

    return placeholder1


def decrypt(matrix):

    placeholder=[[0],[0]]

    for i in range(2):

        for j in range(1):

            for x in range(2):

                placeholder[i][j]+=modularInvertedMatrix[i][x]*matrix[x][j]  

            placeholder[i][j]=placeholder[i][j]%26

    return placeholder


def inputProcessorForDecryption(inputToDecrypt):

    placeholder1=''

    k=int(len(inputToDecrypt)/2)

    for i in range(1,k+1):

        placeholder2=''
        
        for j in range((i-1)*2,i*2):
            placeholder2+=inputToDecrypt[j]

        encryptedMatrix=matrixMaker(placeholder2)

        placeholder1+=matrixToText(decrypt(encryptedMatrix))

    return placeholder1



'''    
def adjointer(matrix): #converts matrix to adjoint through normal algebraic method

    adjoint=[[0,0],[0,0]] 

    inverse=np.linalg.inv(matrix)

    for i in range(2):

        for j in range(1):

            adjoint[i][j]=inverse[i][j]*(np.linalg.det(matrix))

    return adjoint

    
def modularInverseMatrix(matrix):#used to calculate the modular inverse, useable for decryption

    adjointMatrix=[[0,0],[0,0]]
    adjointMatrix=adjointer(matrix)
    determinant=np.linalg.det(matrix)
    invertedMatrix=[[0,0],[0,0]]

    for i in range(3):

        for j in range(3):

            invertedMatrix[i][j]=cofactorMatrix[i][j]*pow(cofactorMatrix[i][j],-1,determinant)
        
    return invertedMatrix


def obtainingKey():

    key=input('Please enter a 9 letter lowercase word without any other characters.')
    key=key.strip()

    while (key.isalpha() and key.islower() and len(key)==9)==False:
        key=input('Please enter a valid key')

    counter=0

    while np.linalg.det(keyMatrix)!=0:
        
        for i in range(3):

            for j in range(3):

                keyMatrix[i][j]=ord(key[counter])%96
                counter+=1

        if np.linalg.det(keyMatrix)==0:

            key=input('This key forms a singular matrix, please try entering something else')
            continue

        else:

            break
'''

with open("info.dat",'rb') as datafile:

    variableTuple=pickle.load(datafile)

    encryptedInformation=variableTuple[0]

    decryptedIformation=variableTuple[1]

    keyMatrix=variableTuple[2]

    messageMatrix=variableTuple[3]

    encryptedMatrix=variableTuple[4]

    modularInvertedMatrix=variableTuple[5]


while True:
    
    var1=input('Would you like to encrypt or decrypt? (Type exit to quit)')

    if var1.lower()=='encrypt':

        inputToEncrypt=inputObtainer()

        encryptedInformation=inputProcessorForEncryption(inputToEncrypt)

        print(encryptedInformation)

        continue

    elif var1.lower()=='decrypt':

        inputToDecrypt=input('Enter encrypted information ->')

        decryptedInformation=inputProcessorForDecryption(inputToDecrypt)

        print(decryptedInformation)

        continue

    elif var1.lower()=='exit':

        break

    else:

        var1=input('Please try to enter again, encrypt or decrypt?')
        continue
    
