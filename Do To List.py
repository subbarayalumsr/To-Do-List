todo = []

while (cmd := input("\n(add/view/done/exit): ")) != "exit":
    if cmd == "add":
        todo += [input("Enter task: ")]
    elif cmd == "view":
        if todo:
            for i, task in enumerate(todo, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")
    elif cmd == "done":
        if todo:
            num = input("Enter task number to mark done: ")
            if num.isdigit():
                d = int(num) - 1
                if 0 <= d < len(todo):
                    print(f"Removed: {todo.pop(d)}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")
        else:
            print("No tasks to remove.")
    else:
        print("Unknown command.")
