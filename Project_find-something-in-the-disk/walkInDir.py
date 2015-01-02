import fnmatch
import os
matches=[]
start=input("where would you like to start?\n").encode('utf-8')
pattern=input("what would you like to find?: eg. *.py *abc*.* \n").encode('utf-8')
print("loading...\n")
for root,dirnames,filenames in os.walk(start):
	for filename in fnmatch.filter(filenames,pattern):
		matches.append(os.path.join(root,filename))

if len(matches)==0:
	print("Sorry, nothing found...\n")
else:
	for match in matches:
		print(match.decode('utf-8')+'\n')
