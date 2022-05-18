import requests
import datetime as dt
import os


class DateTimeFunctions:
    @staticmethod
    def fetch_datetime():
        ipv4 = requests.get('https://checkip.amazonaws.com').text.strip()

        datetime = requests.get(f'https://timeapi.io/api/Time/current/ip?ipAddress={ipv4}').json()

        year = datetime['year']
        month = datetime['month']
        day = datetime['day']
        hour = datetime['hour']
        minute = datetime['minute']

        return dt.datetime(year, month, day, hour, minute)

    @staticmethod
    def strdatetime_to_datetime(str_time):
        # converts the datetime got from "Qdate/timeEdit" (string object) to DateTime object
        date, time, ampm = str_time.split(' ')
        month, day, year = date.split('/')
        hour, minute = time.split(':')

        if ampm == 'PM':
            if int(hour) != 12 and int(hour) + 12 < 24:
                hour = int(hour) + 12

        elif ampm == 'AM' and int(hour) == 12:
            hour = 0

        # in windows datetime format of qt is 5/10/2022 but in linux datetime format is 5/10/22
        year = year if os.name == 'nt' else 2000 + int(year)
        __datetime = dt.datetime(int(year), int(month), int(day), int(hour), int(minute))

        return __datetime


if __name__ == '__main__':
    print(DateTimeFunctions.fetch_datetime())
