# Task 1: Code Correction

# Original code
# weather = "sunny"

# if weather == "sunny":
# print("Wear sunglasses!")
# else:
# print("Take an umbrella!")

# My Code
# Both print statements should be indented 4 spaces or by tabbing.
weather = 'sunny'

if weather == "sunny":
    print('Wear sunglasses')
else:
    print("Take an umbrella!")


# Task 2: Your Mood Today
# Used conditionals to print appropriate message.
# Used .lower() method to ensure proper casing my user.


mood = input("How do you feel today?")

if mood.lower() == 'sad':
    print('I hope your day gets better.')
elif mood.lower() == 'happy':
    print("That's great to hear!")