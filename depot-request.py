# test request to repo for checking version app
#### THIS FILE IS JUST A TEST FOR A PERSONAL APP ##########


import requests
import json


# [!] possible error by "import circular in main ...""->
from functions import txt, txtError,txtInfo, txtSuccess, getSettings

from constants import FILE_SETTINGS


URL_VERSIONS = getSettings().get('update_url')



def get_online_version():
    """ return online version from github repo """
    if URL_VERSIONS is False:
        txtError(f"Update url is invalid or empty in settings.json. URL : {URL_VERSIONS}")
    try:
        data = requests.get(URL_VERSIONS, timeout=3).json()
        return data
    except Exception as err:
        print(f"Error checking online version ... please try again or contact administrator. ({err})")
        return False

def get_local_version():
    """ return current local version from computeur """
    try:
        with open(FILE_SETTINGS, "r") as local_version: 
            data = json.load(local_version)
            return data
    except Exception as err:
        print(f"Error checking local version ... please try again or contact administrator. ({err})")
        return False

    
online  = get_online_version()
local   = get_local_version()

online_version      = online.get('app_version')
local_version       = local.get('app_version')

# print(local_version, online_version )
# input('...')

def version_to_tuple(version):
    return tuple(map(int, version.split(".")))

def check_versions():
    if not online:
        print("[!] Erreur get_online_version()")
        return
        
    if not local:
        print("[!] Erreur get_local_version()")
        return

    if version_to_tuple(online_version) > version_to_tuple(local_version):
        txtInfo(f"Mise à jour disponible")

        txtError(f"Current: {local_version}")
        txtSuccess(f"Evailable: {online_version}")
    else:
        txtSuccess(f"Application à jour . V {local_version}")

