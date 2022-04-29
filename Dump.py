lines (13 sloc)  319 Bytes
import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '32bit':
    from dumpp import menu
    menu()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
