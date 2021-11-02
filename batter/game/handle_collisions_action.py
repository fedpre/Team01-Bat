import random
from game import constants
from game.action import Action

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
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]

        init_pos = paddle.get_position()
        positions = [init_pos]
        i = 0
        for _ in paddle.get_text():
            positions.append(init_pos.add_x(i+1))
            i += 1

        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("") 
                ball.set_velocity(ball.get_velocity().reverse())
            for position in positions:
                if ball.get_position().equals(position):
                    ball.set_velocity(ball.get_velocity().reverse())
            
            


####### CHANGE THE CODE ABOVE #######