#with Dictionary

result={
    "banana":"3",
    "apple":"2"
}

while True:
    print("Option: ")
    print("1- Add item into the list")
    print("2- Remove item from the list")
    print("3- View current List")
    print("4- Quit")
    
    option=input("what do you wan to do? Please select from the options: ")
    
    if option=="1":
        item=input("enter new item : ")
        quantity=input("enter quantity for item : ")
        
        if item in result:
            updateNeeds=result.values()
            result[item]=quantity
            result.update()
        else:
            result[item]=quantity
            
        print(f"{quantity}{item} is added into list. ")
        result.items()
        print(f"updated list: {result}")
        
    elif option=="2":
        item=input("remove the item from the list: ")
        
        if item in result:
            del result[item]
            print(f"{item} removed from the list")
        else:
            print(f"{item} is not in the list")
        result.items()
        print(f"updated {result}")
        
    elif option=="3":
        print("shopping list: ")
        for item, quantity in result.items():
            print(f"{quantity} {item} ")
            
    elif option=="4":
        print("Quit")
        break
    else:
        print("Invalid option")

print("final list : ")

for item, quantity in result.items():
    print(f"{quantity} {item} ")
    



    
    
    
    

    
    
    