
def client_key_send(a, g, p):
    A = g**a % p
    return A

def server_key_send_receive(b, g, p, A):
    B = g**b % p
    K_b = A**b % p  # Ключ сервер
    print(K_b)
    return B

def client_receive(B, a, p):
    K_a = B**a % p  # Ключ клиент
    print(K_a)

#  client_key_send() ---> server_key_send_receive() ---> client_receive()

a = 10
b = 3478
g = 634
p = 6589

client_receive(server_key_send_receive(b, g, p, client_key_send(a, g, p)), a, p)