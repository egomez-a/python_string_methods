# Python String References #

a = "Hello, World! How are you, my friend?"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
b = a.split(",")  # Creates a list with various elements.
print(b)

print (a.capitalize()) # Converts the first character to upper case
print (a.casefold()) # Converts string into lower case
print (a.count("o")) # Returns the number of times a specified value occurs in a string

c = str(a.count("r"))
d = "There are "
e = " r in the sentence"
print(d + c + e)

# Another way to do it with the format function:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

print(a.endswith("!")) # Returns true if end character is the one given

print(a.find("W")) #	Searches the string for a specified value and returns the position of where it was found
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#Use a mapping table to replace "S" with "P":
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#Use a mapping table to replace many characters:
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

#The third parameter in the mapping table describes characters that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

#The same example as above, but using a dictionary instead of a mapping table:
txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))