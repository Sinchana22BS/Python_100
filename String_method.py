a = "SinchanaSuresh ,,,,,,"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip(","))
print(a.replace("Sinchana","Keerthi"))
print(a.split(" "))
blogHeading = "introduction to js"
print(blogHeading.capitalize()) #capitalize first letter

str = "Welcome"
print(len(str))
print(len(str.center(14)))
print(a.count("S"))

str1 = "Welcome to my home!!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

print(a.find("u"))
print(a.find("i"))
print(a.index("n"))
print(a.isalnum())

s = "abc"
print(s.islower())

d = "Happy new year\n"
print(d.isprintable()) #o\p will be false remove \n to get true

x = "           " #using space bar
print(x.isspace())

y = "   "    #using tab space
print(y.isspace())

i = "World Health Organisation"  # it will identify ecah and every word starting letter is capital
print(i.istitle())
print(i.startswith("World"))

p = "Python is a Interpreted Language" #it will convert uppercase into lower and vice-versa
print(p.swapcase())
print(p.title())

