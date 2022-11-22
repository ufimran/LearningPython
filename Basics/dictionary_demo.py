# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Defining dictionaries
# Accessing items from dictionaries
# Adding items to dictionary
# Removing items from dictionary

demo_dict= {}
demo_dict1 = {1:20, 2:45, 3:50, 6:67}
demo_dict2 = {"qa":"testurl", "uat":"uaturl"}
demo_dict3 = {'qa':34, 3:"uaturl"}
print(demo_dict2)
demo_dict2['prod']='produrl'
print(demo_dict2)
demo_dict2.pop('qa')
print(demo_dict2)

# print(demo_dict1[1]) # prints 20
# print(demo_dict1[6]) # prints 67
# print(demo_dict2["uat"]) # prints 67