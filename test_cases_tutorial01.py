import tutorial01 as A1

actual_answers = [9, 12,201,14.5,0,1,-253.8,-610.352,-0.002,[-2, -3.0, -4.5, -6.75, -10.125],[-2, -3.0, -4.5, -6.75, -10.125]
,[2, 6, 18, 54, 162]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(67,3)
student_answers.append(test_case_3)

test_case_4 = A1.divide(87,6)
student_answers.append(test_case_4)

test_case_5 = A1.divide(87,0)
student_answers.append(test_case_5)

test_case_6 = A1.add(-4,5)
student_answers.append(test_case_6)

test_case_7 = A1.multiply(-4.7, 54)
student_answers.append(test_case_7)



################################################################################################

# power

num1 = -2.5
num2 = 7
result = A1.power(num1,num2)
student_answers.append(result)

num1 = -2.5
num2 = -7
result = A1.power(num1,num2)
student_answers.append(result)

# for gp 

a = -2
r = 1.5
n = 5
gp1 = A1.printGP(a,r,n)
gp1 = list(gp1)
student_answers.append(gp1)

a = -2
r = 1.5
n = 5.0 #float number of n gives result 0
gp2 = A1.printGP(a,r,n)
gp2 = list(gp2)
student_answers.append(gp2)



################################################################################################

# Driver code 

a = 2 # starting number 
r = 3 # Common ratio 
n = 5 # N th term to be find 

gp = A1.printGP(a, r, n) 
gp = list(gp) 
student_answers.append(gp)


print(gp)
print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
