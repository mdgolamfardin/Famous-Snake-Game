# Import necessary libraries
from body import Body  # This file defines the Body class for the snake
from food import Food  # This file defines the Food class for the snake's target
import time  # To control the speed of the game loop
from scoreboard import Scoreboard  # To display the score.

EASY_DELAY = 0.0675  # Delay between movements for Easy difficulty (seconds)
MED_DELAY = 0.0475  # Delay between movements for Medium difficulty (seconds)
HARD_DELAY = 0.0330  # Delay between movements for Hard difficulty (seconds)
INTRO_PAUSE = 2  # Intro screen pause time (seconds)


def play():
    """
    This function is the main entry point for the game loop.
    It initializes the game, handles user input, and runs the main game loop.
    """

    # Create the snake body with a starting length of 3 segments
    body = Body(3)

    # Create the food object for the snake to eat
    food = Food()
    food.take_new_position(body)  # Place food in a random location avoiding the snake

    # Initialize game state variables
    body.screen.tracer(0)  # Turn off automatic screen updates for better performance
    score_board = Scoreboard()
    score_board.write_score()  # Display initial score
    body.screen.update()  # Manually update the screen once to show initial state

    # Ask user to choose difficulty level and set move delay accordingly
    difficulty = body.screen.textinput(title="Difficulty Level", prompt="Choose your level (Easy/Medium/Hard)").lower()
    if difficulty == "easy":
        move_delay = EASY_DELAY
    elif difficulty == "hard":
        move_delay = HARD_DELAY
    else:
        move_delay = MED_DELAY

    # Listen for keyboard input to control the snake
    body.screen.listen()
    body.screen.onkey(key="Up", fun=body.face_up)  # Bind "Up" key to face_up function
    body.screen.onkey(key="Down", fun=body.face_down)  # Bind "Down" key to face_down function
    body.screen.onkey(key="Left", fun=body.face_left)  # Bind "Left" key to face_left function
    body.screen.onkey(key="Right", fun=body.face_right)  # Bind "Right" key to face_right function

    # Show a short intro delay before starting the game loop
    time.sleep(INTRO_PAUSE)
    game_on = True

    # Main game loop - continues until the game ends (collision)
    while game_on:
        body.screen.update()
        time.sleep(move_delay)  # Introduce a short delay between movements
        body.move()
        # Check if the snake's head is close enough to the food to eat it

        # Check for collisions with walls or the snake's own body
        collision = body.wall_collision() or body.self_collision()

        # Handle collision (game over)
        if collision:
            game_on = False
            score_board.game_over()  # Display game over message with final score and high score.
            body.screen.update()
            body.screen.onkey(key="space", fun=play)  # Bind space key to restart the game

        scored = body.head.distance(food) < 15
        if scored:
            score_board.update_score()  # Update score
            body.new_segment(food.xcor(), food.ycor())  # Grow the snake
            food.take_new_position(body)  # Place food in a new random location

    # Keep the game window open until the user clicks on it to close
    body.screen.exitonclick()


# Start the game by calling the play function
play()
