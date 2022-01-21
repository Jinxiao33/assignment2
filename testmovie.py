from Assignment_2.place import Place


def run_tests():
    print("Test empty movie:")
    default_movie = movie()
    print(default_movie)
    assert default_movie.name == ""
    assert not default_movie.is_visited

    print("Test initial-value movie:")
    new_movie = Place("Dream", "Spain", 1, False)
    print(new_place)

    print("Test alternate method for marking watched")
    new_movie = Place("Dream", "Spain", 1, "n")
    print(new_movie)

    print(new_movie)
    print(new_movie.check_watched())
    print(new_movie.is_important())



run_tests()