def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    count = len(marks_dict)
    return total / count if count else 0

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    length = len(scores)
    if length == 0:
        return 0
    if length % 2 == 1:
        return scores[length // 2]
    else:
        mid1 = scores[length // 2 - 1]
        mid2 = scores[length // 2]
        return (mid1 + mid2) / 2

def find_max_score(marks_dict):
    if marks_dict:
        return max(marks_dict.values())
    return 0

def find_min_score(marks_dict):
    if marks_dict:
        return min(marks_dict.values())
    return 0

def assign_grades(marks_dict):
    grades = {}
    for student, marks in marks_dict.items():
        if marks >= 90:
            grades[student] = 'A'
        elif marks >= 80:
            grades[student] = 'B'
        elif marks >= 70:
            grades[student] = 'C'
        elif marks >= 60:
            grades[student] = 'D'
        else:
            grades[student] = 'F'
    return grades

def count_grades(grades_dict):
    grade_count = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades_dict.values():
        if grade in grade_count:
            grade_count[grade] += 1
    return grade_count

def pass_fail_lists(marks_dict):
    passed_students = [name for name, marks in marks_dict.items() if marks >= 40]
    failed_students = [name for name, marks in marks_dict.items() if marks < 40]
    return passed_students, failed_students

def display_results(marks_dict, grades_dict):
    print("\nName       Marks     Grade")
    print("---------------------------")
    for student in marks_dict:
        print(f"{student:<10} {marks_dict[student]:<8} {grades_dict[student]}")

def main():
    print("Welcome to the GradeBook Analyzer")
    while True:
        try:
            n = int(input("Enter the number of students: "))
            if n <= 0:
                print("Please enter a positive integer for number of students.")
                continue
        except ValueError:
            print("Invalid input, please enter an integer value.")
            continue
        
        marks = {}
        for _ in range(n):
            name = input("Enter student name: ")
            while True:
                try:
                    score = int(input(f"Enter marks for {name}: "))
                    if score < 0 or score > 100:
                        print("Marks should be between 0 and 100. Please re-enter.")
                        continue
                    break
                except ValueError:
                    print("Invalid marks. Please enter an integer.")
            marks[name] = score
        
        average = calculate_average(marks)
        median = calculate_median(marks)
        maximum = find_max_score(marks)
        minimum = find_min_score(marks)
        
        grades = assign_grades(marks)
        grade_counts = count_grades(grades)
        
        passed_students, failed_students = pass_fail_lists(marks)
        
        print("\nStatistics:")
        print(f"Average Score: {average:.2f}")
        print(f"Median Score: {median}")
        print(f"Highest Score: {maximum}")
        print(f"Lowest Score: {minimum}")
        
        print("\nGrade Distribution:")
        for grade, count in grade_counts.items():
            print(f"{grade}: {count}")
        
        print("\nPassed Students:")
        print(", ".join(passed_students) if passed_students else "None")
        
        print("\nFailed Students:")
        print(", ".join(failed_students) if failed_students else "None")
        
        display_results(marks, grades)
        
        choice = input("\nDo you want to analyze again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using GradeBook Analyzer. Goodbye!")
            break

if __name__ == "__main__":
    main()
