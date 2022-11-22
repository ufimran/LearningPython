# break: Breaks out from the nearest enclosing loop
# continue: Go to the start of nearest enclosing loop
#
# while <expression>:
#     <statement(s)>
#     break
#     <statement(s)>
#     continue
#     <statement(s)>
# <statement(s)>
#
# else clause:
# while <expression>:
#     <statement>
# else:
#     <statement>

# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1
#     # break # it came into the loop and encountered the break and break out of the loop and printed the output
#     continue
#     print("inside while") # won't print if we use continue condition
# print("out of the while loop")

x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    print("Parent while")
#     while y < 5:
#         print(y)
#         y = y +1 #using for fixing the infinite loop when happened in continue
#         #break #affect nearest enclosing loops
#         continue #infinite loop
#         print("Inner loop")
# print("Out of the loop")
    if x == 5:
        break
else:
    print("Out of the loop")