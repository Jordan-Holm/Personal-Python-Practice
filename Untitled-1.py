class_grades = [[0,53,84], [33,87,79], [75,100,94]]

for student_grades in class_grades:
    test_number = 1
    for test_grade in student_grades:
        test_result = f"%{test_grade}" if test_grade >= 60 else "FAILED"
        if test_grade >= 90:
            test_letter_grade = "A"
        elif test_grade >= 80:
            test_letter_grade = "B"
        elif test_grade >= 70:
            test_letter_grade = "C"
        else:
            test_letter_grade = "F"
        print(f"Test #{test_number} Grade: {test_letter_grade} {test_result}", end=", ")
        test_number += 1
    print()