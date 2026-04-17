import socket

HOST = '127.0.0.1' # change this later to the actual host, only use locally
PORT = 65432

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept() # Wait for a connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # Receive up to 1024 bytes
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
