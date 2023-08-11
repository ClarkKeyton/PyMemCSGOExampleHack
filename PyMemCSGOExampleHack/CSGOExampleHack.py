from pymem.process import module_from_name
from pymem.ptypes import RemotePointer
from pymem import Pymem
import time
pymem_csgo = Pymem("csgo.exe")

class Main:
    def GetClientBase():
        clientbase = module_from_name(pymem_csgo.process_handle, 'client.dll')
        return clientbase.lpBaseOfDll
    def GetLocalPlayer():
        localpl = pymem_csgo.read_int(Main.GetClientBase() + 0xDEA98C)
        return localpl
    def GetHealth():
        localplayer = pymem_csgo.read_int(Main.GetClientBase() + 0xDEA98C)
        health_value = pymem_csgo.read_int(localplayer + 0x100)
        return health_value
if __name__ == "__main__":
    print("LOCAL PLAYER ADDR: " + str(hex(Main.GetLocalPlayer())).upper())
    print("HEALTH VALUE: " + str(Main.GetHealth()))
    time.sleep(3)
    exit(665)