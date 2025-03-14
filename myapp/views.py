from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import copy
import unittest

# Create your views here.

def index(request):
    return HttpResponse("welcome first page")

class Curd:
    def __init__(self, filename="tasks_project.json"):
        self.filename = filename 
        self.tasks = []
        self.history = []
        self.load_curd()

    def save_curd(self):
        with open(self.filename, "w") as f :
            print('f---------',f)
            json.dump(self.tasks, f) 
    
    def load_curd(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    self.tasks = json.load(f)
                    print('Loaded tasks:--------', self.tasks)
                except json.JSONDecodeError:
                    print("JSON file is empty or corrupted. Initializing an empty task list.")
                    self.tasks = []

    def add_task(self, task):
        task = task.strip()
        if not task:
            print("Task description cannot be empty")
            return

        task_id = len(self.tasks)
        self.history.append(copy.deepcopy(self.tasks))
        self.tasks.append({"id": task_id,"desc": task, "done": False})
        self.save_curd()

    def list_curd1(self):
        if not self.tasks:
            print("Not tasks found")
        else:
            for index, task in enumerate(self.tasks):
                print('a---------',index,task)
                status = "Done" if task["done"] else "Pending"
                print(f"{index+1}. {task['desc']} [{status}]")

    def list_curd2(self):
        self.load_curd()
        try: 
            if 0 < len(self.tasks):
                print("yes, data is available ")
                for index, task in enumerate(self.tasks):
                    print('a---------',index,task)
                    status = "Done" if task["done"] else "Pending"
                    print(f"{index+1}. {task['desc']} [{status}]")
            else:
                print("no, data is not preesent")
        except ValueError as e:
            print("try again")

    def remove_task_1(self, id_task_number):
        a = self.load_curd()
        id_task_number = int(id_task_number)
        for index, task in enumerate(self.tasks):
            if id_task_number == index: 
                self.history.append(copy.deepcopy(self.tasks))              
                del self.tasks[id_task_number]
                self.save_curd()
                print(f"Task '{id_task_number}' removed successfully!")
                return
            print(f"id number Task '{id_task_number}' not found!")

    def remove_task_2(self, id_task_number):
        self.load_curd()
        if not self.tasks:
            print("No tasks to remove.")
            return
        try:
            index_task_number = int(id_task_number) - 1
            if 0 <= index_task_number < len(self.tasks):
                self.history.append(copy.deepcopy(self.tasks))
                del self.tasks[index_task_number]
                self.save_curd()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    
    def complete_task(self, id_task_no):
        self.load_curd()  # Load existing tasks
        try:
            id_task_no = int(id_task_no) 
        except ValueError:
            print("Enter a valid Task ID Number")
            return  

        if not self.tasks:
            print("Data does not exist")
            return

        for item in self.tasks:
            if item['id'] == id_task_no:
                self.history.append(copy.deepcopy(self.tasks))
                item['done'] = True
                self.save_curd()  # Save changes after updating
                print(f"Task ID {id_task_no} marked as completed ✅")
                return  # Exit after updating

        print(f"Task ID {id_task_no} not found ❌")  # If ID does not exist


    def edit_task(self, id_task_no, new_desc):
        self.load_curd()
        new_desc = new_desc.strip()

        if not new_desc:
            print("Error: Task description cannot be empty.")
            return

        try:
            id_task_no = int(id_task_no) 
        except ValueError:
            print("Enter a valid Task ID Number")
            return  

        if not self.tasks:
            print("Data does not exist")
            return

        for item in self.tasks:
            if item['id'] == id_task_no:
                self.history.append(copy.deepcopy(self.tasks))
                item['desc'] = new_desc
                self.save_curd()
                print(f"Task ID {id_task_no} marked as completed ✅")
                return  
        print(f"Task ID {id_task_no} not found ❌") 

    
    def undo(self):
        self.load_curd()
        if self.history:
            self.tasks = self.history.pop()
            self.save_curd()
            print("undo opertations")
        else:
            print("No actions to undo")


def main():
    todo = Curd()
    while True:
        print("\nCurd List Manager")
        print("1. Add task")
        print("2. List tasks 1")
        print("3. List tasks 2")
        print("4. Remove task 1")
        print("5. Remove task 2")
        
        print("6. Complete task")
        print("7. Edit task")
        print("8. Undo last action")
        print("9. Exit")
        
        choice = input("Enter choice:-------> ")
        if choice == "1": 
            task = input("Enter task description: ")
            todo.add_task(task)

        elif choice == "2":
            todo.list_curd1()

        elif choice == "3":
            todo.list_curd2()

        elif choice == "4":
            id_task_number = input("Enter task number to remove: ")
            todo.remove_task_1(id_task_number)
        
        elif choice == "5":
            id_task_number = input("Enter task number to remove: ")
            todo.remove_task_2(id_task_number)

        elif choice == "6":
            num = input("Enter task number to complete: ")
            todo.complete_task(num)
            
        elif choice == "7":
            id_task_no = input("Enter task number to edit: ")
            new_desc = input("Enter new description: ")
            todo.edit_task(id_task_no, new_desc)

        elif choice == "8":
            todo.undo()

        elif choice == "9":
            print("Exiting curd List Manager")
            break
        else:
            print("Invalid choice! Please try again")

if __name__ == "__main__":
    main()


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.history = []
        self.filename = filename
        self.load_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                try:
                    self.tasks = json.load(f)
                except json.JSONDecodeError:
                    self.tasks = []

    def add_task(self, task):
        task = task.strip()
        print('task--------',task)
        if not task:
            print("Task description cannot be empty")
            return
        self.history.append(copy.deepcopy(self.tasks))
        self.tasks.append({"desc": task, "done": False})
        self.save_tasks()

    def remove_task(self, task_number):
        if not self.tasks:
            print("No tasks to remove.")
            return
        try:
            task_number = int(task_number) - 1
            print('task_number--------------',task_number)
            if 0 <= task_number < len(self.tasks):
                self.history.append(copy.deepcopy(self.tasks))
                del self.tasks[task_number]
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def complete_task(self, task_number):
        if not self.tasks:
            print("No tasks to complete.")
            return
        try:
            task_number = int(task_number) - 1
            if 0 <= task_number < len(self.tasks):
                self.history.append(copy.deepcopy(self.tasks))
                self.tasks[task_number]["done"] = True
                self.save_tasks()
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Please enter a valid task number.")

    def edit_task(self, task_number, new_desc):
        new_desc = new_desc.strip()
        if not new_desc:
            print("Error: Task description cannot be empty.")
            return
        if not self.tasks:
            print("Error: No tasks to edit.")
            return
        try:
            task_number = int(task_number) - 1
            if 0 <= task_number < len(self.tasks):
                self.history.append(copy.deepcopy(self.tasks))
                self.tasks[task_number]["desc"] = new_desc
                self.save_tasks()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def undo(self):
        if self.history:
            self.tasks = self.history.pop()
            self.save_tasks()
            print("undo opertations")
        else:
            print("No actions to undo")

    def list_tasks(self):
        if not self.tasks:
            print("Not tasks found")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Pending"
                print(f"{i+1}. {task['desc']} [{status}]")

def main():
    todo = TodoList()
    while True:
        print("\nTodo List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Complete task")
        print("4. Edit task")
        print("5. Undo last action")
        print("6. List tasks")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1": 
            task = input("Enter task description: ")
            todo.add_task(task)
        elif choice == "2":
            num = input("Enter task number to remove: ")
            todo.remove_task(num)
        elif choice == "3":
            num = input("Enter task number to complete: ")
            todo.complete_task(num)
        elif choice == "4":
            num = input("Enter task number to edit:")
            new_desc = input("Enter new description:")
            todo.edit_task(num, new_desc)
        elif choice == "5":
            todo.undo()
        elif choice == "6":
            todo.list_tasks()
        elif choice == "7":
            print("Exiting Todo List Manager")
            break
        else:
            print("Invalid choice! Please try again")

if __name__ == "__main__":
    main()

