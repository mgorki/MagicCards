import serial, serial.tools.list_ports

ports = list(serial.tools.list_ports.comports(include_links=False))
for port in ports:
    print(port.description)
