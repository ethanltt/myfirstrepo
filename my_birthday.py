from datetime import datetime

def days_until_birthday(birthday):
    # Get today's date
    today = datetime.today()

    # Create a birthday date for the current year
    this_year_birthday = datetime(today.year, birthday.month, birthday.day)

    # If birthday has already passed this year, use next year's birthday
    if this_year_birthday < today:
        next_year_birthday = datetime(today.year + 1, birthday.month, birthday.day)
        days_left = (next_year_birthday - today).days
    else:
        days_left = (this_year_birthday - today).days

    return days_left

# Input your birthday (year is not necessary, just the month and day)
birthday = datetime(month=8, day=5, year=2020)  # Change to your birthday
days_left = days_until_birthday(birthday)

print(f"There are {days_left} days left until your birthday!")
