from assignment2.moviecollection import moviecollection
from assignment2.movie import movie

import csv

def run_tests():
    print("Test empty moviecollection:")
    moviecollection = moviecollection()
    print(moviecollection)
    assert not moviecollection.movie

    print("Test loading movies:")
    moviecollection.load_movies('movie.csv')
    print(moviecollection)
    assert moviecollection.places

    print("Test adding new movie:")
    moviecollection.add_movie(Place("Smithfield", "Master", 5, False))
    print(movieollection.movies)



    print("Test sorting - by watched status")
    moviecollection.sort_watched(moviecollection.movies)
    print(movieollection)


    print("Test saving:")
    moviecollection.save_file('movie.csv')



run_tests()