from datetime import datetime

def dateformat(date):
    date_object = datetime.strptime(date, "%Y%m%dT%H%M%S")
    return date_object.strftime("%H:%M")