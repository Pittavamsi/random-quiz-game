print("Welcome to my game quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's start the quiz game:)")
score = 0

answer = input("When was the first computer invented?")
if answer.lower() == "1943":
    print('Correct answer!')
    score += 1
else:
    print("wrong answer!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct answer!')
    score += 1
else:
    print("wrong answer!")

answer = input("Who is currently the CEO of Microsoft?")
if answer.lower() == "Satya Nadella":
    print('Correct answer!')
    score += 1
else:
    print("wrong answer!")

answer = input("")
if answer.lower() == "power supply":
    print('Correct answer!')
    score += 1
else:
    print("wrong answer!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")