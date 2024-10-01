students = [{'name':'Alice','grades':[88, 92, 79, 85]},
                {'name':'Bob','grades':[75, 85, 90, 91]},
                {'name':'Charlie','grades':[95, 87, 91, 89]}]
def process_student_data(student):
    student_average = {}

    for i in students:
        name = i['name']
        grade = i['grades']

        average_grade = sum(grade)/len(grade)
        student_average = round(average_grade,2)
    return student_average
result = process_student_data(students)
print(result)