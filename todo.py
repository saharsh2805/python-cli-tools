#codename = input("Enter codename: ")
#mission_id = int(input("Enter mission id: "))
#print(f"Agent {codename} (ID: {mission_id}) is checked in.")
import json

def load_tasks():       #Its job is to load saved tasks from a file
    try:
        with open('tasks.json', 'r') as file:     #file:variable representing tasks.json file
            return json.load(file)
    except FileNotFoundError:
        return []     #If file not found, return empty list

def save_tasks(tasks) :
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

print("----To-Do List Menu----")
print("1. Add a task (type add, 1)")
print("2. View tasks (type view, 2)")
print("3. Checkmark a task (type check, 3)")
print("4. Remove a task (type remove, 4)")
print("5. Quit (type exit, 0)")

to_do_list = load_tasks()
                              #Load existing tasks from file

def add_task(task):
    to_do_list.append({"Task": task, "Status": "Incomplete"})

def view_tasks():
    if not to_do_list:
        print("No tasks in To-Do List.")
    else:
        for i, task in enumerate(to_do_list):
            print(f"{i+1}. {task['Task']} - {task['Status']}")

def check_task(task_number):
    if 0 < task_number <= len(to_do_list):
        to_do_list[task_number - 1]['Status'] = "Complete"
        print(f"Task '{to_do_list[task_number - 1]['Task']}' marked as complete.")
        view_tasks()
    else:
        print("Invalid task number.")

def remove_task(task_number):
    if 0 < task_number <= len(to_do_list):
        print(f"Task '{to_do_list[task_number - 1]['Task']}' removed.")
        del to_do_list[task_number - 1]
        view_tasks()
    else:
        print("Invalid task number.")

while True :
    command = input("Enter command: ")

    if command.lower() == "exit" or command == "0":
        save_tasks(to_do_list)   #Save tasks to file before exiting
        break

    elif command.lower() == "add" or command =="1":
        #set of intructions to add a task
        task = input("Enter task: ")
        add_task(task)
    elif command.lower() == "view" or command =="2":
        #set of instructions to view to-do list
        view_tasks()
    elif command.lower() == "check" or command =="3":
        #set of instructions to checkmark a task
        task_number = int(input("Enter task number to check-mark:"))
        check_task(task_number)
    elif command.lower() == "remove" or command =="4":
        #set of instructions to remove a task
        task_number = int(input("Enter task number to remove:"))
        remove_task(task_number)

    else:
        print("Invalid command. Please try again.")
    
print("End of To-Do applications.")

    #The loop will break automatically whenever the user types "exit" or "0"
