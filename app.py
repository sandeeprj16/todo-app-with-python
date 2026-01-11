# app.py
# Simple CLI To-Do Application

def show_menu():
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter task name: ")
    tasks.append(task)
    print("✅ Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("⚠️ No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            removed_task = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{removed_task}' deleted.")
        except (ValueError, IndexError):
            print("❌ Invalid task number.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
