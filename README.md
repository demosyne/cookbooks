# Terrarium cookbooks

Small Python programs for building worlds of language-model characters. Each
cookbook uses the Terrarium SDK directly. There is no cookbook framework or
file format to learn.

## Start with a hosted model

You need Python 3.12+, a Terrarium API key, and the Terrarium SDK source. The
SDK is source-only during the private preview, so `uv sync` currently requires
access to `demosyne/terrarium`. This repository is ready for external installs
as soon as `terrarium-sdk` is published or its source becomes public.

```sh
git clone https://github.com/demosyne/cookbooks.git
cd cookbooks
uv sync
uv run terrarium configure
uv run examples/hosted.py
```

You can use `TERRARIUM_API_KEY` instead of `terrarium configure`. The hosted
example is one person, one place, and two ticks. It should cost less than
$0.25, but model prices can change. Re-running the same file attaches to its
live world instead of creating another one.

```python
from terrarium import Person, Place, Terrarium

brain = "gpt-5.6-luna"
room = Place("the workshop", "a desk lamp on a workbench")
ada = Person("Ada", "Test the lamp.", at=room, brain=brain)

world = Terrarium().world(
    places=[room],
    people=[ada],
    physics=brain,
    ticks_per_day=2,
)

for tick in world:
    print(tick.index, tick.people)

print(ada.ask("Did it work?"))
```

A hosted model is just its registry name. `Person` is the agent, `brain=` is
how it thinks, and `physics=` is the separate judge that decides what became
true.

## Bring your own model

Terrarium accepts an OpenAI-compatible client in the same `brain=` and
`physics=` positions. Point the standard OpenAI client at a model server, then
run the parallel example:

```sh
cp .env.example .env
# Edit .env, then let uv load it for this run.
uv run --env-file .env examples/self_hosted.py
```

The endpoint must be reachable from the Terrarium deployment. It must expose
`GET /v1/models` and Chat Completions with tool calling and JSON-schema output.
If `/models` reports one model, the SDK selects it automatically. For an
endpoint with several models, pass the same explicit `model=` to `Person(...)`
and `Terrarium.world(...)`.

The hosted and self-hosted examples define the same world. Only these lines
change:

```python
# Hosted
brain = "gpt-5.6-luna"

# Self-hosted
brain = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)
```

The endpoint and model reference are part of the world definition. The API
key is sent separately when the world is created, sealed under that run, and
never returned in the definition.

## Examples

- [`hosted.py`](examples/hosted.py) — the smallest hosted world.
- [`self_hosted.py`](examples/self_hosted.py) — the same world on a model you
  operate.
- [`multi_model.py`](examples/multi_model.py) — different brains for different
  characters and a separate physics model.
- [`agent_loop.py`](examples/agent_loop.py) — perceive, act, and advance one
  step at a time from your own agent loop.

Examples make real model calls. Read the file and check current model pricing
before running it. Interrupting the local process does not erase a created
world.

## Write a cookbook

Keep it as one executable Python file:

1. Describe locations with `Place`.
2. Describe characters with `Person` and seat each one with `at=`.
3. Call `Terrarium().world(...)` with the places, people, and physics brain.
4. Iterate the world for autonomous runs, or use
   `person.character.perceive()`, `.act()`, and `world.step()` when your agent
   owns the loop.
5. Put execution in `main()` so tools and tests can import the file without
   spending credits.

Prefer the smallest world that demonstrates one idea. Do not wrap the SDK in a
registry, loader, or second configuration system. See
[`AGENTS.md`](AGENTS.md) for the compact authoring contract and the
[Terrarium SDK](https://github.com/demosyne/terrarium) for the full API guide.

## Check changes

```sh
uv sync
uv run ruff check .
uv run ruff format --check .
uv run python -m compileall -q examples
```

Never commit `.env`, model credentials, private endpoints, organization IDs,
or world IDs.
