import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['Alice', 'Bob', 'Charlie', "Dylan"]
    actions = ["run", "eat", "grab", "move", "sleep"]
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(ten_ev: list[tuple[str, str]])\
                  -> typing.Generator[tuple[str, str], None, None]:
    while ten_ev:
        to_del = random.choice(ten_ev)
        ten_ev.remove(to_del)
        yield to_del


if __name__ == "__main__":
    events = gen_event()
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")
    for to_delete in consume_event(ten_events):
        print(f"Got event from list: {to_delete}")
        print(f"Remains in list: {ten_events}")
