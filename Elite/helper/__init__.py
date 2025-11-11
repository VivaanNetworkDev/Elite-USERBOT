import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Elite"])

async def join(client):
    try:
        await client.join_chat("VivaanNetwork")
    except BaseException:
        pass
