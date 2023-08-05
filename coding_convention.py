import json

class StudentManager:
    """Class to manage student records."""

    def __init__(self, file_path="student_records.json"):
        """
        Initialize the StudentManager.

        Parameters:
        file_path (str): Path to the JSON file to store student records.
        """
        self.file_path = file_path
        self.load_records()

    def load_records(self):
        """Load student records from the JSON file."""
        try:
            with open(self.file_path, "r") as file:
                self.records = json.load(file)
        except FileNotFoundError:
            self.records = []

    def save_records(self):
        """Save student records to the JSON file."""
        with open(self.file_path, "w") as file:
            json.dump(self.records, file)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student to the records.

        Parameters:
        student_id (int): Student ID.
        name (str): Student's name.
        age (int): Student's age.
        grade (str): Student's grade.

        Returns:
        str: Message indicating the success of adding the student.
        """
        new_student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
        }
        self.records.append(new_student)
        self.save_records()
        return "Student added successfully."

    def search_student(self, search_key):
        """
        Search for a student by student_id or name.

        Parameters:
        search_key (int or str): Student ID or name to search.

        Returns:
        dict or None: Student information if found, None if not found.
        """
        for student in self.records:
            if student["student_id"] == search_key or student["name"] == search_key:
                return {"age": student["age"], "grade": student["grade"]}
        return None

    def update_student(self, search_key, age=None, grade=None):
        """
        Update a student's information by student_id or name.

        Parameters:
        search_key (int or str): Student ID or name to search.
        age (int, optional): New age to update. Default is None.
        grade (str, optional): New grade to update. Default is None.

        Returns:
        str: Message indicating the success of updating the student.
        """
        for student in self.records:
            if student["student_id"] == search_key or student["name"] == search_key:
                if age is not None:
                    student["age"] = age
                if grade is not None:
                    student["grade"] = grade
                self.save_records()
                return "Student information updated successfully."
        return "Student not found."

# Example usage
if __name__ == "__main__":
    manager = StudentManager()

    # Add new students
    manager.add_student(101, "Alice", 20, "A")
    manager.add_student(102, "Bob", 21, "B")
    manager.add_student(103, "Charlie", 19, "C")

    # Search for a student
    student_info = manager.search_student(102)
    if student_info:
        print(f"Student found: Age - {student_info['age']}, Grade - {student_info['grade']}")
    else:
        print("Student not found.")

    # Update a student's information
    message = manager.update_student("Alice", age=21)
    print(message)
