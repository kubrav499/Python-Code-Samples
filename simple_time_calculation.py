def addMinutes(str, mins):
    # Splitting the given hour and minute expression into components
    hours, minutes = map(int, str.split(':'))

    # Calculating the total minutes
    totalMinutes = minutes + mins

    # Calculating the new hour and minute
    newHours = (hours + (totalMinutes // 60)) % 24
    newMinutes = totalMinutes % 60
    
    # Formatting the hour in a two-digit format
    return f"{newHours:02d}:{newMinutes:02d}"

print(addMinutes('11:30', 90))

