# AGENTS.md — Terrarium cookbooks

This repository holds small, runnable examples for the public Terrarium SDK.
Each example is one Python file and uses only names exported from `terrarium`.

- Optimize for copying. Keep setup at the top, the world definition in the
  middle, and the run loop at the bottom.
- Use `Person`, `Place`, and `Terrarium.world(...)`. Do not add a cookbook
  framework, registry, loader, configuration layer, or wrapper around the SDK.
- Put network work in `main()` behind `if __name__ == "__main__"`. Importing an
  example must not create or advance a world.
- Keep public examples small: one idea, one or two characters, and the fewest
  ticks that demonstrate it. State the expected model cost when it is known.
- Read secrets and self-hosted endpoints from environment variables. Never
  commit a real API key, private hostname, tailnet address, organization ID,
  world ID, or internal model alias.
- A self-hosted model is an OpenAI-compatible URL, key, and optional model
  name. Pass an `openai.OpenAI` client directly. Do not add registration,
  proxy, relay, certificate, or connector setup.
- Keep hosted and self-hosted examples visibly parallel so a reader can see
  that only model selection changes.
- Run the checks in `README.md` after edits. Live runs spend model credits;
  only run one when the task explicitly calls for it.
