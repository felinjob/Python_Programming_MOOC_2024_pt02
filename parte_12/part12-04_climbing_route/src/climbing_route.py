class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(items: list) -> list:
    def sort(item: ClimbingRoute) -> ClimbingRoute:
        return item.length
    
    return sorted(items, key=sort, reverse=True)

def sort_by_difficulty(routes: list) -> list:
    def sort(route: ClimbingRoute) -> ClimbingRoute:
        return (route.grade[0], route.grade[1], len(route.grade), route.length)
    
    return sorted(routes, key=sort, reverse=True)

if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 9, "7A")
    r3 = ClimbingRoute("Syncro", 14, "8C+")
    r4 = ClimbingRoute("Big cut", 36, "6B")
    r5 = ClimbingRoute("Fruit garden", 8, "6A")
    r6 = ClimbingRoute("No grip", 12 , "6B+")
    r7 = ClimbingRoute("Small steps", 13, "6A+")
    r8 = ClimbingRoute("The Swedish route", 42, "5+")
    for route in sort_by_difficulty([r1, r2, r3, r4, r5, r6, r7, r8]):
        print(route)