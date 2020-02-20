import Msim




def func_creating(s, evt):
    evt = s.create_event(type_desc="create", start=s.now()+6, extra=None, f=func_creating)
    s.add_event(evt)
    evt = s.create_event(type_desc="create", start=s.now()+7, extra=None, f=func_creating)
    s.add_event(evt)
    evt = s.create_event(type_desc="terminate", start=s.now()+5, extra=None, f=func_terminating)
    s.add_event(evt)

def func_terminating(s, evt):
    return



def main():
    simulation = Msim.Sim()
    simulation.set_run_till(50)

    evt = simulation.create_event(type_desc="create", start=simulation.now()+1, extra=None, f=func_creating)
    simulation.add_event(evt)


    simulation.run()
    print(simulation)

if __name__ == '__main__':
    main()