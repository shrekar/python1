from inmemory import InMemoryImp1

while True:

    print("*"*100)
    print("1.add 2.view all 3.update 4.delete 5. search 6.exit")
    print("*"*100)
    ch = int(input("enter your choice"))

    if ch==1:
        InMemoryImp1.addcontact()
    elif ch==2:
        InMemoryImp1.viewcontact()
    elif ch==3:
        InMemoryImp1.update()
    elif ch==4:
        InMemoryImp1.deletecontact()
    elif ch==5:
        InMemoryImp1.search()
    else:
        break
