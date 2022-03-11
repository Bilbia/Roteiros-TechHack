import socket
import pyfiglet

banner = pyfiglet.figlet_format("Bilb's Port Scanner")
print(banner)

ip = input("Insira um IP para ser escaneado: ")
ports = input("Insira uma range de ports, separando com - e sem utilizar espaços (ex: 0-65535): ")

port1, port2 = ports.split("-")

print("\n Escaneando o IP {0} \n".format(ip))
openPorts = []

try:
    try:
        for port in range(int(port1), int(port2)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if (sock.connect_ex((ip, port)) == 0):
                service = socket.getservbyport(port, "tcp")
                print("A porta {0} está aberta\n".format(port))
                print("Serviço que está rodando na porta {0}: {1}".format(port, service))
                openPorts.append(port)
            else:
                # print("A porta {0} está  fechada".format(port))
                pass
            sock.close()
    except: 
        print(socket.error)

except:
    print("Erro ao conectar no servidor")

print("\nPortas abertas: {0}".format(openPorts))

