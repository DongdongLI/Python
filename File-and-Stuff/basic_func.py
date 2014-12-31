def add_something():
    to_be_add=input("what do you want to add? ")
    f=open('test.txt','a')
    f.write(to_be_add)
    f.close()

def show():
    f=open('test.txt')
    for line in f.readlines():
        print(line)
    


#add_something()
show()
