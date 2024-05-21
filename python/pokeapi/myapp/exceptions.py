class CustomException(Exception):
    """A custom exception for the PokemonService."""
    def __init__(self, message="A custom exception occurred"):
        self.message = message
        super().__init__(self.message)