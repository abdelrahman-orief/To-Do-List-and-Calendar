import calendar
import datetime
import tkinter as tk
from datetime import date

#root = tk.Tk()
class Calendar:
    def __init__(self, parent, values):
        self.values = values
        self.parent = parent
        self.cal = calendar.TextCalendar(calendar.SUNDAY)
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.wid = []
        self.day_selected = 1
        self.month_selected = self.month
        self.year_selected = self.year
        self.day_name = ''
         
        self.setup(self.year, self.month)
         
    def clear(self):
        for w in self.wid[:]:
            w.grid_forget()
            #w.destroy()
            self.wid.remove(w)
     
    def go_prev(self):
        if self.month > 1:
            self.month -= 1
        else:
            self.month = 12
            self.year -= 1
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)
 
    def go_next(self):
        if self.month < 12:
            self.month += 1
        else:
            self.month = 1
            self.year += 1
         
        #self.selected = (self.month, self.year)
        self.clear()
        self.setup(self.year, self.month)
         
    def selection(self, day):
        self.day_selected = str(day).zfill(2)
        self.month_selected = self.month
        self.year_selected = self.year
        dt = '{}/{}/{}'.format(day, self.month, self.year)
        day, month, year = (int(x) for x in dt.split('/')) 
        ans = datetime.date(year, month, day)
        self.day_name = ans.strftime("%A")
         
        #data
        self.values['day_selected'] = str(day).zfill(2)
        self.values['month_selected'] = self.month
        self.values['year_selected'] = self.year
        self.values['day_name'] = ans.strftime("%A")
        self.values['month_name'] = calendar.month_name[self.month_selected]
         
        self.clear()
        self.setup(self.year, self.month)
         
    def setup(self, y, m):
        left = tk.Button(self.parent, text='<', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=1)
         
        header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)
         
        right = tk.Button(self.parent, text='>', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5)
         
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num)
         
        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    #print(calendar.day_name[day])
                    b = tk.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day))
                    self.wid.append(b)
                    b.grid(row=w, column=d)
                     
        sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)
         
        ok = tk.Button(self.parent, width=5, text='OK', command=self.kill_and_save)
        self.wid.append(ok)
        ok.grid(row=9, column=2, columnspan=3, pady=10)
         
    def kill_and_save(self):
        self.parent.destroy()

def popup():
            child = tk.Toplevel()
            cal = Calendar(child, data)

def print_selected_date():
            print(data)

#date = tk.Button(root, text='Date',command=popup, borderwidth=0, bg='white')
#print_button = tk.Button(root, text='print',command=print_selected_date)
#date.grid()
#print_button.grid()
data = {}

def today_date():
    now = datetime.datetime.now()
    data['day_selected'] = str(now.day).zfill(2)
    data['month_selected'] = str(now.month).zfill(2)
    data['year_selected'] = now.year
    data['day_name'] = now.strftime("%A")
    data['month_name'] = calendar.month_name[now.month]

    
def return_date():
    global data
    if len(data) == 0:
        return None
    date = '{}/{}/{}'.format(data['day_selected'], data['month_selected'], data['year_selected'])
    data = {}
    return date

#root.mainloop()

