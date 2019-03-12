students = 18.0
'%d' % students
'%f' % students
'%s' % students

format(students, '.3f')


def report_new(wages):
    students = wages.keys()
    students.sort()
    for student in students:
        print "{:<20}{:12.2f}".format(student, wages[student])

wages = {'mary': 6.238, 'joe': 5.45, 'john': 4.25}
report_new(wages)
