import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import colorama
from azure.identity import ClientSecretCredential
from azure.mgmt.web import WebSiteManagementClient
from colorama import Fore


def local_datetime_chile() -> datetime:
    santiago_timezone = ZoneInfo("America/Santiago")
    return datetime.now().astimezone(santiago_timezone)


colorama.init(autoreset=True)

args = sys.argv

appservice = args[1]
resourcegroup = args[2]

subscription_id = args[3]
client_id = args[4]
tenant = args[5]
secret = args[6]

credentials = ClientSecretCredential(
    client_id=client_id, client_secret=secret, tenant_id=tenant
)
# Restart app service
web_client = WebSiteManagementClient(credentials, subscription_id)
web_client.web_apps.restart(resourcegroup, appservice)

print(
    f"{Fore.GREEN} WebApp {appservice} reiniciada correctamente a las {datetime.strftime(local_datetime_chile(), '%Y-%m-%d %H:%M:%S')}."
)
