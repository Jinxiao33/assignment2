import csv
import sys


def open_file():
    global movie_list
    with open('movies.csv', 'r') as file:
        reader = csv.reader(file)
        movie_list = list(reader)

def save_file():
    with open('movies.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)




def get_name():
    print("Welcome user!")
    user_name = input("What is your name?: ")
    while user_name == "":
        print("Your name cannot be blank!")
        user_name = input("What is your name?: ")
    print("Hello {}!".format(user_name))



def show_menu():
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("M - Mark a movie as watched")
    print("Q - Quit")


def list_out_movies():
    list_numb = 0
    unwatched_movies = 0
    max_length = 0
    for row in movie_list:
        for item in row:
            if len(item)> max_length:
                max_length = len(item)
    for row in movie_list:
        if row[3] == "v":
            list_numb += 1
            print("{:>2}. {:<{}} in {:>{}} priority {}".format(list_numb, row[0],max_length, row[1],max_length, row[2]))
        else:
            list_numb += 1
            print("*{}. {:<{}} in {:>{}} priority {}".format(list_numb, row[0],max_length, row[1],max_length, row[2]))
            unwatched_movies += 1
    return unwatched_movies


def execute_menu():
    show_menu()

    menu_choice = input("Please choose one of the above options: ").upper()
    if menu_choice == "L":
        unwatched_movies = list_out_movies()

        if unwatched_movies > 0:
            print("{} movies. You still want to watch {} movies.".format(unwatched_movies, unwatched_movies))
        else:
            print("No unwatched movies.")

    elif menu_choice == "A":
        movie_name = input("What is the movie's name?: ")
        while movie_name == "":
            print("Please enter a movie!")
            movie_name = input("What is the movie's name?: ")
        addition_list = []
        addition_list.append(movie_name)



    elif menu_choice == "M":
        unwatched_movies = list_out_movies()
        rows = 0
        if unwatched_movies == 0:
            print("There are no more unwatched movies.")
        else:
            movie_to_edit = input("Which movie would you like to mark aswatched?: ")
            for item in movie_list:
                rows+=1
                if movie_to_edit in item:
                    index_numb = movie_list.index(item)
                    movie_list[index_numb][3] = "v"
                    print("FOUND IT! The list has been updated!")
                    break
                else:
                    print("This is not in row {}.".format(rows))
    elif menu_choice == "Q":
        save_file()
        print("Thank you and goodbye!")
        sys.exit()
    else:
        print("That was an invalid input.")
        execute_menu()

    execute_menu()


def main():
    open_file()
    get_name()
    execute_menu()

main()