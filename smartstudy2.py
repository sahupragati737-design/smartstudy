
# MINI PROJECT: SMARTSTUDY
# Student Study Planner and Progress Tracker

class StudyPlanner:

    def __init__(self):
        self.__tasks = []
        self.__next_id = 1

    # Add a new study task
    def add_task(self):
        print("\n--- ADD NEW STUDY TASK ---")

        subject = input("Enter subject name: ").strip()
        topic = input("Enter topic name: ").strip()

        if subject == "" or topic == "":
            print("Subject and topic cannot be empty!")
            return

        print("\nSelect Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        choice = input("Enter choice: ")

        priorities = {
            "1": "High",
            "2": "Medium",
            "3": "Low"
        }

        if choice not in priorities:
            print("Invalid priority!")
            return

        task = {
            "id": self.__next_id,
            "subject": subject.title(),
            "topic": topic,
            "priority": priorities[choice],
            "completed": False
        }

        self.__tasks.append(task)
        self.__next_id += 1

        print("\nTask added successfully!")

    # Display all tasks
    def view_tasks(self):
        print("\n--- YOUR STUDY TASKS ---")

        if len(self.__tasks) == 0:
            print("No tasks available.")
            return

        for task in self.__tasks:
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print("\nTask ID:", task["id"])
            print("Subject:", task["subject"])
            print("Topic:", task["topic"])
            print("Priority:", task["priority"])
            print("Status:", status)
            print("-------------------------")

    # Mark a task as completed
    def complete_task(self):
        self.view_tasks()

        if len(self.__tasks) == 0:
            return

        try:
            task_id = int(input("\nEnter Task ID to complete: "))
        except ValueError:
            print("Please enter a valid number!")
            return

        for task in self.__tasks:
            if task["id"] == task_id:

                if task["completed"]:
                    print("This task is already completed!")
                else:
                    task["completed"] = True
                    print("Congratulations! Task completed.")

                return

        print("Task ID not found!")

    # Delete a task
    def delete_task(self):
        self.view_tasks()

        if len(self.__tasks) == 0:
            return

        try:
            task_id = int(input("\nEnter Task ID to delete: "))
        except ValueError:
            print("Please enter a valid number!")
            return

        for task in self.__tasks:
            if task["id"] == task_id:
                self.__tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Task ID not found!")

    # Search tasks by subject
    def search_subject(self):
        subject = input("\nEnter subject to search: ").strip().lower()

        found = False

        print("\n--- SEARCH RESULTS ---")

        for task in self.__tasks:
            if task["subject"].lower() == subject:
                print("ID:", task["id"])
                print("Topic:", task["topic"])
                print("Priority:", task["priority"])
                print("Status:",
                      "Completed" if task["completed"] else "Pending")
                print("----------------------")
                found = True

        if not found:
            print("No tasks found for this subject.")

    # Display progress report
    def show_progress(self):
        total = len(self.__tasks)

        completed = 0

        for task in self.__tasks:
            if task["completed"]:
                completed += 1

        pending = total - completed

        print("\n========== STUDY PROGRESS ==========")
        print("Total Tasks:", total)
        print("Completed Tasks:", completed)
        print("Pending Tasks:", pending)

        if total > 0:
            percentage = (completed / total) * 100
            print("Completion Percentage:",
                  round(percentage, 2), "%")
        else:
            percentage = 0
            print("Completion Percentage: 0%")

        print("\n--- SUBJECT-WISE SUMMARY ---")

        subjects = set()

        for task in self.__tasks:
            subjects.add(task["subject"])

        if len(subjects) == 0:
            print("No subjects added yet.")

        for subject in sorted(subjects):
            subject_total = 0
            subject_completed = 0

            for task in self.__tasks:
                if task["subject"] == subject:
                    subject_total += 1

                    if task["completed"]:
                        subject_completed += 1

            print(subject + ":",
                  subject_completed, "/", subject_total,
                  "completed")

        print("====================================")

        if percentage == 100 and total > 0:
            print("Excellent! All your tasks are completed!")
        elif percentage >= 50:
            print("Great progress! Keep going!")
        else:
            print("Stay focused. You can do it!")


# Main program

def main():

    planner = StudyPlanner()

    while True:

        print("\n")
        print("====================================")
        print("       SMARTSTUDY PLANNER")
        print("====================================")
        print("1. Add Study Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Search by Subject")
        print("6. View Study Progress")
        print("7. Exit")
        print("====================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            planner.add_task()

        elif choice == "2":
            planner.view_tasks()

        elif choice == "3":
            planner.complete_task()

        elif choice == "4":
            planner.delete_task()

        elif choice == "5":
            planner.search_subject()

        elif choice == "6":
            planner.show_progress()

        elif choice == "7":
            print("\nThank you for using SmartStudy!")
            print("Keep learning and keep growing!")
            break

        else:
            print("Invalid choice! Please select 1-7.")


# Run the application

if __name__ == "__main__":
    main()
