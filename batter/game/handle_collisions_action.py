import random
from game import constants
from game.action import Action
from game.point import Point
import sys

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"] # there's only one
        bricks = cast["brick"]

        ###### Handle collisions with the bricks ######
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                ball.set_velocity(ball.get_velocity().random_reverse())
        
        ###### Handle collisions with the paddle ######
        for piece in paddle:
            if ball.get_position().equals(piece.get_position()):
                ball.set_velocity(ball.get_velocity().random_reverse_x())

        ###### Handle collisions with the top ######
        for i in range(1, constants.MAX_X):
            if ball.get_position().equals(Point(i, 1)):
                ball.set_velocity(ball.get_velocity().reverse_y())

        ###### Handle collisions with the bottom ######
        for i in range(1, constants.MAX_X):
            if ball.get_position().equals(Point(i, constants.MAX_Y)):
                ball.set_velocity(ball.get_velocity().reverse_y())
                #sys.exit()

        ###### Handle collisions with the walls ######
        for i in range(1, constants.MAX_Y):
            if ball.get_position().equals(Point(1, i)) or ball.get_position().equals(Point(constants.MAX_X, i)):
                ball.set_velocity(ball.get_velocity().reverse_x())