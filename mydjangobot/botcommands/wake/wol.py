from wakeonlan import send_magic_packet
from mydjangobot.discordbot_settings import macs

def wake(name):
    try:
        mac_adresses = macs[name]
        if isinstance(mac_adresses, str):
            mac_adresses = [mac_adresses]
        
        for mac in mac_adresses:
            send_magic_packet(mac)
        
        return True
    except:
        return False
