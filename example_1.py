import csv

# Содержимое файла subjects.csv
subjects = ["Математика", "Физика", "История", "Литература"]

# Запись в файл subjects.csv
with open('subjects.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(subjects)

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        words = value.split()
        for word in words:
            if not word[0].isupper() or not word.isalpha():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        setattr(obj, self.private_name, value)

class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    for subject in row:
                        self.subjects[subject] = {'grades': [], 'test_scores': []}
            print(f"Загруженные предметы: {list(self.subjects.keys())}")
        except Exception as e:
            print(f"Ошибка при загрузке предметов: {e}")

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not (2 <= grade <= 5):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not (0 <= test_score <= 100):
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if not test_scores:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects.values() for grade in subject['grades']]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        subjects_list = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subjects_list}"

# Пример использования
student = Student("Иван Иванов Иванович", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
