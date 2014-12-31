def add_something():
    file_name=input("what is the name of the file? ")
    f=open(file_name,'a')
    to_be_add=input("what do you want to add? ")
    f.write(to_be_add)
    f.close()

def new_file():
    file_name=input("what is the name of the file? ")
    f=open(file_name,'w')
    f.close()
    show(file_name)
    

def show(file_name):
    f=open(file_name)
    print(f.read())
#for line in f.readlines():
#        print(line)
#    print(f.read())    

new_file()
add_something()
