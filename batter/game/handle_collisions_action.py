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
        wall_left = cast["wall_left"]
        wall_right = cast["wall_right"]



        ###### Handle collisions with the bricks ######
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                ball.set_velocity(ball.get_velocity().random_reverse())
        
        ###### Handle collisions with the paddle ######
        for piece in paddle:
            
            if ball.get_position().equals(piece.get_position()):
                ball.set_velocity(ball.get_velocity().random_reverse_x())
                # location = ball.get_velocity()
                # location_x = location.get_x()  
                # if location_x > 0:
                #     ball.set_velocity(Point(location_x + .1, location.get_y()*-1))
                # else:
                #     ball.set_velocity(Point(location_x - .1, location.get_y()*-1))
        ###### Handle collisions with the top ######
        for i in range(1, constants.MAX_X):
            if ball.get_position().equals(Point(i, 1)):
                ball.set_velocity(ball.get_velocity().reverse_y())

        ###### Handle collisions with the bottom ######
        for i in range(1, constants.MAX_X):
            if ball.get_position().equals(Point(i, constants.MAX_Y)):
                # ball.set_velocity(ball.get_velocity().reverse_y()) ### Keep this for testing purposes
                sys.exit()

        ###### Handle collisions with the walls ######
        for wall_left in wall_left:
            if ball.get_position().equals(wall_left.get_position()):
                ball.set_velocity(ball.get_velocity().reverse_x())

        for wall_right in wall_right:
            if ball.get_position().equals(wall_right.get_position()):
                ball.set_velocity(ball.get_velocity().reverse_x())

