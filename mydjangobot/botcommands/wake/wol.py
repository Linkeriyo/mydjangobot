from wakeonlan import send_magic_packet
import json
from mydjangobot.discordbot_settings import macs

def wake(name):
    try:
        mac_address = macs[name]
        send_magic_packet(mac_address)
        return True
    except:
        return False
