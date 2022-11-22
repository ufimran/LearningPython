# used to iterate block of code as long as test expression is true
# test expression is checked first, if expression is evaluated to true then the body of loop is executed
# conditions care used to stop the loops
# can iterate on list, strings, tuples, dictionary
#
# while test_expression:
#     body of the loop

# x = 0
# while x <= 10: #test_expression
#     print(x)
#     x = x + 1
#     print("inside while")
# print("Out of while loop")

city = "Melbourne"
x = 0
while x < len(city):
    print(city[x])
    x = x + 1
print("'Melbourne' is printed Separatetly")
