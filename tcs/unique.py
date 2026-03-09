'''input =4
c
python 
java 
python 
output = 
unique courses = 3
c =1
java = 1
python = 2
'''
n = int(input("Enter the number of courses: "))

courses = []
for i in range(n):
    course = input("Enter the course: ")
    courses.append(course)

unique_courses = set(courses)
print("Unique courses =", len(unique_courses))

course_count = {}
for course in courses:
    if course in course_count:
        course_count[course] += 1
    else:
        course_count[course] = 1

for course, count in course_count.items():
    print(course, "=", count )
