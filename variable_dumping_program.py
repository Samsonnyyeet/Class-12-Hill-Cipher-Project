import pickle
Dfile=open("info.dat",'wb')
pickle.dump(('','',[[3,7],[5,12]],[[0],[0]],[[0],[0]],[[12,19],[21,3]]),Dfile)
Dfile.close()
