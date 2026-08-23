"""Run a tiny Terrarium world with a hosted model.

Two ticks plus the final question are expected to cost less than $0.25.
"""

from terrarium import Person, Place, Terrarium


def main() -> None:
    brain = "gpt-5.6-luna"

    workshop = Place("the workshop", "a workbench with a silent desk lamp")
    ada = Person(
        "Ada",
        "You are testing the desk lamp. Turn it on and confirm that it works.",
        at=workshop,
        brain=brain,
    )

    world = Terrarium().world(
        places=[workshop],
        people=[ada],
        physics=brain,
        ticks_per_day=2,
    )

    for tick in world:
        for person in tick.people:
            print(f"{person.name} @ {person.at} — {person.doing}")

    print(ada.ask("Did the lamp work?"))
    world.refresh()
    print(f"Cost: {world.cost}")


if __name__ == "__main__":
    main()
