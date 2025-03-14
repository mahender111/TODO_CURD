from django.test import TestCase

# Create your tests here.



    # def remove_task(self, task_number):
    #     try:
    #         if 0 <= task_number < len(self.tasks):
    #             del self.tasks[task_number]
    #         else:
    #             print("Invalid task number!")
    #     except IndexError:
    #         print("Error: Task number out of range.")

    # def complete_task(self, task_number):
    #     try:
    #         if 0 <= task_number < len(self.tasks):
    #             self.tasks[task_number]["done"] = True
    #         else:
    #             print("Invalid task number!")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #     finally:
    #         print("Operation completed.")



# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append({"desc": task, "done": False})
    
   

#     def remove_task(self, task_number):
#         if self.is_empty():
#             print(f'Stack Underflow')
#         try:
#             if 0 <= task_number < len(self.tasks):
#                 del self.tasks[task_number]
#             else:
#                 print("Invalid task number!")
#         except IndexError:
#             print("Error: Task number out of range.")

#     def complete_task(self, task_number):
#         try:
#             if 0 <= task_number < len(self.tasks):
#                 self.tasks[task_number]["done"] = True
#             else:
#                 print("Invalid task number!")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#         finally:
#             print("Operation completed.")

#     def list_tasks(self):
#         if self.tasks=="":
#             print("tasks is empty")
#         else:
#             for i, task in enumerate(self.tasks):
#                 status = "Done" if task["done"] else "Pending"
#                 print(f"{i+1}. {task['desc']} [{status}]")

#     def undo(self, x):
#         self.push(x)
#         print(x)

#     def redo(self, x):
#         self.pop(x)
#         print(x)

#     def is_empty(self):
#         return self.tasks is None

# def main():
#     todo = TodoList()
#     while True:
#         print("\nTodo List Manager")
#         print("1. Add task")
#         print("2. Remove task")
#         print("3. Complete task")
#         print("4. List tasks")
#         print("5. Exit")
#         choice = input("Enter choice: ")

#         if choice == "1":
#             task = input("Enter task description: ")
#             if isinstance(num_1, int)==True:
#                 todo.add_task(task)
#             else:
#                 print("enter a interger value")
#         elif choice == "2":
#             num = input("Enter task number to remove: ")
#             if isinstance(num_1, int)==True:
#                 todo.remove_task(int(num))
#             else:
#                 print("enter a interger value")
#         elif choice == "3":
#             num = input("Enter task number to complete: ")
#             if isinstance(num_1, int)==True:
#                 todo.complete_task(int(num))
#             else:
#                 print("enter a interger value")
            
            
#         elif choice == "4":
#             todo.list_tasks()
#         elif choice == "5":
#             print("Exiting Todo List Manager.")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# if __name__ == "__main__":
#     main()



# class TodoList:
#     def __init__(self, filename="tasks.json"):
#         self.tasks = []
#         self.filename = filename
#         self.history = []  # Stack for undo functionality
#         self.load_tasks()

#     def save_tasks(self):
#         with open(self.filename, "w") as f:
#             json.dump(self.tasks, f)

#     def load_tasks(self):
#         if os.path.exists(self.filename):
#             with open(self.filename, "r") as f:
#                 try:
#                     self.tasks = json.load(f)
#                 except json.JSONDecodeError:
#                     self.tasks = []

#     def add_task(self, task):
#         task = task.strip()
#         if not task:
#             print("Error: Task description cannot be empty.")
#             return
#         self.history.append(copy.deepcopy(self.tasks))
#         self.tasks.append({"desc": task, "done": False})
#         self.save_tasks()

#     def remove_task(self, task_number):
#         if not self.tasks:
#             print("Error: No tasks to remove.")
#             return
#         try:
#             task_number = int(task_number) - 1
#             if 0 <= task_number < len(self.tasks):
#                 self.history.append(copy.deepcopy(self.tasks))
#                 del self.tasks[task_number]
#                 self.save_tasks()
#             else:
#                 print("Error: Invalid task number.")
#         except ValueError:
#             print("Error: Please enter a valid task number.")

#     def complete_task(self, task_number):
#         if not self.tasks:
#             print("Error: No tasks to complete.")
#             return
#         try:
#             task_number = int(task_number) - 1
#             if 0 <= task_number < len(self.tasks):
#                 self.history.append(copy.deepcopy(self.tasks))
#                 self.tasks[task_number]["done"] = True
#                 self.save_tasks()
#             else:
#                 print("Error: Invalid task number.")
#         except ValueError:
#             print("Error: Please enter a valid task number.")

#     def edit_task(self, task_number, new_desc):
#         new_desc = new_desc.strip()
#         if not new_desc:
#             print("Error: Task description cannot be empty.")
#             return
#         if not self.tasks:
#             print("Error: No tasks to edit.")
#             return
#         try:
#             task_number = int(task_number) - 1
#             if 0 <= task_number < len(self.tasks):
#                 self.history.append(copy.deepcopy(self.tasks))
#                 self.tasks[task_number]["desc"] = new_desc
#                 self.save_tasks()
#             else:
#                 print("Error: Invalid task number.")
#         except ValueError:
#             print("Error: Please enter a valid task number.")

#     def undo(self):
#         if self.history:
#             self.tasks = self.history.pop()
#             self.save_tasks()
#             print("Last operation undone.")
#         else:
#             print("Error: No actions to undo.")

#     def list_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#         else:
#             for i, task in enumerate(self.tasks):
#                 status = "Done" if task["done"] else "Pending"
#                 print(f"{i+1}. {task['desc']} [{status}]")

# def main():
#     todo = TodoList()
#     while True:
#         print("\nTodo List Manager")
#         print("1. Add task")
#         print("2. Remove task")
#         print("3. Complete task")
#         print("4. Edit task")
#         print("5. Undo last action")
#         print("6. List tasks")
#         print("7. Exit")
#         choice = input("Enter choice: ")

#         if choice == "1":
#             task = input("Enter task description: ")
#             todo.add_task(task)
#         elif choice == "2":
#             num = input("Enter task number to remove: ")
#             todo.remove_task(num)
#         elif choice == "3":
#             num = input("Enter task number to complete: ")
#             todo.complete_task(num)
#         elif choice == "4":
#             num = input("Enter task number to edit: ")
#             new_desc = input("Enter new description: ")
#             todo.edit_task(num, new_desc)
#         elif choice == "5":
#             todo.undo()
#         elif choice == "6":
#             todo.list_tasks()
#         elif choice == "7":
#             print("Exiting Todo List Manager.")
#             break
#         else:
#             print("Invalid choice! Please try again.")

# if __name__ == "__main__":
#     main()


# n = 5
# alph = 65
# for i in range(0, n):
#     print(" " * (n-i), end=" ")
#     for j in range(0, i+1):
#         print(chr(alph), end=" ")
#         alph += 1
#     alph = 65
#     print()



# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:  # Swap if greater
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Example usage
# numbers = [5, 3, 8, 1, 2]
# bubble_sort(numbers)
# print(numbers)


# def count_zeros(matrix):
#     count = 0
#     for row in matrix:
#         for num in row:
#             if num == 0:
#                 count += 1
#     return count

# arr = [[0, 0, 1],  
#        [2, 1, 0]]

# print(count_zeros(arr))  # Output: 3
