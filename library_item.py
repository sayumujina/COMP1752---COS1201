class LibraryItem:
    def __init__(self, name, director, rating=0, play_count=0, key=None):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count
        self.key = key
        

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

    