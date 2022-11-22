# add(elem)
# remove(elem)
# discard(elem)
# pop()
# clear()
#
# Joining two sets
# union()
# update()
#
# Keep only duplicates
# intersections()
# intersection_update()
#
# Keep all excluding duplicates
# symmetric_difference()
# symmetric_difference_update()
#
# Returns set containing difference between two or more sets
# difference
# difference_update
#
# issubset()
# issuperset()

demo_set1 = {"Dhaka", "Gazipur", "Melbourne", "Sydney", "Sirajganj"}
demo_set2 = {"Dhaka", "Gazipur", "Melbourne", "Sydney", "Sirajganj", "New York"}


# demo_set1.add("Gold Coast") #adding an item
# print(demo_set1)
#
# demo_set1.remove("Gazipur") #removing an item
# print(demo_set1)
#
# demo_set1.discard("Melbourne") #removing an item
# print(demo_set1)
#
# demo_set1.pop() #removing an item
# print(demo_set1)
#
# demo_set1.clear()
# print(demo_set1)

# # Joining two sets/ intersection
# demo_set3 = demo_set1.union(demo_set2)
# print(demo_set3)
#
# demo_set1 = demo_set1.update(demo_set2)
# print(demo_set1)
demo_set3 = demo_set1.intersection(demo_set2)
print(demo_set3)
demo_set1 = demo_set1.intersection_update(demo_set2)
print(demo_set1)