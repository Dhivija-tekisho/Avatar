import asyncio
import subprocess
import sys

async def run_server():
    process = await asyncio.create_subprocess_exec(
        sys.executable, "server.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[SERVER] {line.decode().rstrip()}")

async def run_agent():
    process = await asyncio.create_subprocess_exec(
        sys.executable, "agent.py", "dev",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[AGENT] {line.decode().rstrip()}")

async def main():
    # Run both concurrently
    await asyncio.gather(
        run_server(),
        run_agent()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Shutting down both services...")
