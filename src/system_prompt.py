import anyio
from claude_agent_sdk import ClaudeAgentOptions, query


async def main() -> None:
    options = ClaudeAgentOptions(
        system_prompt="claude_code",
    )
    async for message in query(prompt="2+2は？", options=options):
        print(message)


anyio.run(main)
