from task import Task
from utils import add_task, view_tasks, filter_tasks_by_priority, filter_tasks_by_category, sort_tasks_by_due_datetime, mark_task_complete, remove_task, save_tasks

def main():
    while True:
        print("\n========= Easy Task Manager Application ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Filter Tasks by Priority")
        print("4. Filter Tasks by Category")
        print("5. Sort Tasks by Due Date & Time")
        print("6. Mark Task as Complete")
        print("7. Remove Task")
        print("8. Save Tasks")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            filter_tasks_by_priority()
        elif choice == "4":
            filter_tasks_by_category()
        elif choice == "5":
            sort_tasks_by_due_datetime()
        elif choice == "6":
            mark_task_complete()
        elif choice == "7":
            remove_task()
        elif choice == "8":
            save_tasks()
            print("Tasks saved successfully.")
        elif choice == "9":
            save_tasks()
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
