
class KmapError(Exception):
    """ Base class for all kmap related errors. """
    pass

class InvalidInputError(KmapError):
    """ Minterm input not valid  """
    pass

class InputLengthError(KmapError):
    """ Amount of minterms entered out of range for specific kmap """
    pass
