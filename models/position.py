''' Import needed in the module '''
import random


class Position:

    """Represent the position of an object in th game with x vertical and y horizontal
       Some method to move on the board"""
    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    def __hash__(self):
        return hash(self.position)

    def __eq__(self, pos):
            return self.position == pos.position

    def up(self):
        ''' Substract 1 to x position (Move up) '''

        x, y = self.position
        return Position(x-1, y)

    def down(self):
        ''' Add 1 to x position (Move down) '''

        x, y = self.position
        return Position(x+1, y)

    def left(self):
        ''' Substract 1 to y position (Move left) '''

        x, y = self.position
        return Position(x, y-1)

    def right(self):
        ''' Add 1 to y position (Move right) '''

        x, y = self.position
        return Position(x, y+1)

    @staticmethod
    def get_random_free_position(board):
        ''' Get a random path remaining in the free path after removing object path on board '''
        return random.choice(Position.get_free_positions(board))

    @staticmethod
    def get_free_positions(board):
        ''' Get all path remaining in the free path after removing object path on board '''
        return [position for position in board.paths if position not in (board.start,
                                                                         board.end,
                                                                         board.tiles_position,
                                                                         board.enemies_position)]

    @staticmethod
    def next_possible_positions(board, position):
        ''' Take a position as arg and the board,
        check the free position inside the board positions,
        try to move the position in all possible move
        and return all the possible next position'''

        next_possible_positions = []
        free_positions = Position.get_free_positions(board)

        around_positions = []
        around_positions.append(getattr(position, "right")())
        around_positions.append(getattr(position, "left")())
        around_positions.append(getattr(position, "up")())
        around_positions.append(getattr(position, "down")())

        for pos in around_positions:
            if pos in free_positions:
                next_possible_positions.append(pos)

        return next_possible_positions
