#FizzBuzz Game
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

    






# total = 0
# for number in range(2, 101, 2):
#   # if number %2 == 0:
#   total = total + number
# print(total)





# student_scores = input("Enter a list of student heights: ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# max = student_scores[0]

# for scores in student_scores:
#   if scores > max:
#     max = scores
# print(max)

# total_height = 0
# for height in student_heights:
#   total_height = total_height + height

# number_of_students = 0
# for student in student_heights:
#   number_of_students = number_of_students + 1

# average_height = round(total_height/number_of_students)
# print(average_height)

# # total_height = sum(student_heights)
# # number_of_students = len(student_heights)
# # average_height = total_height/number_of_students
# # print(round(average_height))

