def main():
    time = input("What time is it? ").strip().casefold()
    if time[-1] == "m" or time[-1] == "." :
        twelve_hour_time = convert12(time)
        compare12(twelve_hour_time)
    else:
        hours_after_midnight = convert(time)
        compare24(hours_after_midnight)

def compare24(n):
    if 7 <= n <= 8 :
        print("Breakfast time ")
    elif 12 <= n <= 13 :
        print("Lunch time ")
    elif 18 <= n <= 19 :
        print("Dinner time")

def compare12(n):
    if 7 <= n <= 8 :
        print("Breakfast time ")
    elif 12 <= n <= 13 :
        print("Lunch time ")
    elif 6 <= n <= 7 :
        print("Dinner time ")
   
def convert(time):
    hours_minutes = time.split(":")
    hours = hours_minutes[0]
    minutes = hours_minutes[1]
    number_hours = float(hours)
    number_minutes = float(minutes)
    minute_decimal = number_minutes / 60
    hours_after_midnight = number_hours + minute_decimal
    time = hours_after_midnight
    return hours_after_midnight

def convert12(time):
    converted_time = time.replace("a.m.", "")
    converted_time = converted_time.replace("p.m.", "")
    converted_time = converted_time.replace("am", "")
    converted_time = converted_time.replace("pm", "")
    hours_minutes = converted_time.split(":")
    hours = hours_minutes[0]
    minutes = hours_minutes[1]
    number_hours = float(hours)
    number_minutes = float(minutes)
    minute_decimal = number_minutes / 60
    twelve_hour_time = number_hours + minute_decimal
    return twelve_hour_time


if __name__ == "__main__":
    main()

