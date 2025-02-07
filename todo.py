import time
from plyer import notification
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(Fore.GREEN + f"Task '{task}' added." + Style.RESET_ALL)
        self.notify_task(task)  # Notify the user after adding the task

    def view_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "No tasks available." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Your To-Do List:" + Style.RESET_ALL)
            for idx, task in enumerate(self.tasks, 1):
                print(Fore.BLUE + f"{idx}. {task}" + Style.RESET_ALL)

    def remove_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(Fore.RED + f"Task '{removed_task}' removed." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Invalid task number." + Style.RESET_ALL)

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
        print(Fore.MAGENTA + "1. Add Task" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. View Tasks" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. Remove Task" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. Exit" + Style.RESET_ALL)
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            try:
                task_index = int(input("Enter task number to remove: "))
                app.remove_task(task_index)
            except ValueError:
                print(Fore.YELLOW + "Invalid input. Please enter a number." + Style.RESET_ALL)
        elif choice == '4':
            print(Fore.CYAN + "Exiting app. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + "Invalid choice. Try again." + Style.RESET_ALL)

        time.sleep(1)

if __name__ == "__main__":
    main()