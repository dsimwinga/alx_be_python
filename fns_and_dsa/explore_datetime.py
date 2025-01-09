from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")


def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=number_of_days)
    future = current_date + delta
    future_date = future.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()