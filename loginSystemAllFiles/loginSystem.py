def newUser():
    writingToFile = open("users.txt","a")
    username = input("ENTER A USERNAME: ")
    password = input("ENTER A PASSWORD: ")                                          
    reEnterPassword = input("RE-ENTER A PASSOWORD: ")
    while password != reEnterPassword:
        print("DIDNT RE ENTER PASSWORD CORRECTLY")
        password = input("ENTER A PASSWORD: ")                                          
        reEnterPassword = input("ENTER A PASSOWORD: ")    
    writingToFile.write(username+","+password+"\n")
    writingToFile.close()

def login():
    takingFromFile = open("users.txt","r")
    username = input("ENTER YOUR USERNAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    for line in takingFromFile:
        line = line.strip()
        uName,pWord = line.split(",")
        if username == uName and password == pWord:
            print("hello,",uName)
            #add where ever you want to go#()
    print("INVALID DETAILS")
    return takingFromFile()
    takingFromFile.close()


