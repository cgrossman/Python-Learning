#Various scripts on how to work through stringss

#Pass a variable through string
types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

print("Mary had a little lamb")
print("Who's fleece was white as {}.".format('snow')) #Passes 
print("And everywhere that Mary went")
print("." * 10) #Will print out 10 times


end1 ="H"
end2 ="e"
end3 ="l"
end4 ="l"
end5 ="o"
end6 ="w"
end7 ="o"
end8 ="r"
end9 ="l"
end10 ="d"

#Adding a comma at the end = Hello World
print(end1+end2+end3+end4+end5, end=' ')
print (end6+end7+end8+end9+end10)