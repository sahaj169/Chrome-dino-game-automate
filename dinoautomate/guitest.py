import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
	pyautogui.keyDown(key)
	return

def colorchange():
	for i in range(700,1000):
		for j in range(150,250):
			if data[i,j] <50:
				return True
	return False
def isCollide(data):
	# draw the rectange for birds
	# for i in range(300,350):
	# 	for j in range(410,540):
	# 		if data[i,j] <100:
	# 			hit("down")
	# 			hit("up")
	# 			return 

	# for cactus8
	if not colorchange():
		for i in range(350,570):
			for j in range(400,700):
				if data[i,j] <200:
					hit("up")
					return 
	else:
		for i in range(350,570):
			for j in range(400,700):
				if data[i,j] >50:
					hit("up")
					return 

	return 

if __name__ == '__main__':
	print("Hey..Dino game about to start in 4 seconds")
	time.sleep(4)
	hit("space")
	while True:
		image = ImageGrab.grab().convert('L')	
		data = image.load()
		isCollide(data)
			
		# print(asarray(image))
		# # draw the rectange for cactus
		# for i in range(350,400):
		# 	for j in range(560,700):
		# 		data[i,j] =0

		# # draw the rectange for birds
		# for i in range(300,350):
		# 	for j in range(410,563):
		# 		data[i,j] =150
		# image.show()
		# break
		# for i in range(700,1000):
		# 	for j in range(150,250):
		# 		data[i,j] =0
		# image.show()
		# break

		


