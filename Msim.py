import numpy as np




class Event:
    def __init__(self, type_desc, start_time, extra, function):
        self.type_desc = type_desc
        self.start_time = start_time
        self.extra = extra
        self.function = function

    def __str__(self):
        return "("+self.type_desc+","+str(self.start_time)+","+str(self.extra)+")"






class Sim:
    def __init__(self):
        self.events_list = []
        self.time_now = 0
        self.run_till = -1
        self.total_events_created = 0
        self.total_events_add_list = 0
        self.total_events_executed = 0

    def now(self):
        return self.time_now

    def set_run_till(self, t):
        self.run_till = t


    def create_event(self, type_desc, start, extra=None, f=None):
        if start<self.time_now:
            return False

        self.total_events_created += 1
        e = Event(type_desc, start, extra, f)
        return e

    def binary_search (self, arr, l, r, x):
        if r >= l: 
            mid = int(l + (r - l)/2)
            if arr[mid].start_time == x: 
                return mid

            elif arr[mid].start_time > x: 
                return self.binary_search(arr, l, mid-1, x) 

            else: 
                return self.binary_search(arr, mid+1, r, x) 
        else: 
            return l


    def add_event(self, evt):
        index = self.binary_search(self.events_list, 0, len(self.events_list)-1, evt.start_time)
        self.total_events_add_list += 1
        self.events_list = self.events_list[:index] + [evt] + self.events_list[index:] 


    def print_eventos(self):
        for i in range(len(self.events_list)): 
            print(self.events_list[i], end=">")

        print("\nNow: ",self.time_now,"\nTotal events:",len(self.events_list),"\n")

    def get_proximo_evento(self):
        if self.is_empty():
            return None
        else:
            p = self.events_list.pop(0)
            self.time_now = p.start_time
            self.total_events_executed += 1
            return p


    def validate_fila(self):
        for i in range(len(self.events_list)-1):
            if not self.events_list[i].start_time<=self.events_list[i+1].start_time:
                return False
        return True

    def is_next_event_valid(self):
        if len(self.events_list)==0:
            return False
        return self.events_list[0].start_time>self.run_till

    def run(self):
        while self.now()<self.run_till and not self.is_empty():
            if self.is_next_event_valid():
                break
            p = self.get_proximo_evento()
            print(self.now(), p)
            if p==None:
                return
            p.function(self, p)

            self.print_eventos()


    def is_empty(self):
        return len(self.events_list)==0

    def __str__(self):
        o = {"events_list_size": len(self.events_list),
        "time_now": self.time_now,
        "run_till": self.run_till,
        "total_events_created": self.total_events_created,
        "total_events_add_list": self.total_events_add_list,
        "total_events_executed": self.total_events_executed}
        return str(o)