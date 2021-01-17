from timeit import default_timer as timer


class GameLogic:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.lines = 0

    def start_game(self):
        self.start_time = timer()

    def end_game(self):
        self.end_time = timer()
        self.total_time = self.end_time - self.start_time

    def load_data(self, file_name):
        with open(file_name, 'r') as f:
            data = f.readlines()
        data = [line.rstrip('\n') for line in data]
        return data

