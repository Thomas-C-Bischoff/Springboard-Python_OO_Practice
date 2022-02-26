"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """Creates a New Serial Generator with a Given Starting Point"""
        self.start = start
    
    def __repr__(self):
        """Returns a Representation of Serial Generator"""
        return f"Serial Generator (start = {self.start})"
    
    def generate(self):
        """Returns the Next Serial Number in the Sequence"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets to the Start Number"""
        self.next = self.start