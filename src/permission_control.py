import asyncio
from typing import Any

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
)


async def custom_permission_handler(
    tool_name: str,
    input_data: dict[str, Any],
    context: dict,
) -> Any:
    """Custom logic for tool permissions."""

    print(f"============ {tool_name} =============")

    return {
        "behavior": "deny",
        "message": "Not allowed",
        "interrupt": True,
    }


async def main() -> None:
    options = ClaudeAgentOptions(
        can_use_tool=custom_permission_handler,
        allowed_tools=["Read", "Write", "Edit"],
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            "examples/hello_world.pyを編集して「こんにちは」と出力するようにして",
        )

        async for message in client.receive_response():
            # Will use sandbox path instead
            print(message)


asyncio.run(main())
