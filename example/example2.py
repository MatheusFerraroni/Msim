import Msim

interval = 60


def func_creating(s, evt):
    evt = s.create_event(type_desc="terminate", start=s.now()+5, extra=None, f=func_terminating)
    s.add_event(evt)

def func_terminating(s, evt):
    return


def func_repeating(s, evt):
    evt = None
    evt = s.create_event(type_desc="repeating", start=s.now()+interval, extra=None, f=func_repeating)
    s.add_event(evt)


def main():
    simulation = Msim.Sim()
    simulation.set_run_till(1000)

    evt = simulation.create_event(type_desc="create", start=simulation.now()+1, extra=None, f=func_creating)
    simulation.add_event(evt)

    evt = simulation.create_event(type_desc="create", start=simulation.now()+2, extra=None, f=func_creating)
    simulation.add_event(evt)

    evt = simulation.create_event(type_desc="create", start=simulation.now()+3, extra=None, f=func_creating)
    simulation.add_event(evt)

    evt = simulation.create_event(type_desc="repeating", start=simulation.now()+interval, extra=None, f=func_repeating)
    simulation.add_event(evt)


    simulation.run()
    print(simulation)

if __name__ == '__main__':
    main()