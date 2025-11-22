class SubjectMarksManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SubjectMarksManager, cls).__new__(cls)
            cls._instance.subject_marks = {}
        return cls._instance
    def my_name(self,name):
        print(f'may name is {name}')
    def add_mark(self, subject_name, subject_mark):
        self.subject_marks[subject_name] = subject_mark
        print(f"Added mark for {subject_name}: {subject_mark}")

    def find_best_subject(self):
        if not self.subject_marks:
            return None, None
        best_subject = max(self.subject_marks, key=self.subject_marks.get)
        return best_subject, self.subject_marks[best_subject]

    def find_worst_subject(self):
        if not self.subject_marks:
            return None, None
        worst_subject = min(self.subject_marks, key=self.subject_marks.get)
        return worst_subject, self.subject_marks[worst_subject]

    def calculate_average(self):
        if not self.subject_marks:
            return 0
        total_marks = sum(self.subject_marks.values())
        num_subjects = len(self.subject_marks)
        return total_marks / num_subjects


if __name__ == "__main__":
   
    manager = SubjectMarksManager()

    num_subjects = int(input("Enter the number of subjects: "))
    for i in range(num_subjects):
        subject_name = input(f"Enter the name of subject {i+1}: ")
        subject_mark = int(input(f"Enter the mark for {subject_name}: "))
        manager.add_mark(subject_name, subject_mark)

    best_subject_name, best_mark = manager.find_best_subject()
    worst_subject_name, worst_mark = manager.find_worst_subject()
    average_mark = manager.calculate_average()

    if best_subject_name:
        print(f"The subject with the best mark is {best_subject_name} with a mark of {best_mark}.")
        print(f"The subject with the worst mark is {worst_subject_name} with a mark of {worst_mark}.")
        print(f"The average mark is: {average_mark}")
    else:
        print("No subject data entered.")