from game.action import Action

class DrawActorsAction(Action):
    """A code template for drawing the actors. The responsibility of this
    class of objects is to draw the actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (Outputservice): An instance of Outputservice.
        """
        
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """




############ CHANGE THE CODE OF THIS CLASS ############