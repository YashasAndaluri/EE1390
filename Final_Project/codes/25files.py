import numpy as np
import soundfile as sf
new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file
y1 = np.empty([25000,])
commands=["back","forward","left","right","stop"]
for k in range(0,5): #range generates all integers from 0 up to,but not including 5 
	for j in range(1,81):
		b= commands[k]+str(j)+".wav"
		data, samplerate = sf.read(b) #reading audio file using soundfile library
		print (len(data))
		print (samplerate)
		x= len(data)
		p= (25000-x)//25
		for y in range(p,(25*p)+1,p):  
			for i in range(0,y):      #adding empty elements in the array in the start
				new_data[i] =y1[i]
			for i in range(y,x+y):
				new_data[i] =data[i-y]
			for i in range(x+y,25000):    #adding empty elements in the array in the end 
				new_data[i] = y1[i]	
			a = commands[k]+"__"+str(j)+"_"+str(y//p)+".wav"    #total length becomes 25000
			sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
			print (len(new_data))
