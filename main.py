#By Twotoque
#9 December 2021
import pygame, time
from pygame.locals import *

pygame.init()
pygame.mixer.init

surface = pygame.display.set_mode((500, 500))
white = (255, 255, 255)
black = (0, 0, 0)
cookie = pygame.image.load("cookie.png")
font  = pygame.font.SysFont("font/Inter-Black", 40)
fontCredit  = pygame.font.SysFont("font/Inter-Thin", 30)
n = 0
credit = fontCredit.render("By Twotoque", 1, black)
button = (120, 120, 250, 250)
double = 0
boop = "boop.wav"
musicFile = "15.wav"
print("Fake Cookie Clicker - v.01")

while True:
  event = pygame.event.poll()
  if event.type == MOUSEBUTTONDOWN and n >= 90:
    n = n + 3
    i = ("Cookies clicked: " + str(n))
    double = 2
    pygame.mixer.music.load("boop.wav")
    pygame.mixer.music.play(0)
  elif event.type == MOUSEBUTTONDOWN and n >= 15:
    n = n + 2
    i = ("Cookies clicked: " + str(n))
    pygame.mixer.music.load("boop.wav")
    pygame.mixer.music.play(0)
    double = 1
  elif event.type == MOUSEBUTTONDOWN:
    n = n + 1
    i = ("Cookies clicked: " + str(n))
    words = font.render(i, 1, black)
    pygame.mixer.music.load("boop.wav")
    pygame.mixer.music.play(0)
  else:
    i = ("Cookies clicked: " + str(n))
    words = font.render(i, 1, black)
    pygame.mixer.music.load("boop.wav")
    pygame.mixer.music.play(0)
  surface.fill(white)
  surface.blit(cookie, (120, 120))
  surface.blit(words, ([120, 70]))
  if double == 1:
    double = fontCredit.render("2x cookies unlocked", 1, black)
    surface.blit(double, ([190, 100]))
    double = 1
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(musicFile))
  elif double == 2:
    double = fontCredit.render("3x cookies unlocked", 1, black)
    surface.blit(double, ([190, 100]))
    double = 2

  surface.blit(credit, ([190, 400]))
  pygame.display.flip()
  time.sleep(10 / 1000) 
  
