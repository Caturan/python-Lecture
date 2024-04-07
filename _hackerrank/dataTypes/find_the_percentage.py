"""
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
    Print the average of the marks array for the student name provided, showing 2 places after the decimal. 
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_query = student_marks[query_name]
    student_list = list(avg_query)
    avg_student = (student_list[1] + student_list[2] + student_list[0]) / 3
    formated_value = "{:.2f}".format(avg_student)
    print(formated_value)

"""
Ex input:
    2
    Harsh 25 26.5 28
    Anurag 26 28 30
    Harsh
"""