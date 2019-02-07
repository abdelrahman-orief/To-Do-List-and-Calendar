from Algorithm.SQLite_Algorithm import *
import time
import datetime
from datetime import date


Date = time.strftime("%d/%m/%Y")
day, month, year = (int(x) for x in Date.split('/')) 
ans = datetime.date(year, month, day)

from datetime import time

def process_time(intime, start, end):
    if start <= intime <= end:
        return True
    elif start > end:
        end_day = time(hour=23, minute=59, second=59, microsecond=999999)
        if start <= intime <= end_day:
            return True
        elif intime <= end:
            return True
    return False

from datetime import datetime

def info_now():
    #Sees what the user has to do now and returns the message which the user will get when
    #when he will opens the Today tab
    list = strainer("", 'Type', 'Today')
    Times = []
    times = []

    for i in list:
        time = i[9].split('-')
        Times.append(time[0])
        times.append([time[0], time[1]])
    now = datetime.now().strftime("%H:%M")
    
    for i in times:
        State = process_time(now, i[0], i[1])
        if State == True:
            Time = '{}-{}'.format(i[0], i[1])
            
            for i in list:
                if i[9]==Time:
                    time = i[9].split('-')
                    return 'You should now be working on {} from {} to {}'.format(i[0], time[0], time[1])
    sl = [900, '00:00']
    FMT = '%H:%M'
    
    for i in Times:
        tdelta = datetime.strptime(i, FMT) - datetime.strptime(now, FMT)
        interval = int(tdelta.total_seconds()/60)
        if interval<0:
            continue
        if interval < sl[0]:
            sl.pop()
            sl.pop()
            sl.append(interval)
            sl.append(i)
    for i in list:
        if i[9].split('-')[0] == sl[1]:
            if sl[0] > 60:
                return 'In {} h {} min you should be working on {}'.format(sl[0]//60, sl[0]%60, i[0])
            return 'In {} minutes you should be working on {}'.format(sl[0], i[0])
    return "You haven't anything else schedueld for today. Enjoy!"
    
        
        
        
# Functions for Today Frame

def info_today():

    global Date
    global ans

    list = strainer('', '{}'.format(ans.strftime("%A")), 1.0)
    result_event = []
    result_todo = []
    
    for l in list:
        if int(l[16]) == 1:
            continue
        Name = l[0]

        Time = '{}:{}-{}:{}'.format(l[9], l[10], l[11], l[12])

        Repeat = [l[1], l[2], l[3], l[4], l[5], l[6], l[7]]
        x = 0
        rep_days = []
        Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for w in Repeat:
            if int(w) == 1:
                rep_days.append(Days[x])
                rep_days.append(', ')
            x +=1
        if len(rep_days)>0:
            rep_days.pop()
        days = ''.join(map(str, rep_days))

        Points = int(l[8])

        Number = int(l[15])

        if int(l[9]) == 00 and int(l[11]) == 00:
            result_todo.append([Name, Time, days, Points, Number])
        else:
            result_event.append([Name, Time, days, Points, Number])

    list = strainer('', 'Type', 'Work')

    for l in list:
        if l[13] == Date:

            if int(l[16]) == 1:
                continue
        
            Name = l[0]

            Time = '{}:{}-{}:{}'.format(l[9], l[10], l[11], l[12])

            Repeat = [l[1], l[2], l[3], l[4], l[5], l[6], l[7]]
            x = 0
            rep_days = []
            Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            for w in Repeat:
                if int(w) == 1:
                    rep_days.append(Days[x])
                    rep_days.append(', ')
                x +=1
            if len(rep_days)>0:
                rep_days.pop()
            days = ''.join(map(str, rep_days))

            Points = int(l[8])

            Number = int(l[15])
            
            if [Name, Time, days, Points, Number] not in result_event and [Name, Time, days, Points, Number] not in result_todo:
                if int(l[9]) == 00 and int(l[11]) == 00:
                    result_todo.append([Name, Time, days, Points, Number])
                else:
                    result_event.append([Name, Time, days, Points, Number])

            
        
    return result_event, result_todo

# Function for Calendar Frame

def sorting(L):
    splitup = L.split('/')
    return splitup[2], splitup[1], splitup[0]

def dates():
    list = strainer('', 'Type', 'Work')
    dates = []
    for i in list:
        if i[13]!=None:
            dates.append(i[13])
    dates.sort(key=sorting)
    unique = []
    [unique.append(item) for item in dates if item not in unique]
    return unique

def info_calendar():

    list = strainer('', 'Type', 'Work')
    date = dates()
    result = []

    for i in date:
        for l in list:
            if i == l[13]:
                
                if int(l[16]) == 1:
                    continue

                if int(l[9]) == 00 and int(l[11]) == 00:
                    continue
                
                Name = l[0]

                Date = l[13]

                Time = '{}:{}-{}:{}'.format(l[9], l[10], l[11], l[12])

                Repeat = [l[1], l[2], l[3], l[4], l[5], l[6], l[7]]
                x = 0
                rep_days = []
                Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                for w in Repeat:
                    if int(w) == 1:
                        rep_days.append(Days[x])
                        rep_days.append(', ')
                    x +=1
                if len(rep_days)>0:
                    rep_days.pop()
                days = ''.join(map(str, rep_days))

                Number = int(l[15])

                Points = int(l[8])

                result.append([Name, Date, Time, days, Points, Number])
                
    for l in list:
        if int(l[16]) == 1:
            continue

        if int(l[9]) == 00 and int(l[11]) == 00:
            continue
                
        Name = l[0]

        Date = l[13]

        Time = '{}:{}-{}:{}'.format(l[9], l[10], l[11], l[12])

        Repeat = [l[1], l[2], l[3], l[4], l[5], l[6], l[7]]
        x = 0
        rep_days = []
        Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for w in Repeat:
            if int(w) == 1:
                rep_days.append(Days[x])
                rep_days.append(', ')
            x +=1
        if len(rep_days)>0:
            rep_days.pop()
        days = ''.join(map(str, rep_days))

        Number = int(l[15])

        Points = int(l[8])

        if [Name, Date, Time, days, Points, Number] not in result:
            result.append([Name, Date, Time, days, Points, Number])
                
    return result

# Functions for Todo Frame

def info_todo():
    result = []
    list = strainer('', 'Type', 'Work')
    
    for l in list:
            if int(l[9]) != 00 and int(l[11]) != 00:
                continue
            
            if int(l[16]) == 1:
                continue
            
            Name = l[0]

            Date = l[13]

            Repeat = [l[1], l[2], l[3], l[4], l[5], l[6], l[7]]
            x = 0
            rep_days = []
            Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            for w in Repeat:
                if int(w) == 1:
                    rep_days.append(Days[x])
                    rep_days.append(', ')
                x +=1
            if len(rep_days)>0:
                rep_days.pop()
            days = ''.join(map(str, rep_days))

            Number = int(l[15])

            Points = int(l[8])

            result.append([Name, Date, days, Points, Number])
    return result




