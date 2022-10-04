from terminal_servicej import TerminalServicej
from jumper import Jumper
from puzzle import Puzzle


class Directorj:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._keep_guessing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalServicej()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_guessing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle._select_word()
        self._puzzle.word_guess()
        guess_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        self._puzzle.process_guess(guess_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self._jumper._parachute()
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if self._puzzle.can_keep_guessing():
            self._keep_guessing = False