def add_time(start, duration, day_of_week=None):
    """
    This function takes a starting time in 12-hour format (AM/PM), a duration in hours and minutes, 
    and optionally a starting day of the week. It returns the new time after adding the duration, 
    taking into account AM/PM and optionally the new day of the week.
    
    Parameters:
    - start (str): The starting time in "hh:mm AM/PM" format.
    - duration (str): The duration to add in "hh:mm" format.
    - day_of_week (str, optional): The starting day of the week (e.g., 'Monday'). The function will return
      the new day of the week after adding the duration.
      
    Returns:
    - str: The resulting time in "hh:mm AM/PM, Day of the Week" format, 
      including information about the number of days later if applicable.
    """
    
    # List of days of the week in lowercase for easy matching
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Split the start time into hour, minute, and period (AM/PM)
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Convert the 12-hour format time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12  # PM times need 12 hours added (except 12 PM itself)
    elif period == "AM" and start_hour == 12:
        start_hour = 0  # 12 AM is midnight, so convert to 0

    # Parse the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate total time in minutes
    total_start_minutes = start_hour * 60 + start_minute  # Start time in minutes
    total_duration_minutes = duration_hours * 60 + duration_minutes  # Duration in minutes
    total_minutes = total_start_minutes + total_duration_minutes  # Total time after adding the duration

    # Calculate the total number of days and remaining minutes for the new time
    total_days = total_minutes // (24 * 60)  # Total days passed (1 day = 1440 minutes)
    remaining_minutes = total_minutes % (24 * 60)  # Remaining minutes in the current day

    # Calculate the new hour and minute for the resulting time
    new_hour = remaining_minutes // 60  # New hour (in 24-hour format)
    new_minute = remaining_minutes % 60  # New minute

    # Adjust the period (AM/PM) based on the new hour
    if new_hour >= 12:
        period = "PM"
        if new_hour > 12:
            new_hour -= 12  # Convert hour to 12-hour format
    else:
        period = "AM"
        if new_hour == 0:
            new_hour = 12  # Midnight is 12 AM, not 0 AM

    # Format the new time as a 12-hour time with AM/PM
    new_time = f"{new_hour}:{new_minute:02d} {period}"

    # If a day of the week is provided, calculate the new day of the week
    if day_of_week:
        # Convert the day of the week to lowercase to handle any case inconsistencies
        day_of_week = day_of_week.strip().lower()
        # Find the current day's index and calculate the new day index after adding the total days
        current_day_index = days_of_week.index(day_of_week)
        new_day_index = (current_day_index + total_days) % 7  # Use modulo 7 to handle week wrapping
        new_day = days_of_week[new_day_index].capitalize()  # Capitalize only the first letter of the day
        new_time += f", {new_day}"

    # If there were days added, append the appropriate text
    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    return new_time
