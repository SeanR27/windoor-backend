import datetime

def dateString(dateString):
    dateArr = dateString.split("/")

    try:
        date = int(dateArr[0])
        month = int(dateArr[1])
        year = int(dateArr[2])
        datetime.date(year, month, date)
        return dateArr
    
    except ValueError:
        return None

