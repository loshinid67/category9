def fuzzy_temperature(temp):
    if temp <= 20:
        return 0, 0
    elif temp <= 30:
        hot = (temp - 20) / 10
        warm = 1 - hot
        return warm, hot
    else:
        return 0, 1

def fuzzy_fan_speed(temp):
    warm, hot = fuzzy_temperature(temp)

    slow = warm * 30
    fast = hot * 100

    speed = (slow + fast) / (warm + hot)

    return speed

temp = float(input("Enter Temperature: "))

speed = fuzzy_fan_speed(temp)

print("Fan Speed:", round(speed, 2), "RPM")
