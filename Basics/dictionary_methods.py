# get() Returns the value for specified key in the dictionary
# keys() Returns a copy of dictionary 's keys
# items() Returns a copy for dictionarie's key value pair
# values () Returns a copy of the values in the dictionary
# pop() Removes the item with the specified key
# popitem(O Removes the arbitrary key: value pair
# update() Adds the specified key-value pairs to dictionary
# copy() Returns a copy of the dictionary
# clear() Removes all the elements from the dictionary

demo_dict2 = {"qa":"testurl", "uat":"uaturl","preprod": "preprodurl"}
# print(demo_dict2.keys()) #returns all the keys
# print(demo_dict2.items()) #returns all the items within the dictionaries
# print(demo_dict2.values()) #returns all the key values
# print(demo_dict2.pop("uat")) #returns uat value
#print(demo_dict2.popitem()) #returns all the keys

# demo_dict2.update({"prod":"produrl"})
demo_copy= demo_dict2.copy()
print(demo_dict2)
print(demo_copy)
demo_copy.clear()
print(demo_copy)

