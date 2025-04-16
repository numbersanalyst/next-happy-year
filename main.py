def ifYearHappy(year: int) -> bool:
    """Return True if the year has all unique digits."""
    numbers = [int(x) for x in str(year)]
    counted_numbers = []
    for number in numbers:
        if number in counted_numbers:
            return False
        counted_numbers.append(number)
    return True


def happyYear(year: int) -> int:
    """Return the next happy year after the given year."""
    year += 1 # start with the next year
    while not ifYearHappy(year):
        year += 1
    return year


def main():
    print(happyYear(2017)) # 2018
    print(happyYear(1990)) # 2013
    print(happyYear(2021)) # 2031


if __name__ == "__main__":
    main()
