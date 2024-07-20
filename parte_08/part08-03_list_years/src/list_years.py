# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    years = []
    for date in dates:
        years.append(date.year)
    return sorted(years)

if __name__ == "__main__":
    list_years()