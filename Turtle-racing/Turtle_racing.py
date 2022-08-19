import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
	no_of_races = 0
	while True: # telling the user to insert a valid number (2-10)
		no_of_races = input('Enter the number of racers (2 - 10): ')
		if(no_of_races.isdigit()):
			no_of_races = int(no_of_races)
		else:
			print('Input is not numeric... Try Again!')
			continue

		if(2 <= no_of_races <= 10):
			return no_of_races
		else:
			print('Number not in range 2-10. Try Again!')

def create_turtles(colors): # we get turtle of different colors
	turtles = []  # we are taking empty turtle, as we dont know particular turtles
	spacingx = WIDTH // (len(colors) + 1) # 500/(#turtles + 1) to get equi-distance from both side for extreme turtles
	for i, color in enumerate(colors):  # enumerates gives index and values of all elements in colors
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)

        # from center to their stating position we first penup() then move to them in their 1st place and then pendown()
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
  
		turtles.append(racer)

	return turtles

def race(colors):
	turtles = create_turtles(colors)

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20) # moving turtle randomly with pixel sizes 1 to 20
			racer.forward(distance)

			x, y = racer.pos()
			if (y >= HEIGHT // 2 - 10): #to return the winning turtle
				return colors[turtles.index(racer)]



def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers] # takes colors randomly from the COLOR list

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)



"""
--> Turtle speed lies in range (0 - 10)
--> If input is a number greater than 10 or smaller than 0.5, speed is set to 0;
--> SpeedStrings are mapped to speedvalues in the following way:
 1. 'fastest': 0
 2. 'fast': 10
 3. 'normal': 6
 4. 'slow': 3
 5. 'slowest: 1

"""