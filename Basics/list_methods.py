# list.append(x)
cities = ["Dhaka", "Gazipur", "Melbourne", "Sydney", "Sirajganj"]
print(cities)
cities.append("Tangail") #adds in the last of the list

# list.insert(i, x)
cities.insert(1, "Zylbrad")
print(cities) #adds in specified index

# list.remove(x)
cities.remove("Melbourne")
print(cities)

# list.pop([i])
cities.pop(3) #mentioned index has been popped out
print(cities)

# list.index(x[, start[, end]])
print(cities.index("Tangail"))

# list.count()
print(cities.count("Sirajganj"))

# list.sort(*, key=None, reverse=false)
cities.sort()
print(cities)

# list.reverse()
cities.reverse()
print(cities)

# list.copy()
new_cities= cities.copy()
print(new_cities)

# list.clear()
print(new_cities.clear())

