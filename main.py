from utils import add_task, view_tasks, filter_tasks_by_priority, filter_tasks_by_category, sort_tasks_by_due_datetime, \
    mark_task_complete, remove_task, save_tasks, quit_task_manager


def print_menu():
    """Prints the menu options."""
    menu_options = [
        "Add Task",
        "View Tasks",
        "Filter Tasks by Priority",
        "Filter Tasks by Category",
        "Sort Tasks by Due Date & Time",
        "Mark Task as Complete",
        "Remove Task",
        "Save Tasks",
        "Quit"
    ]
    print("\n========= Easy Task Manager Application ==========")
    for idx, option in enumerate(menu_options, start=1):
        print(f"{idx}. {option}")


def main():
    menu_functions = {
        "1": add_task,
        "2": view_tasks,
        "3": filter_tasks_by_priority,
        "4": filter_tasks_by_category,
        "5": sort_tasks_by_due_datetime,
        "6": mark_task_complete,
        "7": remove_task,
        "8": save_tasks,
        "9": quit_task_manager,
    }

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice in menu_functions:
            menu_functions[choice]()
            if choice == "9":
                print("Exiting Task Manager. Goodbye!")
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
