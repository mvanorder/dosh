import doshlib
import pprint

def help(command):
    print "listdroplets"
    print "dropletup <droplet ID>"
    print "dropletdown <droplet ID>"

def invalid(command):
    print "Invalid command: " + command

def listdroplets(args):
    print('Droplets: ')
    result = doshlib.client.droplets.all()
    for i in result['droplets']:
        print i['id'],i['name'],i['status']

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
