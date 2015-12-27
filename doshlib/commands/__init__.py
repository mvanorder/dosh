import doshlib
import pprint
import dateutil.parser as dp

def help(command):
    print "listdroplets"
    print "dropletup <droplet ID>"
    print "dropletdown <droplet ID>"
    print "dropletsnapshots <droplet ID>"

def invalid(command):
    print "Invalid command: " + command

def listdroplets(args):
    result = doshlib.client.droplets.all()
    row = ['ID','Name','Status']
    print("{: >10} {: >40} {: >10}".format(*row))
    for i in result['droplets']:
        row = [i['id'],i['name'],i['status']]
        print("{: >10} {: >40} {: >10}".format(*row))

def rebootdroplet(command):
    print('not implimented yet')

def dropletup(command):
    droplet_id = int(command.split()[1])
    if doshlib.isdroplet(int(droplet_id)):
        status = doshlib.client.droplets.get(droplet_id)['droplet']['status']
        if status == 'off':
            result = doshlib.client.droplets.power_on(droplet_id)
            print result
        else:
            print "Droplet is currently on. Please power it off to run this event."
    else:
        print "Invalid droplet ID:",droplet_id

def dropletdown(command):
    droplet_id = int(command.split()[1])
    if doshlib.isdroplet(int(droplet_id)):
        status = doshlib.client.droplets.get(droplet_id)['droplet']['status']
        if status == 'off':
            print "Droplet is alreday off."
        else:
            result = doshlib.client.droplets.power_off(droplet_id)
            print result
    else:
        print "Invalid droplet ID:",droplet_id

def dropletsnapshots(command):
    droplet_id = int(command.split()[1])
    if doshlib.isdroplet(int(droplet_id)):
        snapshots = doshlib.client.droplets.get_droplet_snapshots(droplet_id)['snapshots']
        row = ['Created at','Disto','ID','Min disk size','Name','Public','Regions']
        print("{: >20} {: >10} {: >10} {: >15} {: >20} {: >10} {: >10}".format(*row))
        for i in snapshots:
            row = [str(dp.parse(i['created_at'])),i['distribution'],i['id'],i['min_disk_size'],i['name'],i['public'],i['regions']]
            print("{: >20} {: >10} {: >10} {: >15} {: >20} {: >10} {: >10}".format(*row))

    else:
        print "Invalid droplet ID:",droplet_id

