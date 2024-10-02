from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class represents the scoreboard for the snake game.

    The Scoreboard object:
        - Inherits from the Turtle class to display text on the screen.
        - Manages the score and displays it to the user.
        - Shows a "GAME OVER" message and restart instructions when the game ends.
    """

    def __init__(self):
        """
        This function initializes the scoreboard object.

        - Sets the turtle color to light green.
        - Hides the turtle so only the text is visible.
        - Lifts the pen to avoid drawing lines while moving.
        - Positions the turtle at the top center of the screen (0, 280).
        - Clears the screen at this position to avoid overlapping text on the screen.
        - Initializes the score to 0.
        """
        super().__init__()
        self.color("light green")
        self.hideturtle()
        self.penup()
        self.goto(-130, 280)  # Clear the top center area for the score
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_score(self):
        """
        This function writes the current score to the screen.

        - Uses the write method from the Turtle class to display formatted text.
        - The formatted text includes "Score: " followed by the current score value.
        - Sets the font to Arial, size 25, and bold style.
        """
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", font=("Arial", 25, "bold"))

    def update_score(self):
        """
        This function updates the score by 1 and displays the new score.

        - Increments the score by 1.
        - Clears the previously written score using the clear method.
        - Calls the write_score function to display the updated score.
        """
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.clear()
        self.write_score()

    def game_over(self):
        """
        This function displays a "GAME OVER" message and restart instructions.

        - Positions the turtle at the center of the screen (0, 0).
        - Changes the color to red to highlight the message.
        - Writes "GAME OVER" in large, bold font (Arial, 40, bold).
        - Positions the turtle below the "GAME OVER" message (-120 on the y-axis).
        - Puts the pen down to start drawing a line.
        - Draws a horizontal line under the "GAME OVER" message.
        - Changes the color to white for the restart instructions.
        - Writes instructions to "Press space to restart" with smaller font (Arial, 20, normal).
        - Positions the turtle at the right side of the screen for restart instructions (98 on the x-axis).
        """
        self.goto(-125, 0)
        self.color("red")
        self.write(arg="GAME OVER", font=("Arial", 40, "bold"))
        self.goto(x=0, y=-120)
        self.pendown()
        self.goto(x=-98, y=-120)
        self.color("white")
        self.write(arg="Press space to restart", font=("Arial", 20, "normal"))
        self.goto(x=98, y=-120)
