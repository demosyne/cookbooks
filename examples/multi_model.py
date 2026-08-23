"""Give each character a hosted model and give physics a separate judge.

This is a larger example. Check model pricing before you run it.
"""

from terrarium import Person, Place, Terrarium


def main() -> None:
    green = Place(
        "the village green",
        "two campaign signs beside a circle of benches",
        "a notice: choose a councillor before the meeting ends",
    )
    maya = Person(
        "Maya",
        "You are running for councillor. You want to keep the green open to everyone.",
        at=green,
        brain="gpt-5.6-sol",
    )
    lin = Person(
        "Lin",
        "You are running for councillor. You want to repair the village well first.",
        at=green,
        brain="gemma-4-31b",
    )

    world = Terrarium().world(
        places=[green],
        people=[maya, lin],
        physics="gpt-5.6-luna",
        rules="Preserve what each candidate says and promises. There are no other people here.",
        ticks_per_day=2,
    )

    for tick in world:
        for person in tick.people:
            print(f"{person.name} @ {person.at} — {person.doing}")

    print("Maya:", maya.ask("What case did you make?"))
    print("Lin:", lin.ask("What case did you make?"))
    world.refresh()
    print(f"Cost: {world.cost}")


if __name__ == "__main__":
    main()
