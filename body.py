# Import necessary libraries
from turtle import Turtle, Screen

SCREEN_SIZE = (612, 612)
MOVE_DISTANCE = 20


class Body:
    """
    This class represents the snake's body in the game. It manages the creation, movement,
    and state of the snake's body segments.

    The Body object:
      - Initializes the game screen and sets up the background.
      - Creates a list of turtle objects representing the snake's body segments using a helper function.
      - Defines the head of the snake as the first segment in the body list.
      - Provides methods to:
          - Create a turtle object with specific settings for the body segments (make_a_turtle).
          - Create a list of turtle objects representing the entire snake body (make_body).
    """
    def make_a_turtle(self, x, y=0):
        """
        This function creates a turtle object with the following properties:

        - Shape: Square
        - Hidden initially (shown later)
        - Fastest animation speed (0)
        - White color
        - Pen lifted (to avoid drawing while moving)
        - Teleported to a specific position (x, y)
        - Shown after teleportation
        """
        self.this_turtle = Turtle(shape="square")
        self.this_turtle.speed(0)
        self.this_turtle.color("white")
        self.this_turtle.penup()
        self.this_turtle.teleport(x=x, y=y)
        return self.this_turtle

    def make_body(self, size):
        """
        This function creates a list of turtle objects representing the snake's body segments.
        """
        parts = []
        x_pos = 0  # Initial x-position for the first segment (can be adjusted)
        for _ in range(size):
            a_turtle = self.make_a_turtle(x_pos)  # Create a turtle using the helper function
            x_pos -= 20  # Move the x-position for the next segment
            parts.append(a_turtle)
        return parts

    def new_segment(self, x, y):
        new_segment = self.make_a_turtle(x, y)  # Add new segment
        self.full_body.append(new_segment)


    # Define functions to control the snake's head direction
    def face_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)  # Set heading to 90 degrees (face up)

    def face_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)  # Set heading to 270 degrees (face down)

    def face_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)  # Set heading to 0 degrees (face right)

    def face_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)  # Set heading to 180 degrees (face left)

    def move(self):
        """
        This function simulates basic snake movement.

        It moves the snake by teleporting each segment to the position of the segment in front of it,
        creating the illusion of movement. This is done for better performance compared to moving each segment individually.
        """
        # Move each tail segment to the previous segment's position
        for i in range(len(self.full_body) - 1, 0, -1):
            xy_before_tail = (self.full_body[i - 1].xcor(), self.full_body[i - 1].ycor())
            self.full_body[i].goto(xy_before_tail[0], xy_before_tail[1])

        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def wall_collision(self):
        """
        This function checks for collision between the snake's head and the game boundaries.

        It takes the head turtle object of the snake as input.

        The function performs the following steps:
        1. Gets the current heading of the head (in degrees).
        2. Uses conditional statements to check if the head's x or y coordinate (rounded to the nearest integer)
           has gone beyond the playable area boundaries (set at +/- 280 pixels).
        3. If any of the conditions are true, the function returns True indicating a collision.
        4. If none of the conditions are met, the function returns False indicating no collision.
        """
        heading = self.head.heading()
        collided = ((heading == 0 and round(self.head.xcor()) > 280)
                    or (heading == 90 and round(self.head.ycor()) > 280)
                    or (heading == 180 and round(self.head.xcor()) < -280)
                    or (heading == 270 and round(self.head.ycor()) < -280))

        if collided:
            return True
        return False

    def self_collision(self):
        """
        This function checks if the snake's head has collided with its body.
        """
        for part in self.full_body[1:]:
            if self.head.distance(part) < 15:
                return True
        return False

    def __init__(self, size):
        """
        This function initializes a Body object with a snake body of the specified size.
        """
        # Set up the game screen
        self.this_turtle = None
        self.screen = Screen()
        self.screen.clear()
        self.screen.title("Joss Game")
        self.screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])  # Set screen width and height to 600 pixels
        self.screen.bgcolor("Black")

        # Create the snake body segments
        self.screen.tracer(0)  # Turn off automatic screen updates for better performance
        self.full_body = self.make_body(size)
        self.screen.update()  # Update the screen to show the initial body
        self.head = self.full_body[0]  # Define the head as the first segment
