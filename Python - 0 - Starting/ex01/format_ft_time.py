import datetime


def check_month(month):
    switcher = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    return switcher.get(month, "error :invalid month")


timesince70 = datetime.datetime.now() - datetime.datetime(1970, 1, 1)

seconds_since_1970 = timesince70.total_seconds()

formatted_seconds_commas = "{:,.4f}".format(seconds_since_1970)
formatted_seconds_sci = "{:.4e}".format(seconds_since_1970)

print("Seconds since January 1, 1970:", formatted_seconds_commas, "or",
      formatted_seconds_sci, "in scientific notation")


today = datetime.date.today()
month = check_month(today.month)
data = month + " " + str(today.day) + " " + str(today.year)

print(data)
