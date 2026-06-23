def add():
    grade = input("Enter Your Grade")
    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(grade + "\n")
        print("Note Added Correctly")
        

def list_items():
    with open("notlar.txt","r",encoding="utf-8") as file:
        listt  = file.read()    
        print(listt)



def exit_program():
    print("EXIT")


actions = {
    "1": add,
    "2": list_items,
    "3": exit_program
}

choice = input("Make a Choice: ")

if choice in actions:
    actions[choice]()
else:
    print("Invalid Choice")