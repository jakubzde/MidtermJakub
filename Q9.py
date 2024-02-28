def days_passed_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))
    
    # Get the current date
    current_date = (28, 2, 2024)  # Assuming current date is 27th February 2024
    
    # Calculate the total days passed in the birth year (excluding birth day)
    days_passed_in_birth_year = (12 - month) * 30 + (30 - day)
    
    # Calculate the total days passed in the current year (excluding current day)
    days_passed_in_current_year = current_date[1] * 30 + current_date[0]
    
    # Calculate the total days passed between the birth year and the current year
    total_days_passed = (current_date[2] - year - 1) * 365 + days_passed_in_birth_year + days_passed_in_current_year
    
    return total_days_passed

birthday = "23-01-2003"
print("Days passed since birthday:", days_passed_since_birthday(birthday))