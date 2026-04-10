#!/usr/bin/env python3
from typing import Generator
import random

def gen_event():
    names: list[str] = ["bob", "alice", "dylan", "charlie"]
    actions: list[str] = ["move", "use",
    "grab", "climb", "release", "jump", "run"]

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield(name, action)

def consume_event(events: list[tuple[str, str]])-> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = events.pop(0)
        yield event

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
 events_list = []
    for i in range(10):
        events_list.append(next(gen))
    print("Built list of 10 events", events_list)

for event in consume_event(events_list):
    print("Got event from list:", event)
    print("Remains in list:", events_list)
