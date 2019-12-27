import config.settings as const
from .position import Position

class Map:

    def __init__(self, filename):
        self.filename = filename
        
        self.paths = set()
        self.data = {
            "start_pos": set(),
            "end_pos" : set()
        }

        self.load_from_file()

    def __contains__(self, position):
        return position in self.paths

    @property
    def start(self):
        return list(self.data["start_pos"])[0]

    def load_from_file(self):

        with open(self.filename) as infile:
            for x, line in enumerate(infile):
                for y, c in enumerate(line):
                    if c == const.PATH_CHAR:
                        self._paths.add(Position(x,y))
                    elif c == const.START_CHAR:
                        self._paths.add(Position(x,y))
                        self._start.add(Position(x,y))
                    elif c == const.END_CHAR:
                        self._paths.add(Position(x,y))
                        self._end.add(Position(x,y))

    def main():
        map = Map('data/maps/map.txt')

        p = Position(-1, 0)
        print(p in map)

    if __name__ == "__main__":
        main()
