from turtle import Turtle
import random


class Food(Turtle):
    """
    This class represents the food object in the snake game.

    The food object is a circle-shaped turtle that appears randomly within the game boundaries.
    The snake needs to eat this food to grow longer.
    """

    def __init__(self):
        """
        This function initializes the food object.

        - It creates a turtle object with a circle shape.
        - Sets the turtle speed to the fastest (0).
        - Lifts the pen to avoid drawing while moving.
        - Sets the color of the turtle to blue.
        - Sets the size of the turtle to a half-sized circle without an outline.
        """
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.color("blue")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5, outline=None)
        self.goto(self.xcor(), self.ycor())  # Move the turtle to the initial random position

    def take_new_position(self, body):
        """
        This function randomly positions the food object within the game boundaries.

        - It generates random x and y coordinates within the playable area (-280 to 280).
        - This ensures the x-coordinate is a multiple of 20 to align with the snake's body segments which move in
        increments of 20 pixels (similarly for y-coordinate).
        - It sets the turtle's position to the generated coordinates.
        - It checks for collision with the snake's body. If there's a collision, it generates a new random position
        until a safe spot is found.
        """
        self.setx(random.randint(-280, 280))
        while self.xcor() % 20 != 0:
            self.setx(random.randint(-280, 280))
        self.sety(random.randint(-280, 280))
        while self.ycor() % 20 != 0:
            self.sety(random.randint(-280, 280))
        self.goto(self.xcor(), self.ycor())  # Move the turtle to the new random position
        for part in body.full_body:
            if (self.xcor() == round(part.xcor())) and (self.ycor() == round(part.ycor())):
                self.take_new_position(body)
