list1 = ("Bangladesh", "USA", "Australia", "UK", "Qatar")
list2 = ("Dhaka", "New York", "Sydney", "London", "Doha")

# s = zip(list1, list2)
# print(list(s)) # maps the indexes accordingly, does't show the unmapped ones
#
# for x,y in zip(list1, list2):
#     print(x,y) #values have been mapped
total_cost = (45,67,65,87)
sale_price = (55,77,89,76)

for x,y in zip(total_cost,sale_price):
    print(y-x)

