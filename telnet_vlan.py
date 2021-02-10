import getpass
import telnetlib


def stonf():
    host = raw_input("Enter the Host ip address: ")
    user = raw_input("Enter your Telnet username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(host)
    print("Connection Stablished...")
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    print("Starting configuration...")
    tn.write(b"enable\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    for x in range(3):
        print("Configurating...")
        tn.write(b"vlan database\n")
        tn.write(b"vlan " + str(x + 2) + b"\n")
        tn.write(b"exit\n")

        tn.write(b"conf t\n")

        tn.write(b"int vlan" + str(x + 2) + b"\n")
        tn.write(b"ip address " + str(x + 2) + b"0.0.0.1 255.255.0.0\n")
        tn.write(b"no shutdown\n")

        tn.write(b"end\n")

    tn.write(b"wr\n")
    tn.write(b"exit\n")
    #Uncomment to see output
    #print(tn.read_all().decode('ascii'))


def __init__():
    try:
        print("Started configuration...")
        stonf()
        print("End configuration...")
    except:
        print("Something went wrong...")


__init__()
