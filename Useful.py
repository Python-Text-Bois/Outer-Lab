def InputMenu(menu,demands):
    print(menu)
    return input(demands+" ")
    
def NewSave():
    temp=open("savetemp.txt")
    temp2=temp.read()
    temp.close()
    temp=open("save.txt","w")
    temp.write(temp2)
    temp.close()

def Fetch(filename):
    file=open(filename)
    a=file.read()
    file.close()
    return a