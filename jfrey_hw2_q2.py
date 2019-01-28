def feel_temp():
    x = raw_input("Enter a temperature in degrees celsius: ")
    if x > 35:
        return "Hot"
    elif x >= 20:
        return "Warm"
    elif x >= 10:
        return "Cool"
    else:
        return "Cold"

