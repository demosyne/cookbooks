"""Run a tiny Terrarium world with one model served from your own endpoint."""

import os

from openai import OpenAI
from terrarium import Person, Place, Terrarium


def main() -> None:
    brain = OpenAI(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
    )

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
