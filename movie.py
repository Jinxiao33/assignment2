class Place:
    def __init__(self, name="", is_visited=False):
        self.name = name
        self.is_watched = is_watched

    def __str__(self):
        return "{},{},{},{}".format(self.name, self.check_watched())

    def __repr__(self):
        return str(self)

    def str_watch_to_bool(self):

        if self.is_watched == 'v':
            self.is_watched = True
            return self.is_watched
        elif self.is_watchted == 'n':
            self.is_watched = False
            return self.is_watched

    def check_watched(self):
        self.str_vwatch_to_bool()
        if self.is_watched == False:
            return "Unvisited"
        if self.is_watched == True:
            return "watched"



    pass