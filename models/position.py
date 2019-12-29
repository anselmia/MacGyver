class Positionable:
    
    def __init__(self):
        super().__init__()
        self.position = None
        

class Position:
    
    """Represent the position of an object in th game with x vertical and y horizontal
       Some method to move on the map"""
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)
    
    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
        return self.position == pos.position

    def up(self):
        x, y = self.position
        return Position(x-1, y)

    def down(self):
        x, y = self.position
        return Position(x+1, y)

    def left(self):
        x, y = self.position
        return Position(x, y-1)

    def right(self):
        x, y = self.position
        return Position(x, y+1)

    def main():
        pos = Position(1,2)
        pos1 = Position(1,3)

        print(pos == pos1)

    if __name__ == "__main__":
        main()
            