from datetime import datetime
from tabulate import tabulate
import csv


class Task:
    def __init__(self, task_title, task_description, task_due_date, task_due_time, task_due_time_format, task_priority,
                 task_category, task_completed):
        self.task_title = task_title
        self.task_description = task_description
        self.task_due_date = datetime.strptime(task_due_date,
                                               "%Y-%m-%d").date()  # Convert due_date string to datetime.date
        self.task_due_time = datetime.strptime(task_due_time,
                                               task_due_time_format).time()  # Convert due_time string to datetime.time
        self.task_priority = task_priority
        self.task_category = task_category
        self.task_completed = task_completed

    def mark_complete(self):
        self.task_completed = True

    def __str__(self):
        return f"{self.task_title} ({self.task_due_date.strftime('%Y-%m-%d')} {self.task_due_time.strftime('%H:%M')}) - Priority: {self.task_priority}, Category: {self.task_category}, Completed: {self.task_completed}"

    def to_dict(self):
        return {
            "title": self.task_title,
            "description": self.task_description,
            "due_date": self.task_due_date.strftime("%Y-%m-%d"),
            "due_time": self.task_due_time.strftime("%H:%M"),
            "priority": self.task_priority,
            "category": self.task_category,
            "completed": self.task_completed,
        }


tasks = []
task_title_index = {}  # Dictionary to map task title to index in the tasks list

# Load tasks from the CSV file
try:
    with open("tasks.csv", "r") as file:
        reader = csv.reader(file)
        # Skip the header row
        header = next(reader)

        for idx, row in enumerate(reader):
            # Pad the row with default values if it doesn't have enough columns
            row += [""] * (8 - len(row))
            title, description, due_date, due_time, due_time_format, priority, category, completed = row

            # Skip rows where due_date or due_time is empty or contains the header value
            if due_date in ("Due Date", "") or due_time in ("Due Time", ""):
                continue

            # Create the Task object only if due_date and due_time are valid
            try:
                task = Task(title, description, due_date, due_time, due_time_format, priority, category,
                            completed.lower() == "true")
                tasks.append(task)
                task_title_index[title] = idx  # Store the index of the task in the dictionary
            except ValueError:
                print(f"Invalid date or time format for task: '{title}'")
except FileNotFoundError:
    pass


def add_task():
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")
    due_time_str = input("Enter due time (HH:MMAM/PM): ")
    task_priority = input("Enter priority (low, medium, high): ")
    task_category = input("Enter category: ")

    due_time_str = due_time_str.upper()
    new_task = Task(task_title, task_description, due_date_str, due_time_str, "%I:%M%p", task_priority, task_category,
                    task_completed="False")
    tasks.append(new_task)
    print("Task added successfully.")


def view_tasks(filtered_tasks=None):
    if filtered_tasks is None:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    task_data = []
    headers = ["Title", "Description", "Due Date", "Due Time", "Priority", "Category", "Completed"]

    for curr_task in filtered_tasks:
        task_data.append([
            curr_task.task_title,
            curr_task.task_description,
            curr_task.task_due_date.strftime('%Y-%m-%d'),
            curr_task.task_due_time.strftime('%H:%M'),
            curr_task.task_priority,
            curr_task.task_category,
            str(curr_task.task_completed)
        ])

    print(tabulate(task_data, headers=headers, tablefmt="grid"))


def filter_tasks_by_priority():
    task_priority = input("Enter priority to filter (low, medium, high): ")
    filtered_tasks = [t for t in tasks if t.task_priority == task_priority]
    view_tasks(filtered_tasks)


def filter_tasks_by_category():
    task_category = input("Enter category to filter: ")
    filtered_tasks = [t for t in tasks if t.task_category == task_category]
    view_tasks(filtered_tasks)


def sort_tasks_by_due_datetime():
    sorted_tasks = sorted(tasks, key=lambda t: (t.task_due_date, t.task_due_time))
    view_tasks(sorted_tasks)


def mark_task_complete():
    task_title = input("Enter task title to mark as complete: ")
    for t in tasks:
        if t.task_title == task_title:
            t.mark_complete()
            print(f"Task '{task_title}' marked as complete.")
            return
    print(f"No task found with title '{task_title}'.")


def remove_task():
    task_title = input("Enter task title to remove: ")
    for t in tasks:
        if t.task_title == task_title:
            tasks.remove(t)
            print(f"Task '{task_title}' removed successfully.")
            return
    print(f"No task found with title '{task_title}'.")


def save_tasks():
    with open("tasks.csv", "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(["Title", "Description", "Due Date", "Due Time", "Priority", "Category", "Completed"])

        for curr_task in tasks:
            if curr_task.task_title in task_title_index:
                # Update the existing row
                writer.writerow([
                    curr_task.task_title,
                    curr_task.task_description,
                    curr_task.task_due_date.strftime("%Y-%m-%d"),
                    curr_task.task_due_time.strftime("%H:%M"),
                    curr_task.task_priority,
                    curr_task.task_category,
                    str(curr_task.task_completed)  # Convert boolean to string
                ])
            else:
                # Append a new row
                writer.writerow([
                    curr_task.task_title,
                    curr_task.task_description,
                    curr_task.task_due_date.strftime("%Y-%m-%d"),
                    curr_task.task_due_time.strftime("%H:%M"),
                    curr_task.task_priority,
                    curr_task.task_category,
                    str(curr_task.task_completed)  # Convert boolean to string
                ])


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
