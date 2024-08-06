# import time
# import psutil
# from pynput import keyboard
# import pygame  # Import pygame
# import threading
# import os
# import random
# import string

# # Initialize pygame mixer
# pygame.mixer.init()

# # Path to your sound files
# incorrect_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - incorrect.mp3"
# correct_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - Voicy.mp3"

# # Load sounds
# incorrect_sound = pygame.mixer.Sound(incorrect_key_sound)
# correct_sound = pygame.mixer.Sound(correct_key_sound)

# # Timestamp of the last key press
# last_key_press_time = time.time()

# # List of random characters
# random_chars = []

# # Function to generate 5 random characters
# def generate_random_chars():
#     global random_chars
#     random_chars = random.sample(string.ascii_lowercase, 5)
#     print(f"New random characters: {random_chars}")

# # Function to monitor keyboard activity
# def on_press(key):
#     global last_key_press_time, random_chars
#     if is_vscode_active():
#         last_key_press_time = time.time()
        
#         try:
#             if key.char in random_chars:
#                 print(f"Correct key '{key.char}' pressed")
#                 correct_sound.play()
#                 generate_random_chars()
#             elif key == keyboard.Key.backspace:
#                 print("Backspace key pressed")
#                 incorrect_sound.play()
#         except AttributeError:
#             pass

# # Function to check if the active window belongs to VSCode
# def is_vscode_active():
#     for proc in psutil.process_iter(['pid', 'name']):
#         if proc.info['name'] == 'Code.exe' or proc.info['name'] == 'code':  # Adjust for your OS
#             print("VSCode is running")
#             return True
#     return False

# # Generate initial random characters
# generate_random_chars()

# # Start the keyboard listener
# listener = keyboard.Listener(on_press=on_press)
# listener.start()

# # Keep the script running
# listener.join()


# import time
# import psutil
# from pynput import keyboard
# import pygame
# import threading
# import os
# import random
# import string

# # Initialize pygame mixer
# pygame.mixer.init()

# # Path to your sound files
# incorrect_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - incorrect.mp3"
# correct_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - Voicy.mp3"

# # Load sounds
# try:
#     incorrect_sound = pygame.mixer.Sound(incorrect_key_sound)
#     correct_sound = pygame.mixer.Sound(correct_key_sound)
# except pygame.error as e:
#     print(f"Error loading sound: {e}")

# # Timestamp of the last key press
# last_key_press_time = time.time()

# # List of random characters
# random_chars = []

# # Function to generate 5 random characters


# def generate_random_chars():
#     global random_chars
#     random_chars = random.sample(string.ascii_lowercase, 5)
#     print(f"New random characters: {random_chars}")

# # Function to monitor keyboard activity


# def on_press(key):
#     global last_key_press_time, random_chars
#     if is_vscode_active():
#         last_key_press_time = time.time()

#         try:
#             if key.char in random_chars:
#                 print(f"Correct key '{key.char}' pressed")
#                 correct_sound.play()
#                 generate_random_chars()
#             elif key == keyboard.Key.backspace:
#                 print("Backspace key pressed")
#                 incorrect_sound.play()
#         except AttributeError:
#             pass

# # Function to check if the active window belongs to VSCode


# def is_vscode_active():
#     for proc in psutil.process_iter(['pid', 'name']):
#         if proc.info['name'] == 'Code.exe' or proc.info['name'] == 'code':  # Adjust for your OS
#             return True
#     return False


# # Generate initial random characters
# generate_random_chars()

# # Start the keyboard listener
# listener = keyboard.Listener(on_press=on_press)
# listener.start()

# # Keep the script running
# listener.join()


import time
import psutil
from pynput import keyboard
import pygame
import random
import string

# Initialize pygame mixer
pygame.mixer.init()

# Path to your sound files
incorrect_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - incorrect.mp3"
correct_key_sound = "C:\\Users\\profe\\Documents\\duoLingoGamificationSound\\Duolingo Sounds - Voicy.mp3"

# Load sounds
try:
    incorrect_sound = pygame.mixer.Sound(incorrect_key_sound)
    correct_sound = pygame.mixer.Sound(correct_key_sound)
except pygame.error as e:
    print(f"Error loading sound: {e}")

# Timestamp of the last key press
last_key_press_time = time.time()

# List of random characters
random_chars = []

# Function to generate 5 random characters


def generate_random_chars():
    global random_chars
    random_chars = random.sample(string.ascii_lowercase, 5)
    print(f"New random characters: {random_chars}")

# Function to monitor keyboard activity


def on_press(key):
    global last_key_press_time, random_chars
    if is_vscode_active():
        last_key_press_time = time.time()

        try:
            if hasattr(key, 'char') and key.char in random_chars:
                print(f"Correct key '{key.char}' pressed")
                correct_sound.play()
                generate_random_chars()
            elif key == keyboard.Key.backspace:
                print("Backspace key pressed")
                incorrect_sound.play()
            elif key == keyboard.Key.alt_l:
                print("Alt key pressed")
                incorrect_sound.play()
            else:
                print(f"Other key '{key}' pressed")
        except AttributeError as e:
            print(f"AttributeError: {e}")

# Function to check if the active window belongs to VSCode


def is_vscode_active():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Code.exe' or proc.info['name'] == 'code':  # Adjust for your OS
            return True
    return False


# Generate initial random characters
generate_random_chars()

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the script running
listener.join()
