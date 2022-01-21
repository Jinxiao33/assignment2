from Assignment_2.place import Place
import csv

class moviecollection:
    def __init__(self, movies=[]):
        self.movies = movies

    def __repr__(self):
        return str(self.movies)

    def load_movies(self, file):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            self.movies = list(reader)
            for i in self.movies:
                i[2] = int(i[2])
                if i[3] == 'n':
                    i[3]= 'unwatched'
                elif i[3] == 'v':
                    i[3] = 'watched'
            return self.movies

    def save_file(self, file):
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.movies)
        print("Your file has been updated and saved!")

    def add_place(self, location):
        temp_list = []
        temp_list.append(location.name)
        temp_list.append(location.check_watched())
        self.movies.append(temp_list)
        return self.movies

    def sort_watched(self, list_to_sort):
        from operator import itemgetter
        list_to_sort.sort(key=itemgetter(3), reverse = False)
        return list_to_sort
    pass