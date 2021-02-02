#This section will go over how to user input variables and prompt users

def UserPrompt():
#Use print to ask the question
    print("How old are you?", end="")
    age = input()
    print("How tall are you?", end=""),
    height = input()
    print("How much do you weigh",end=""),
    weight = input()
    print(f"So you're {age} old, {height} tall, and you weigh {weight}")
    
    #Using the input variable as a prompt to simplify code
    newAge = input("How old are you")
    newHeight = input("How tall are you")
    newWeight = input("How much do you weigh")

    print(f"So you're {newAge} years old, {newHeight} tall, and you weigh {newWeight}...that's respectable")
UserPrompt()