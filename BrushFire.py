import pygame
pygame.init()
import random
import time

background_color = (234, 212, 252)
w = pygame.display.set_mode((300, 300))
pygame.display.set_caption("BrushFire")
on = True
while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

smart = 0
strength = 0
speed = 0
talk = 0
magic = 0

name = input("NAME: ")
lastname = input("LAST NAME: ")
time.sleep(2.5)
mycode = random.randint(1000, 9999)
print("REGISTRATIOAN CODE: " + (str(mycode)) + ".")
print("So " + (str(mycode)) + " where do you come from? ") 
print("In the juck. (+4 speed)" )
print("With the top. (+4 talk)" )    
print("Round the thinkers. (+4 smart)" )
print("Against the odds. (+4 strength)" )
start1 = 100
start1 = input("1, 2, 3, 4 : ")
while (int(start1)) <= 5:
    if (int(start1)) == 1:
        speed += 4
        print("speed " + (str(speed)))
        time.sleep(2.5)
        break
    elif (int(start1)) == 2:
        talk += 4
        print("talk " + (str(talk)))
        time.sleep(2.5)
        break
    elif (int(start1)) == 3:
        smart += 4
        print("smart " + (str(smart)))
        time.sleep(2.5)
        break
    elif (int(start1)) == 4:
        strength += 4
        print("strength " + (str(strength)))
        time.sleep(2.5)
        break
    elif (int(start1)) <= 5:
        start1 = 100
        start1 = input("1, 2, 3, 4 : ")

print("Ok " + (str(mycode)) + " how did you work? ")
print("As a space juncker. (+2 strength +1 speed)" )
print("As a trooper. (+5 strength -2 talk)" )
print("Working as a top administrator of a planet. (+5 talk +2 smart -2 strength) ")
print("As a logistics wizard. (+4 speed +1 talk) ")
print("Doing jobs for the local strange man. (+1 magic +2 talk +1 speed)" )

start2 = 100
start2 = input("1, 2, 3, 4, 5 : ")
while (int(start2)) <= 6:
    if (int(start2)) == 1:
        strength += 2
        speed += 1
        print("strength " + (str(strength)))
        print("speed " + (str(speed)))
        time.sleep(2.5)
        break
    elif (int(start2)) == 2:
        strength += 5
        talk -= 2
        print("strength " + (str(strength)))
        print("talk " + (str(talk)))
        time.sleep(2.5)
        break
    elif (int(start2)) == 3:
        talk += 5
        smart += 2
        strength -= 2
        print("talk " + (str(talk)))
        print("smart " + (str(smart)))
        print("strength " + (str(strength)))
        time.sleep(2.5)
        break
    elif (int(start2)) == 4:
        speed += 4
        talk += 1
        print("speed " + (str(speed)))
        print("talk " + (str(talk)))
        time.sleep(2.5)
        break
    elif (int(start2)) == 5:
        magic += 1
        talk += 2
        speed += 1
        print("magic " + (str(magic)))
        print("talk " + (str(talk)))
        print("speed " + (str(speed)))
        time.sleep(2.5)
        break
    elif (int(start2)) <= 6:
        start2 = 100
        start2 = input("1, 2, 3, 4, 5 : ")
pygame.display.flip()




