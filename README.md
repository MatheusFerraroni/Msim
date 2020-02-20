=================================
Msim: Simple python event simulator
=================================

## Usage

Import MSim::

    import Msim

Create the simulation object::

    simulation = Msim.Sim()

Set the time limit for the simulation::

    simulation.set_run_till(1000)

Add event::

    evt = simulation.create_event(type_desc="create", start=simulation.now()+1, extra=None, f=func_creating)
    simulation.add_event(evt)


And here are the parameters that you can pass to the create_event()::

| Parameter  | Description                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type\_desc | Description of the event                                                                                                                                        |
| start      | Start time \(When the event will be started\)                                                                                                                   |
| extra      | Any other extra information that you may need\. The simulation class do not access this parameter, so you can pass anything you want \(like IDs, counters\.\.\) |
| f          | Function that will be called once the event is started\. The parameters the function receive are the simulation and the event itself                            |


Create the functions that the events will call::

    def func_creating(s, evt):
        evt = s.create_event(type_desc="terminate", start=s.now()+5, extra=None, f=func_terminating)
        s.add_event(evt)
     
    def func_terminating(s, evt):
        return

Run the simulation!::

    simulation.run()



## Examples

Examples folder contain 2 examples you can try.

In "example1.py" the events keep recreating more of then.

In "example2.py" there is an special event that is recalled every 60 seconds.