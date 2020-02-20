# Msim: Simple python event simulator

Ez Pz to use event simulation in Python

1. Create a simulation

2. Set the time limit

3. Create the event

4. Create functions do handle events

5. Run the simulation



## Usage

Import MSim

    import Msim

Create the simulation object

    simulation = Msim.Sim()

Set the time limit for the simulation

    simulation.set_run_till(1000)

Add event

    evt = simulation.create_event(type_desc="create", start=simulation.now()+1, extra=None, f=func_creating)
    simulation.add_event(evt)


And here are the parameters that you can pass to the create_event()

| Parameter  | Description                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type\_desc | Description of the event                                                                                                                                        |
| start      | Start time \(When the event will be started\)                                                                                                                   |
| extra      | Any other extra information that you may need\. The simulation class do not access this parameter, so you can pass anything you want \(like IDs, counters\.\.\) |
| f          | Function that will be called once the event is started\. The parameters the function receive are the simulation and the event itself                            |


Create the functions that the events will call

    def func_creating(s, evt):
        evt = s.create_event(type_desc="terminate", start=s.now()+5, extra=None, f=func_terminating)
        s.add_event(evt)
     
    def func_terminating(s, evt):
        return

Run the simulation!

    simulation.run()



## Examples

Examples folder contain 2 examples you can try.

In "example1.py" the events keep recreating more of then.

In "example2.py" there is an special event that is recalled every 60 seconds.



## Extra information

#### Handler event function 

This is a basic template for a function that handle the events. The first parameter is aways the simulation and the second parameter is the event.

Every time a event is started the function asigned for this event is called.

    def func_creating(s, evt):
        pass



#### Repeting event 

For a event to be recalled you need to re-add this event to the event list in the simulation, so just call create event again


    def func_repeating(s, evt):
        evt = None
        evt = s.create_event(type_desc="repeating", start=s.now()+interval, extra=evt.extra, f=func_repeating)
        s.add_event(evt)

#### Information about Sim object

Parameters

| Parameter                | Description                                                                       |
|--------------------------|-----------------------------------------------------------------------------------|
| events\_list             | Entire list of events waiting to be started                                       |
| time\_now                | The actual time of the simulation                                                 |
| run\_till                | Time limit to stop the simulation \(may stop before if the event\_list is empty\) |
| total\_events\_created   | Information about total event created                                             |
| total\_events\_add\_list | Information about total events really added to the list                           |
| total\_events\_executed  | Information about total events executed                                           |


Methods

| Methods                                                        | Description                                                                                 |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| now\(\)                                                        | Return the actual time of the simulation                                                    |
| set\_run\_till\(t:int\)                                        | Set the time limit to run the simulation                                                    |
| create\_event\(type\_desc:str, start:int, extra=None, f=None\) | Create an event object                                                                      |
| add\_event\(evt:Evento\)                                       | Add the event object to the event\_list                                                     |
| run\(\)                                                        | Run the simulation                                                                          |
| is\_empty\(\)                                                  | Return if the event\_list is empty                                                          |
| print\_eventos\(\)                                             | Print the events in the event\_list                                                         |
| get\_proximo\_evento\(\)                                       | Return the next event and set the simulation to its time                                    |
| validate\_fila\(\)                                             | Validate if the event\_list is organized \(not need unless you are messing with the queue\) |
