def avg_speed(distance, hours, minutes):

    total_time_hours = hours + minutes / 60
    return distance / total_time_hours


distance = float(input("Distance in km: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

average_speed = avg_speed(distance, hours, minutes)
print(f"Average speed: {average_speed:.1f} km/h")
