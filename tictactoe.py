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

        # Get the symbol relative to the turn and add it to correct position
        symbol = symbol_on_turn(turn)
        self.board[coords[0]][coords[1]] = symbol

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
                x, y = input("Input the 2 coords you want to place your symbol, separated by a space: ").split(" ")
                coords = [int(x), int(y)]

            # Error is risen when user doesn't provide valid input
            except ValueError:
                print("Please provide 2 integer values separated by a space")
                continue

            # Remove coordinates that are invalid
            coords = [i for i in coords if 0 <= i <= 2]
            if len(coords) != 2:
                print("Please use valid coordinates: e.g. 0, 1 or 2")
                continue

            # Check that the board position hasn't got a symbol placed on it
            if self.board[coords[0]][coords[1]] != Symbol.EMPTY:
                print("You must choose a position that doesn't have a symbol already placed on it!")
                continue

            invalid = False

        return coords


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

        # Check if game can't be won
        if game.is_game_a_bogey():
            print("Game is a bogey, therefore no one winners")
            break

        # Check if the game can be won
        game.check_win()
        turn = not turn


main()
