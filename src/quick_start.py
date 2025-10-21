import anyio
from claude_agent_sdk import query


async def main() -> None:
    async for message in query(prompt="2+2は？"):
        print(message)


anyio.run(main)
