# s[i:j] - slice of s from i to j
# s[i:j:k] - slice of s from i to j with step k
# s[startindex:endindex:step]

# s = "welcomeee to Umar Faruques coding"

# print(s[2]) # printing the value of string at 2 index
# print(s[-1]) # printing the value of string at last index

# print(s[0:8]) #prints 0-7 indexes
# print(s[4:8]) #prints 4-7 indexes

# print(s[4:8:2]) #only oe got printed

#print(s[0:-1]) #prints the whole string except last character


# print(s[::-1]) #reversing the string

y = "name, age, city"
print(y.index(','))
print(y[0:y.index(',')]) # prints the name
