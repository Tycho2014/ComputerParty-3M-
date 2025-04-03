import os
import sys
import subprocess
import urllib.request
import shutil
import pyautogui
import pygame
import random
import time
from threading import Thread

# URL van het audiobestand
SON_URL = "https://www.dropbox.com/scl/fi/7njdtwjr6zeoqwsv3a527/son.mp3?rlkey=kdj9vpdimvvdep8p6xtwez0ga&st=oakwmmb5&dl=1"

# Maak een tijdelijke map aan
TEMP_DIR = os.path.join(os.getenv("TEMP"), "psychedelic_effect")
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Download het audiobestand
SON_PATH = os.path.join(TEMP_DIR, "son.mp3")
if not os.path.exists(SON_PATH):
    print("Audiobestand downloaden...")
    urllib.request.urlretrieve(SON_URL, SON_PATH)

# Installeer afhankelijkheden indien nodig
def install_dependencies():
    print("Installeren van vereiste modules...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--target", TEMP_DIR, "pygame", "pyautogui"
    ])
    sys.path.append(TEMP_DIR)  # Voeg lokale modules toe aan het pad

try:
    import pyautogui
    import pygame
except ImportError:
    install_dependencies()
    import pyautogui
    import pygame

# Initialiseer Pygame voor audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SON_PATH)
pygame.mixer.music.play(-1)  # Speel in een lus

# Functie voor psychedelisch visueel effect
def psychedelic_effect():
    screen_width, screen_height = pyautogui.size()
    pygame.display.set_caption("Psychedelisch Effect")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    start_time = time.time()

    running = True
    while running:
        # Controleer of 3 minuten zijn verstreken
        if time.time() - start_time > 180:
            running = False
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Willekeurige kleur
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.fill(color)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

# Start het visuele effect
psychedelic_effect()

# Opruimen na 3 minuten
print("Effect beëindigd. Verwijderen van tijdelijke bestanden...")
pygame.mixer.music.stop()
shutil.rmtree(TEMP_DIR)  # Verwijder de tijdelijke map
print("Bestanden verwijderd.")
