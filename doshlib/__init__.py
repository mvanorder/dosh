from digitalocean import ClientV2
from . import commands
import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(['dosh.cfg', os.path.expanduser('~/.dosh.cfg')])

token = config.get("digitalocean", "token")

client = ClientV2(token=token)

def isdroplet(droplet_id):
    for i in client.droplets.all()['droplets']:
        if i['id'] == droplet_id:
            return True
    return False

