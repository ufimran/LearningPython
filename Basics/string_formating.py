x = "Python Class"
y = "Umar Faruque"
print("1 Welcome to " + x + " from " + y + "'s youtube video") # '+' is the concatanation operator

print("2 Welcome to %s from %s" %(x,y))
print("3 Welcome to %s from %s" %("Java Class",y))

print("4 Welcome to {} from {}".format(x,y))
print("5 Welcome to {1} from {0}".format(x,y))
print("6 Welcome to {classname} from {academyname}".format(classname=x,academyname=y))