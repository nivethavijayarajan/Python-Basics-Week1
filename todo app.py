todo_list = ["Join daily stand-up meeting with the product team.",
             "Review and reply to urgent client emails.",
             "Take a 30-minute lunch break and step away from the desk."]
while True:
    choice = int(input("=== TODO APP ===\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit\nEnter your choice:"))
    print()
    if choice not in [1,2,3,4]:
        print("Invalid choice\nTry Again")
        print()
    else:
        match choice:
            case 1:
                if not todo_list:
                    print("TODO List is Empty")
                    print()
                else:
                    print("TODO List")
                    print()
                    for i,todo in enumerate(todo_list,start = 1):
                        print(f"{i}.{todo}")
                    print()
            case 2:
                get_todo = input("Enter Task for ADD in TODO List:")
                print()
                todo_list.append(get_todo)
                print(f"\"{get_todo}\" is successfully Added to TODO list")
                print()
            case 3:
                print("TODO list")
                print()
                for i,todo in enumerate(todo_list,start = 1):
                        print(f"{i}.{todo}")
                num_todo = int(input("Enter TODO List number to Delete:"))
                print()
                shower = todo_list[num_todo - 1]
                if num_todo < len(todo_list) + 1 and num_todo > 0:
                    todo_list.pop(num_todo - 1)
                    print(f"\"{shower}\" is successfully Deleted in TODO list")
                    print()
            case 4:
                print()
                print("Good Bye")
                break




