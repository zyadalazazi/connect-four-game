
"""
This module contains the Player class
Attributes:
    name: string
    color_chosen: string
"""
class Player:

    # The class constructor
    def __init__(self, name: 'str', color_chosen: 'str'):
        self.name = name
        self.color_chosen = color_chosen

    # Overriding the print() function
    def __str__(self):
        return '{0} has the {1} color'.format(self.name, self.color_chosen)