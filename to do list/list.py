class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        return f"[{'✓' if self.completed else '✗'}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            print(f"Task updated to: {new_description}")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task deleted: {removed_task.description}")
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Task completed: {self.tasks[index].description}")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task index to update: ")) - 1
                new_description = input("Enter new task description: ")
                todo_list.update_task(index, new_description)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task index to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '5':
            todo_list.view_tasks()
            try:
                index = int(input("Enter task index to complete: ")) - 1
                todo_list.complete_task(index)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '6':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
