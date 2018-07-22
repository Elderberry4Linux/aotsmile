import pygame





	#Sounds
try:
	pain_sound = pygame.mixer.sound("/usr/share/aotsmile/sound/sounds/smile/pain.wav")
except:
	print("Cannot load one of the sounds. Sound lost unsure")
