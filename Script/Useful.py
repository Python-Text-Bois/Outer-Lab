#Easy way to produce an UI for input
def InputMenu(menu,demands):
    print(menu)
    return input(demands+" ")

#overwrites save file with template
def NewSave():
    temp=open("savetemp.txt")
    temp2=temp.read()
    temp.close()
    temp=open("save.txt","w")
    temp.write(temp2)
    temp.close()

#returns contents of specified file
def Fetch(filename):
    file=open(filename)
    a=file.read()
    file.close()
    return a