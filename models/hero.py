from .map import Map

class Hero:

    def __init__(self, map):
        self.map = map
        self.position = self.map.start()