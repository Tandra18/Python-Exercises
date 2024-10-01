import matplotlib.pyplot as plt

courses = ["Maths", "Science", "English", "History",
           "Art"]
number_of_students = [40,35,30,25,20]

# plt.bar(courses,number_of_students)
# plt.xlabel(courses)
# plt.ylabel(number_of_students)
# plt.title("Bar Chart")
# plt.show()

# plt.pie(number_of_students,labels=courses,autopct='%1.1f%%')
# plt.title("Pie Chart")
# plt.show()

x_value = range(len(courses))
plt.scatter(x_value,number_of_students)
plt.xticks(x_value,courses)
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()
