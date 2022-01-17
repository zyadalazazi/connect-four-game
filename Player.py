
class Player:

    def __init__(self, name, color_chosen):
        self.name = name
        self.color_chosen = color_chosen

    def __str__(self):
        return '{0} has the {1} color'.format(self.name, self.color_chosen)