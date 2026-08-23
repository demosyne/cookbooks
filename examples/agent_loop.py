"""Let your code perceive, act, and advance the world one step at a time.

Two hosted ticks plus the final question are expected to cost less than $0.25.
"""

from terrarium import Person, Place, Terrarium


def main() -> None:
    brain = "gpt-5.6-luna"
    workshop = Place("the workshop", "a workbench with a silent desk lamp")
    ada = Person(
        "Ada",
        "You are testing the desk lamp. Work carefully and report what you observe.",
        at=workshop,
        brain=brain,
    )
    world = Terrarium().world(
        places=[workshop],
        people=[ada],
        physics=brain,
        ticks_per_day=2,
    )

    for action in ("inspect the lamp and its switch", "turn the lamp on"):
        scene = ada.character.perceive()
        print(scene.text)
        ada.character.act(action)
        world.step()

    print(ada.ask("Did the lamp work?"))
    world.refresh()
    print(f"Cost: {world.cost}")


if __name__ == "__main__":
    main()
