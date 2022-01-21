from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from Assignment2.moviecollection import MovieCollection


class TravelTrackerApp(App):
    status_text = StringProperty()
    current_sort = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        travel_locations = movieCollection()
        self.app_list = movie_name.load_places('movie.csv')

    def build(self):
        self.title = "Movie Tracker App"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def clear_input(self):
        self.root.ids.input_name.text = ""

    def create_widgets(self):
        self.status_text = "Click on a movie to change it to watched/unwatched."
        for location in self.app_list:
           movie_name = Button(text="{} in {}, priority {} ({})".format(movie[0],movie[1],movie[2],movie[3]))
           movie_name.bind(on_release=self.press_entry)
           movie_name = name
           if location[3] == "Unwatched":
                temp_button.background_color = [1,0,0,1]
           else:
               temp_button.background_color = [1,1,1,1]
           self.root.ids.entries_box.add_widget(temp_button)


    def press_entry(self, instance):

        name = instance.name
        if name[3] == "watched":
            name[3] = "unwatched"

        else:
            name[3] = "wateched"
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()
        if self.is_important(location[2]) == True:
            if name[3] == "watched":
                self.status_text = "You watched {}. ".format(name[0])
            elif name[3] == "unwatched":
                self.status_text = "You need to watch {}. Get going!".format(name[0])
        else:
            if name[3] == "watched":
                self.status_text = "You watched {}.".format(name[0])
            elif name[3] == "Unvisited":
                self.status_text = "You need to watch {}.".format(name[0])

    def add_place(self):
        temp_list = []
        name = self.root.ids.input_name.text

        try:
            priority = int(self.root.ids.input_priority.text)
            if name == "" or country == "" or priority == "":
                self.status_text = "All fields must be filled in."
            elif priority <= 0:
                self.status_text = "INVALLD number input."
            else:
                temp_list.append(name)
                temp_list.append(country)
                temp_list.append(priority)
                temp_list.append("Unvisited")
                self.app_list.append(temp_list)
                self.root.ids.entries_box.clear_widgets()
                self.create_widgets()
                self.status_text = "{} has been added.".format(name)
        except ValueError:
            self.status_text = "Invalid input. Fill in all fields and a number is chosen for 'Priority'."
        self.root.ids.input_name.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def sort_priority(self):
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(2))
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def sort_alphabetical(self):
        self.app_list.sort()
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def sort_visited(self):
        from operator import itemgetter
        self.app_list.sort(key=itemgetter(3), reverse=False)
        print(self.app_list)
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def is_important(self,priority):
        if priority <= 2:
            return True

    def on_stop(self):
        import csv
        with open('movie.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.app_list)


TravelTrackerApp().run()