# Time Calculator

This Python program calculates the new time after adding a specific duration to a given starting time. The program handles 12-hour time format (AM/PM) and can calculate the new time across multiple days. Optionally, it can also return the new day of the week.

## **Functionality**
- Adds a duration (in hours and minutes) to a starting time (in 12-hour format).
- Converts the resulting time to 12-hour format (AM/PM).
- Optionally, returns the new day of the week if a starting day is provided.
- Handles day-overflows and correctly calculates "next day" or multiple days later.

## **Error Handling**
- The duration should be provided in "hh:mm" format.
- The starting time should be in "hh:mm AM/PM" format.
- The starting day of the week (optional) should be one of the valid days of the week (e.g., "Monday").

## **Example Usage**

### Example without day of the week:

```python
print(add_time('3:30 PM', '2:12'))  # Expected: '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # Expected: '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # Expected: '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))  # Expected: '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # Expected: '6:18 AM (20 days later)'


### Example with day of the week:


```python
print(add_time('3:30 PM', '2:12', 'Monday'))  # Expected: '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # Expected: '2:59 AM, Sunday (next day)'
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # Expected: '12:04 AM, Friday (2 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday'))  # Expected: '6:18 AM, Monday (20 days later)'
