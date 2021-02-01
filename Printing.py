#Learn Python The Hard Way Exercises on Printing
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

def Formatting():  
    formatter = "{} {} {} {}"

    print(formatter.format(1, 2, 3, 4))
    print(formatter.format("one", "two", "three", "four"))
    print(formatter.format(True, False, False, True))
    print(formatter.format(formatter, formatter, formatter,
    formatter))
    print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))
#Call the function for formatting
Formatting()

def Printing():
    days = "Mon Tue Wed Thu Fri Sat Sun"
    months = "\nJan\nFeb\nMar\nApr\nMay\nJun\n"

    print("Days of the week",days)
    print("Months listed below",months)

    print("""
    So I can print
    as much as I want
    on multiple lines
    as long as I use three 
    double quotes
    """)
Printing()

def SpecialCharacters():
    special = "I am 6'2\". tall"
    singlQuote = 'I am 6\'2" tall.'

    print(special)
    print(singlQuote)
    
#Escape    What it does
#   \\     Backlash \
#   \'     Single Quote
#   \"     Double-Quote 
#   \a
#
#
#
#
#

SpecialCharacters()