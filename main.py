def is_happy_year(year: int) -> bool:
    """Return True if the year has all unique digits."""
    year_str = str(year)
    return len(set(year_str)) == len(year_str)


def next_happy_year(year: int) -> int:
    """Return the next happy year after the given year."""
    year += 1  # start with the next year
    while not is_happy_year(year):
        year += 1
    return year


def main():
    print(next_happy_year(2017))  # 2018
    print(next_happy_year(1990))  # 2013
    print(next_happy_year(2021))  # 2031


if __name__ == "__main__":
    main()
