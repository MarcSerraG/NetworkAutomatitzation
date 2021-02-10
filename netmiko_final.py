
import getpass

from netmiko import ConnectHandler


def readfile(sFileInput):
    with open(sFileInput, 'r') as fileInput:
        count = 0
        listInput = list()
        for sLine in fileInput:
            sLine = sLine.replace('\n', '').replace('\r', '')
            listInput.append(sLine)
            ++count
        return listInput


def configureSwitch(user, pasw, ip, listCommands, f):
    for x in range(20):
        cm = "vlan "+str(x+10)
        cp = "name vlan_"+str(x+10)
        listCommands.append(cm)
        listCommands.append(cp)

    print("Connecting terminal "+str(ip)+"...")
    iosv_l2 = {  'device_type': 'cisco_ios',  'ip' : ip,  'username' : user,  'password' : pasw, }
    net_connect = ConnectHandler(**iosv_l2)
    print("Configuring terminal "+str(ip)+"...")
    output = net_connect.send_config_set(listCommands)

    f.write("Configuration of "+str(ip)+b"\n")
    f.write(output)
    print("Configuration done "+str(ip)+".")
    print("")

def configureRouter(user, pasw, ip, listCommands, f):

    print("Connecting terminal "+str(ip)+"...")
    iosv_l2 = {  'device_type': 'cisco_ios',  'ip' : ip,  'username' : user,  'password' : pasw, }
    net_connect = ConnectHandler(**iosv_l2)
    print("Configuring terminal "+str(ip)+"...")
    output = net_connect.send_config_set(listCommands)
    f.write("Configuration of "+str(ip)+b"\n")
    f.write(output)
    f.write(b"\n")
    print("Configuration done "+str(ip)+".")
    print("")


def __init__():
    adress = "adreces"
    conf_router = "conf_router"
    conf_switch = "conf_switch"
    run_config = "run_config.txt"

    adressList = list()
    routerList = list()
    switchList = list()

    if adress:
        adressList = readfile(adress)
    if conf_router:
        routerList = readfile(conf_router)
    if conf_switch:
        switchList = readfile(conf_switch)

    user = raw_input("Enter your SSH username: ")
    password = getpass.getpass()
    print("Configuring please wait...")
    f = open(run_config, "wb+")
    for x in range(len(adressList)):
        if x < 2:
                configureRouter(user,password, adressList[x], routerList, f)
        else:
                configureSwitch(user,password, adressList[x], switchList, f)
    f.close()


__init__()
