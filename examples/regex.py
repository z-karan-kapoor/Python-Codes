import re

# numbers = re.findall('[0-9]+', 'sr23r3km56l')       #for multiple digit numbers
# print(numbers)


# digits = re.findall('[0-9]', 'sr23r3km56l')       #for single digit numbers
# print(digits)


# str = "Karan is here"                    #Search in a string
# x = re.search("^Karan.*her$", str)
# if(x):
#     print("true")
# else:
#     print("false")


# txt = "The rain in Spain"         #Splits a string at whitespaces
# x = re.split("\s", txt)
# print(x)


# txt = "The rain in Spain"         #Substitute a match with given string
# x = re.sub("rain", "9", txt)
# print(x)


txt = "The rain in Spain"           #Search any words that starts with "S"
x = re.search(r"\bS\w+", txt)
print(x.span())                     # span() for return start-end index