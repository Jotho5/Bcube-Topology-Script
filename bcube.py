from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def write_output_file(k, n):
    num_servers = pow(k, n)
    num_switches = num_servers + n * (pow(k, n-1) - 1)
    node_names = [f"N{i}" for i in range(num_servers + num_switches)]

    net = Mininet(controller=RemoteController, link=TCLink, switch=OVSSwitch)

    for i in range(num_servers + num_switches):
        if i < num_servers:
            net.addHost(node_names[i])
        else:
            net.addSwitch(node_names[i])

    for i in range(num_servers):
        for j in range(num_servers + num_switches):
            if (i // pow(k, n-1) == j // pow(k, n-1)):
                net.addLink(node_names[i], node_names[j], bw=1)
            else:
                net.addLink(node_names[i], node_names[j], bw=9999)

    net.start()
    CLI(net)
    net.stop()

k = int(input("Enter the value of k: "))
n = int(input("Enter the value of n: "))
write_output_file(k, n)
