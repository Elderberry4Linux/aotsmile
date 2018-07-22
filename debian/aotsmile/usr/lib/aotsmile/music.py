import pygame





	#Music
try:
	pygame.mixer.music.load("/usr/share/aotsmile/sound/music/background_game.wav")
except:
	print("Cannot load background music")

