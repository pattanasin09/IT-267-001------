class Movie:
    def __init__(self) -> None:
        #protected attributes begin with_
        self._title = ''
        self._year = 0
        self._genre = ''
        self._rating = 6

    #protected method begin with _    
    def _add_movie(self,title,year,genre,ratting =6):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = ratting

    def _get_movie(self):
        print( f'title : {self._title}\nyear :{self._year}\nratting: {self._rating}')
