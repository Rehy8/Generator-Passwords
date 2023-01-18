import random
import itertools

f = open('sym.txt').readline() # txt file where take place all symbols

LenPassword = 9 # Lenght of password
k = list()

for i in range(LenPassword):
	k += f[random.randint(0,67)] # Generator of password

passWord = ''.join(k)

print(passWord)# out this password

'''
for lenPassword in range(1,100):
	passWd = itertools.product (f, repeat = lenPassword)
	for i in passWd:
		str = ''.join(i)
		if str == passWord:
			print('Done',str)
			break
			break
''' # this part of code can brutforce password