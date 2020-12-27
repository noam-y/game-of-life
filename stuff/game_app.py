import random


class GameOfLife:
    def __init__(
        self,
        min_for_life: int = 2,
        max_for_life: int = 3,
        birth: int = 3,
        initial_births: int = 400,
    ):
        # creating game board
        self.board = [[0 for j in range(50)] for i in range(50)]
        self.initial_births = initial_births
        self.min_life = min_for_life
        self.max_life = max_for_life
        self.birth = birth
        self.game_over = False
        self.round = 0

    def run_by_rounds(self, rounds: int = 50):
        self.first_round()

        for _ in range(rounds):
            print(f"round {self.round}")
            self.print_board()
            if not self.game_over:
                self.calc_next_turn()
                print("newround")
                self.round = 1
            else:
                break
        
        if not self.game_over:
            self.game_summary()

    def game_summary(self):
        if self.game_over:
            print(f"game is over, \n you played for {self.round} rounds.")
        else:
            print(f'it seems like life procceeds even after the number of rounds you asked for.')

    def first_round(self):
        newborn = []
        for _ in range(self.initial_births):
            newborn.append((random.randint(0, 49), random.randint(0, 49)))
        self.give_birth(newborn)
        self.round = 1

    def calc_next_turn(self):
        if not self.game_over:
            kill_list = []
            birth_list = []
            for w in range(len(self.board)):
                for h in range(50):
                    cell_index = (w, h)
                    alive_neighbours = self.get_alive_neighbours((w, h))

                    # print(f'my friends: w {w} h {h}', alive_neighbours < self.min_life, alive_neighbours > self.max_life)
                    if self.cell_status(cell_index) and (
                        alive_neighbours < self.min_life
                        or alive_neighbours > self.max_life
                    ):
                        kill_list.append(cell_index)

                    elif (
                        not self.cell_status(cell_index)
                        and alive_neighbours == self.birth
                    ):
                        birth_list.append(cell_index)

            self.give_birth(birth_list)
            self.kill(kill_list)
            print("listssss", kill_list, birth_list)

            if len(kill_list) == 0 and len(birth_list) == 0:
                self.game_over = True
                self.game_summary()

        else:
            print("game is already over.")

    def get_alive_neighbours(self, cell_index: tuple):
        alive_neighbours_counter = 0 
        relative_neighbour_locations = [(1, 0), (-1, 0), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for relative_location in relative_neighbour_locations:
            if cell_index[0] + relative_location[0] < len(self.board) - 1 and cell_index[1] + relative_location[1] < len(self.board[0]) - 1:
                neighbour_location = (cell_index[0] + relative_location[0], cell_index[1] + relative_location[1])
                if neighbour_location == 1:
                    alive_neighbours_counter += 1
        return alive_neighbours_counter

    def cell_status(self, cell_index: tuple):
        return self.board[cell_index[0]][cell_index[1]]

    def give_birth(self, list_of_indexes):
        for w, h in list_of_indexes:
            self.board[w][h] = 1

    def kill(self, list_of_tuples):
        for t in list_of_tuples:
            self.board[t[0]][t[1]] = 0

    def print_board(self):
        for row in self.board:
            print(row)

    def get_board(self):
        return self.board

    def new_game_by_rounds(self, rounds_to_play=50):
        self.first_round()


new = GameOfLife(max_for_life=3, initial_births=5)
