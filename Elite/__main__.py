import asyncio
import importlib
from pyrogram import Client, idle
from Elite.helper import join
from Elite.modules import ALL_MODULES
from Elite import clients, app, ids, init_aiosession, close_aiosession

async def start_bot():
    # Initialize aiohttp session first
    await init_aiosession()
    print("LOG: Initialized aiohttp ClientSession ✅")
    
    await app.start()
    print("LOG: Founded Bot token Booting..")
    
    for all_module in ALL_MODULES:
        importlib.import_module("Elite.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    
    await idle()

async def shutdown():
    """Cleanup function"""
    await close_aiosession()
    print("LOG: Cleaned up aiohttp ClientSession ✅")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        loop.run_until_complete(shutdown())
        loop.close()
