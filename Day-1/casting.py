#casting = Change a vaiable data type without changing the variable itself
a_Number_as_string = "2" #string
print (int (a_Number_as_string) + 2)
print(a_Number_as_string + str(2))
print(float(3))

fav_number = input("What is your favorate Number? > ")
print(type(fav_number))
fav_number_plus_three = int(fav_number) + 3