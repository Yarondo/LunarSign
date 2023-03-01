import datetime

zodiacs = {
    0: 'Monkey',
    1: 'Rooster',
    2: 'Dog',
    3: 'Pig',
    4: 'Rat',
    5: 'Ox',
    6: 'Tiger',
    7: 'Rabbit',
    8: 'Dragon',
    9: 'Snake',
    10: 'Horse',
    11: 'Sheep'
}

# Determine the Chinese zodiac based on the year
def get_zodiac(year):
    return zodiacs[year % 12]

# Get the current year
current_year = datetime.date.today().year

# Determine the Chinese zodiac for the current year
current_zodiac = get_zodiac(current_year)

print(f"The current Chinese zodiac is {current_zodiac}.")
