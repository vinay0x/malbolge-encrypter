keyBase = 'abcdefghijklmnopqrstuvwxyz'
keyBaseArray = list(keyBase)
codeKey = keyBase[::-1]
codeKeyArray = list(codeKey)

def doWork(choice):
    if choice =="1":
        sentence = raw_input("What do you want to encrypt? : ")
    elif choice=="2":
        sentence = raw_input("What do you want to decrpyt? : ")
    charArray = list(sentence)
    for count1,elem in enumerate(charArray):
        for count2,elem2 in enumerate(keyBase):
            if elem == elem2:
                charArray[count1]=codeKeyArray[count2]
    string1=''.join(charArray)
    return string1

def main():
    choice = 0
    while (choice!='3'):
        choice = raw_input("\n1.Encrypt \n2.Decrpyt \n3.Exit \nEnter your choice : ")
        if choice=="1":
            answer=doWork(choice)
            print 'Encrypted sentence is : ' + answer

        elif choice=="2":
            answer=doWork(choice)
            print 'Decrypted sentence is : ' + answer
        elif choice=="3":
            exit()
        else:
            print("Invalid choice, please choose again\n")
main()
