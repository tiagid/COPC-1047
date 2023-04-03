'''
Daniel Tiagi 4-1-23
seasons
'''


def is_valid_date(month, day):
    # Check if the month input is valid
    valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month not in valid_months:
        return False

    # Check if the day input is valid
    if day< 1 or day >31:
        return False

    return True

def get_season(month, day):
    if (month == "December" and day >= 21) or (month == "January") or (month == "February") or (month == "March" and day < 20):
        return "Winter"
    elif (month == "March" and day >= 20) or (month == "April") or (month == "May") or (month == "June" and day < 21):
        return "Spring"
    elif (month == "June" and day >= 21) or (month == "July") or (month == "August") or (month == "September" and day < 22):
        return "Summer"
    else:
        return "Fall"

month = input("Enter the month: ")
day = int(input("Enter the day: "))

if is_valid_date(month, day):
    season = get_season(month, day)
    print(season)
else:
    print("Invalid date entered.")
