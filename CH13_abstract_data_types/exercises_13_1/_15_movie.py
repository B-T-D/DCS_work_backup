class Movie:
    """A class representing a movie."""

    def __init__(self, title, year, actors):
        """Constructor.

        Args:
            self (Movie): the movie object.
            title (str): the title
            year (int): the year of release
            actors (list): a list of strings naming actors in the movie.
        """
        self._title = title
        self._year = year
        self._actors = actors

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_actors(self):
        """Return the list of the actors."""
        return self._actors

    def compare_actors(self, second_movie):
        """Return True if self and second_movie have any common actors,
        else False."""
        for actor in second_movie._actors:
            if actor in self._actors:
                return True
        return False

    # Mutator methods
    def add_actor(self, actor):
        """Add a new actor to the list of actors.

        Args:
            actor (string): a string naming the actor
        """
        self._actors.append(actor)
        

mymovie = Movie("I titled my movie this!", 2020, ["Rebekkanee Wortson",
                                                  "Junior (the hot one)",
                                                  "that one guy",
                                                  "Nicholas Cage"])
print(mymovie.get_actors())
mymovie.add_actor('Chet Manley')
print(mymovie.get_actors())

movie2 = Movie("Another movie", 2019, ["Korge Grault", "that one guy"])

print(mymovie.compare_actors(movie2))
