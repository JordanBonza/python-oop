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
    def __init__(self, start=0):
        """Create SerialGenerator with a starting number"""

        self.start = start
        self.counter = start
    
    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} counter={self.counter}>"

    def generate(self):
        """Generate a serial number that increments 1 each time"""

        if self.counter == self.start:
            self.counter += 1
            return self.start
        else:
            self.counter += 1
            return self.counter - 1
            
        
    def reset(self):
        """Reset the serial number back to starting value"""

        self.counter = self.start
    
