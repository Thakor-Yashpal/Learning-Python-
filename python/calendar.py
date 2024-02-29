import datetime
import calendar

def display_current_date():
    # Get the current date
    current_date = datetime.date.today()
    print("Current Date:", current_date)

def display_calendar():
    # Get the current year and month
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    
    # Create a calendar object for the current month
    cal = calendar.month(current_year, current_month)
    print("Calendar for the Current Month:")
    print(cal)

if __name__ == "__main__":
    display_current_date()
    print("\n")
    display_calendar()
