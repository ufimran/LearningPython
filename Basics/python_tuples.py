# Tuples are indexed, allow duplicates values and cannot be modified (immutable)

demo_tuple = (1,2,3,4,5)
demo_tuple1 = ("Dhaka","Dhaka","Gazipur","Munshiganj","Sylhet")
demo_tuple2 = (True, False, False, True)
demo_tuple3 = (True, 1, "Dhaka", 23.56)

# print(demo_tuple1[0])
# print(demo_tuple1[1])
# print(demo_tuple1.append("Kolkata")) # AttributeError: 'tuple' object has no attribute 'append'
# print(demo_tuple1.pop("Kolkata"))
# print(len(demo_tuple1)) #shows the length of the tuple

# print(demo_tuple1.count("Dhaka"))
# print(demo_tuple1.index("Munshiganj"))
#
# print(demo_tuple1[3])

# for x in demo_tuple1:
#     print (x)
# joined_tuple = demo_tuple1 + demo_tuple2 +demo_tuple3
# print(joined_tuple)
# print(type(joined_tuple))

print(demo_tuple2[0:3])