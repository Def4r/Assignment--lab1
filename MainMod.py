import time
import random
import sys

def Introduction():
    Title = "Welcome to Dungeon Hunters"
    for char in Title:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush

def ContiuneGame():
    Text = "Press"

Introduction()