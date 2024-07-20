# Write your solution here:
class Series:
    def __init__ (self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = ", ".join(genres)
        self.rating = []
        self.average = "no ratings"            
        
    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.rating.append(rating)
            self.average = f"{len(self.rating)} ratings, average {(sum(self.rating) / len(self.rating)):.1f} points"

    def __str__ (self):
        return (f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\n{self.average}")
        

def minimum_grade(rating: float, series_list: list):
    series_nl = []
    
    for series in series_list:
        if sum(series.rating) / len(series.rating) >= rating:
            series_nl.append(series)

    return series_nl


def includes_genre(genre: list, series_list: list):
    series_nl = []
    
    for series in series_list:
        if genre in series.genres:
            series_nl.append(series)

    return series_nl

if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")

    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")

    for series in includes_genre("Comedy", series_list):
        print(series.title)