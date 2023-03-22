def compare_date(date1, date2):
    date1 = list(map(int, date1.split(".")))
    date2 = list(map(int, date2.split(".")))
    return date1[2] > date2[2] or date1[2] >= date2[2] and date1[1] > date2[1] \
           or date1[2] >= date2[2] and date1[1] >= date2[1] and date1[0] >= date2[0]
