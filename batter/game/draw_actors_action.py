from game.action import Action
<<<<<<< HEAD
=======
from game.output_service import OutputService

>>>>>>> main

class DrawActorsAction(Action):
    """A code template for drawing the actors. The responsibility of this
    class of objects is to draw the actors on the screen.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

<<<<<<< HEAD
    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (Outputservice): An instance of Outputservice.
        """
        
        self._output_service = output_service
=======
    

    def __init__(self, output_service):
        """The class constructor.

        Args:
        output_service (Outputservice): An instance of Outputservice.
        """

        self._output_service = output_service
        
        
>>>>>>> main

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
<<<<<<< HEAD

        self._output_service.clear_screen()
        for values in cast.values():  
            self._output_service.draw_actors(values)
=======
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
>>>>>>> main
        self._output_service.flush_buffer()