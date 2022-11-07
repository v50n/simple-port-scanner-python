import socket
srv_adr = input("the server adresse : ")

print("scanning host : ",srv_adr)
# scan port: default 10000
for i in range(1,10000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_port = s.connect_ex((srv_adr,i))
    if s_port == 0:
        print("port : ",i," is Online")
    else:
        print("port : ",i," is closed")
    s.close()
                
