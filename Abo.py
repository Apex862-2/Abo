"""COPYRIGHT:
This Module Was Created By Apex862
A.K.A  Ethan
"""
import time
import typing
from ecapture import ecapture as ec
from ecapture import *
import os
import smtplib
import webbrowser
from datetime import datetime
import Abo_piano
import Abo_Errors
import random

def openp(app):
    app = app.lower()
    print("Opening..")
    print(app)
    print("..")
    print("..")
    os.system(app)


def getchords(mood):
    Abo_piano.chords(mood)


def webopen(search, engine):
    if engine == "google" or "Google" or "GOOGLE":
        webbrowser.open(f'https://www.google.com/search?client=firefox-b-d&q={search}')

    elif engine == "bing" or "BING" or "Bing":
        webbrowser.open(f'https://www.bing.com/search?q={search}&search=&form=QBLH')
    else:
        webbrowser.open(f'https://www.google.com/search?client=firefox-b-d&q={search}')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def Time():
    strtime = datetime.now().strftime("%H:%M:%S")
    print(f"the time is {strtime}")


def music(dir):
    print("Make Sure You Gave Me A Valid Music Path To Go To! Not The Song File")
    print("The File Must Contain Only Music:")
    songs = os.listdir(dir)
    print("songs: ", songs)


def takepic():
    print("wait a moment...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print(f"Errror:{random.randrange ,  random.random , random.betavariate }")
    # ec.capture(0, "Camera ", "img.jpg")


def createfile(content):
    note = content
    strtime = datetime.now().strftime("%H:%M:%S")
    file = open('note.txt', 'w')
    strtime = datetime.now().strftime("%H:%M:%S")
    file.write(strtime)
    file.write(" :- ")
    file.write(note)


def create_python(script_name, complexity_level):
    global script_func
    if complexity_level == "complex":
        script_func = """
    def main():
        print("Hello From Abo")
        pass

    if __name__ == "__main__":
        main()
    """
    elif complexity_level == "game":
        script_func = """
import sys
import pygame

pygame.init()

# create a display surface
display_width = 800
display_height = 600
display_surface = pygame.display.set_mode((display_width, display_height))

# set the title of the game
pygame.display.set_caption('My 3D Game Engine')

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update game objects
    # render game objects
    pygame.display.update()

    """
    elif complexity_level == "simple":
        script_func = """
    print("Hello, World!")
    """
    elif complexity_level == "3d":
        script_func = """
# Import required libraries
import pygame
from OpenGL.GL import *

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF|pygame.OPENGL)

# Set up OpenGL
glViewport(0, 0, 800, 600)
glClearColor(0.5, 0.5, 0.5, 1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, 800/600, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Main loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Render 3D objects
    # ...

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
"""
    # Create script file and write function
    with open(script_name + ".py", "w") as f:
        f.write(script_func)

    print("Script created successfully!")

greetings = ["Hello From Abo","Greetings This is Abo","Salutations from Abo","HELLO FROM ABO  https://We_have_no_website.com  ","Abo!!!","Hi from Abo","This is Abo","HI FROM THE ABO COMMUNITY"]
# ____________________________________________________
print(random.choice(greetings))
