from movie_private import Movie

class Documentary(Movie):
    def __init__(self, title, myear, genre) -> None:
        super().__init__(title, myear, genre)
        self.channel = None

    def add_channel(self,channel):
        self.channel =channel

    def show_channel(self):
        print(f'Channel : {self.channel}')