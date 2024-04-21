from datetime import datetime


class Task:
    def __init__(self, task_title, task_description, task_due_date, task_due_time, task_due_time_format, task_priority,
                 task_category, task_completed):
        self.task_title = task_title
        self.task_description = task_description
        self.task_due_date = datetime.strptime(task_due_date, "%Y-%m-%d").date()
        self.task_due_time = datetime.strptime(task_due_time, task_due_time_format).time()
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
