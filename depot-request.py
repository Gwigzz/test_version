# test request to repo for checking version app

import requests
import json


URL = "https://raw.githubusercontent.com/Gwigzz/test_version/main/version.json"

LOCAL_VERSION = "version_local.json"


def version_to_tuple(version):
    return tuple(map(int, version.split(".")))

def check_online_version():
    """ return online version from github repo """
    try:
        data = requests.get(URL, timeout=3).json()
        return data
    except Exception as err:
        print(f"Error checking online version ... please try again or contact administrator. ({err})")
        return False

def check_local_version():
    """ return current local version from computeur """
    try:
        with open(LOCAL_VERSION, "r") as local_version: 
            data = json.load(local_version)
            return data
    except Exception as err:
        print(f"Error checking local version ... please try again or contact administrator. ({err})")
        return False

    
online = check_online_version()
local = check_local_version()

if not online:
    print("[!] Erreur check_online_version()")
    exit()

if not local:
    print("[!] Erreur check_local_version()")
    exit()

online_version = online["version_app"]
local_version = local["version_app"]

print(f"[*] Online version : {online_version}")
print(f"[*] Local version  : {local_version}")

if version_to_tuple(online_version) > version_to_tuple(local_version):
    print("[+] Mise à jour disponible")
else:
    print("[+] Application à jour")