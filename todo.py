import time
from plyer import notification

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")
        self.notify_task(task)  # Notify the user after adding the task

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

    def notify_task(self, task):
        """Send desktop notification"""
        notification.notify(
            title='To-Do List Reminder',
            message=f'Task "{task}" added to your list!',
            timeout=10  # The notification will show for 10 seconds
        )

def main():
    app = TodoApp()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to remove: "))
            app.remove_task(task_index)
        elif choice == '4':
            print("Exiting app.")
            break
        else:
            print("Invalid choice. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
