# Used to iterate over the sequence like list, string, dictionary, set or tuple
# Less like the for loop in other programming language

cities = [["Bangladesh", "Dhaka"],["Australia", "Sydney"],["Dhaka", "Gazipur"],["Australia", "Melbourne"]]
# for country,city in cities:
#     print("The country is " +country + " and city is " + city) # Iterates the values.

my_dictionay = dict(cities)
print(my_dictionay)
for country, city in my_dictionay.items():
    print(country, city)
    for s in country:
        print(s)