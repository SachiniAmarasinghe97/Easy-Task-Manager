from tabulate import tabulate
import csv
from task import Task


tasks = []
task_title_index = {}


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


def save_tasks():
    with open("tasks.csv", "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(["Title", "Description", "Due Date", "Due Time", "Priority", "Category", "Completed"])

        for curr_task in tasks:
            if curr_task.task_title in task_title_index:
                writer.writerow([
                    curr_task.task_title,
                    curr_task.task_description,
                    curr_task.task_due_date.strftime("%Y-%m-%d"),
                    curr_task.task_due_time.strftime("%H:%M"),
                    curr_task.task_priority,
                    curr_task.task_category,
                    str(curr_task.task_completed)
                ])
            else:
                writer.writerow([
                    curr_task.task_title,
                    curr_task.task_description,
                    curr_task.task_due_date.strftime("%Y-%m-%d"),
                    curr_task.task_due_time.strftime("%H:%M"),
                    curr_task.task_priority,
                    curr_task.task_category,
                    str(curr_task.task_completed)
                ])


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
