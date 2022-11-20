#len(s) : Return the number of items in an object, if object is string it will return string length
# x = "Umar Faruque"
# print(len(x))

#str() : Converts a specified value into a string.
# x = "Umar Faruque"
# y = 79895146
#
# #print(y.find("95")) # as y is integer, so it can't find the 95
# print(len(x))
# print(str(y))
# z = str(y)
# print(z.find("95")) # as z is string, so it can find the 95, String is Array so it shows the index of that particular sub string.

#upper() : Converts a string into upper case
# x = "Umar Faruque"
# y = 79895146
# print(x.upper())

#count(sub[, start[,end]]) : Returns the number of times a specified value is found.
# x = "UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE"
# y = 79895146
# print(x.count("UMAR"))
# print(x.count("M", 10, 30))


#isupper() : Returns True if all characters in the string are upper case
#islower() : Retursn True if all characters in the string are lower case
#rsplit : Splits a string into a list, starting from the right.
# x = "UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE"
# y = 79895146
# print(len(x))
# print(str(y))
# z = str(y)
# print(z.find("95"))
# a = x.upper()
# print(x.count("UMAR", 10, 30))
# print(a.isupper())
# print(a.islower())

#split(sep=None, maxsplit=-1) : Splits the string at the specified separator, and returns a list.
# x = "UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE"
# print(x.split())


#strip(): Returns a trimmed version of the string
#lstrip([chars]): Removes any leading characters
#rstrip([chars]): Removes any trailing characters

# x = "              '$' '%' '#'UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE      "
# print(x.strip())
# #print(x.strip(':7\'')) # \ is escape character
# print(x.lstrip())
# print(x.rstrip())



#replace(old, new[, end]) : Replaces a specified phrase with another specified phrase.
# x = "UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE"
# print(x.replace("UMAR", "Umar", 2)) #replaces the string, As I used 2 so It only changed first 2 values

#find(sub[, start[, end]]) : Searches the string for a specified value and returns the position----
x = "UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE UMAR FARUQUE"

#index(sub[, start[, end]]) : Searches the string for a specified value and returns the position----