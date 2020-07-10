
import time


def main():
    # GMT need to minus 8 hours or 28800 seconds
    # result = time.asctime(time.localtime(time.time() - 28800))
    result = time.asctime(time.localtime(time.time()))
    today_info = ""

    day = ""
    month = ""
    meridium = ""
    date = result[8] + result[9]
    hour = result[11] + result[12]
    minute = result[14] + result[15]
    year = result[20] + result[21] + result[22] + result[23]

    day_dictionary = {
        'Mon': "Isnin",
        'Tue': "Selasa",
        'Wed': "Rabu",
        'Thu': "Khamis",
        'Fri': "Jumaat",
        'Sat': "Sabtu",
        'Sun': "Ahad"
    }

    month_dictionary = {
        'Jan': "Januari",
        'Feb': "Februari",
        'Mar': "Mac",
        'Apr': "April",
        'May': "Mei",
        'Jun': "Jun",
        'Jul': "Julai",
        'Aug': "Ogos",
        'Sep': "September",
        'Oct': "Oktober",
        'Nov': "November",
        'Dec': "Disember",
    }

    if int(hour) >= 12:
        meridium = "PM"
    else:
        meridium = "AM"

    if int(hour) >= 13:
        hour = str(int(hour) - 12)
    elif int(hour) == 00:
        hour = str(int(hour) + 12)

    # Find Day
    for i in day_dictionary:
        if i in result:
            day = day_dictionary[i]

    # Find Month
    for i in month_dictionary:
        if i in result:
            month = month_dictionary[i]

    today_info = hour + ":" + minute + meridium + " " + day + " " + date + " " + month + " " + year
    print(result)
    print(today_info)
    return today_info
main()
