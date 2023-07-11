from os import system as x
server = (input("IP >>"))
packet = int(input("Ping Count > "))
x(("ping {s} -c {p}").format(s=server, p=packet))
