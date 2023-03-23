#with List
fridge=["coke","soda","water"]

while True:
    print()
    print("Option: ")
    print("1- Add item into list ")
    print("2- Remove item from the list ")
    print("3- View current list ")
    print("4- Quit ")
    
    option=input("what do you want to do? Please select from the option ")
    
    if option=="1":
        item=input("enter new item : ")
        fridge.append(item)
        
        print(f" {item} is added into the list")
        print(f"updated list: {fridge}")
        
    elif option=="2":
        item=input("remove item from list : ")
        fridge.remove(item)
        
        print(f" {item} is removed from the list")
        print(f" updated list: {fridge} ")
        
    elif option=="3":
        item=input("Current shopping List: ")
        for item in fridge:
            print(f"{item}")
            
    elif option=="4":
        print("Quit")
        break
    
    else:
        print("invalid option")
        
print("final list : ")
for item in fridge:
    print(f"{fridge}")
        
        