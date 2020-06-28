import numpy as np


# Enum for the possible symbol options
class Symbol:
    CROSS = 1
    NOUGHT = 2
    EMPTY = 3


# Class that represents the TicTacToe game
class TicTacToe:

    def __init__(self):

        # Set up 3x3 board that is empty
        self.board = np.full((3, 3), Symbol.EMPTY)

        # Initialise the win states
        self.crosswin = np.full(3, Symbol.CROSS)
        self.noughtwin = np.full(3, Symbol.NOUGHT)

        # Dict to translate the int symbols to string representations
        self.symbol_to_board = {Symbol.CROSS: "X",
                                Symbol.NOUGHT: "O",
                                Symbol.EMPTY: "*"}

        # Win status will remain false until someone wins the game
        self.win_status = False

    # Updates board with symbol depending on which player's turn it is
    def update_board(self, coords, turn):
        x, y = coords

        # Get the symbol relative to the turn and add it to correct position
        symbol = symbol_on_turn(turn)
        self.board[x][y] = symbol

        self.print_current_board()

    # Prints out a representation of the game board to the terminal
    def print_current_board(self):

        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                symbol = self.board[i][j]

                if j < len(row) - 1:
                    end = " | "
                else:
                    end = "\n"

                print(self.symbol_to_board[symbol], end=end)
        print()

    # Checks that there if the game has been won
    def check_win(self):

        # Get the diagonal and the anti-diagonal of the board
        results = [np.diag(self.board), np.diag(np.fliplr(self.board))]

        # Append the rows and the columns of the board
        for i in range(3):
            results.append(self.board[i:i + 1])
            results.append(self.board.T[i:i + 1])

        # Now, check all results to see if there is a winner using allclose method
        for result in results:

            # Check if crosses win
            if np.allclose(result, self.crosswin):
                self.win_message("Crosses")
                return

            # Check if noughts win
            elif np.allclose(result, self.noughtwin):
                self.win_message("Noughts")
                return

    # Method that displays message depicting the winner and sets the game to be won
    def win_message(self, winner):
        print("Congrats! {} win!".format(winner))
        self.win_status = True

    # Method that checks if there are no "empty" symbols in the board - meaning the game can't be won
    def is_game_a_bogey(self):
        return np.all(self.board != Symbol.EMPTY)

    # Function that takes user input for the coords, and ensures their validity
    def receive_input(self):

        invalid = True
        while invalid:

            try:
                x = int(input("Please input the x position you want to choose: "))
                y = int(input("Please input the y position you want to choose: "))

            # If the inputs aren't of integer format, make user re-enter them
            except ValueError:

                print("Please use an integer value")
                continue

            # If inputs are out of range, make user re-enter them
            if x < 0 or x > 2:
                print("Please use a valid x value, e.g. 0, 1 or 2")
                continue
            if y < 0 or y > 2:
                print("Please use a valid y value, e.g. 0, 1 or 2")
                continue

            # Check that the board position hasn't got a symbol placed on it
            if self.board[x][y] != Symbol.EMPTY:
                print("You must choose a position that doesn't have a symbol already placed on it!")
                continue

            invalid = False
        return [x, y]


# Function that determines what symbol is to be placed on the board
def symbol_on_turn(turn):
    if turn:
        return Symbol.CROSS
    else:
        return Symbol.NOUGHT


# Function that displays whose turn it is to the player
def display_turn(turn):
    if turn:
        player = "Crosses"
    else:
        player = "Noughts"

    print("{} turn!".format(player), end="\n\n")


# Main function that runs the game
def main():
    # player1 = input("Please insert the name of player 1")[:12]
    # player2 = input("Please insert the name of player 2")[:12]

    game = TicTacToe()
    turn = True

    print("Welcome to TicTacToe!\n")

    while not game.win_status:

        display_turn(turn)

        # Obtain the coordinates from user
        coords = game.receive_input()

        # Place the symbol in the desired position
        game.update_board(coords, turn)

        # Check if game can't be won"
        if game.is_game_a_bogey():
            print("Game is a bogey, therefore no one winners")
            break

        # Check if the game can be won
        game.check_win()
        turn = not turn


main()
