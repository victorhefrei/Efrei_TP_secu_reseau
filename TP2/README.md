# TP 2
## Mise en place
Une fois connecté au NAT de GNS3, mon routeur peut joindre internet et je peux ping l'adresse 1.1.1.1
J'ai également paramétré le nat entre l'interface du LAN et celle du WAN.

Configuration des interfaces du routeur (show run sur le routeur) :

```
inteface FastEthernet0/0
  ip address dhcp
  ip nat outside
  ip virtual-reassembly
  duplex half

interface Ethernet1/0
  ip address 10.2.1.254 255.255.255.0
  ip nat inside
  ip virtual-reassembly
  duplex half
```
L'interface FE0/0 correspond à mon interface WAN.
L'interface FE1/0 correspond à mon interface LAN.

Une fois le serveur DHCP remis en place (même configuration que dans le TP1 en y ajoutant l'adresse de l'interface LAN du routeur comme passerelle), les machine du réseau ont pu obtenir une adresse IP en DHCP et peuvent maintenant se ping entre elles, ainsi qu'avec l'extérieur.

## Attaques

### DHCP Spoofing

Pour mettre en place le DHCP Spoofing, j'ai créé un serveur DHCP dnsmasq sur ma machine attaquante.
Ce serveur délivre des adresses sur la plage 10.2.1.225 à 10.2.1.235
Ce serveur à répondu avant le serveur DHCP Légitime au pc qui à fais une demande d'IP.

### DHCP Starvation

Pour mettre en place le DHCP Starvation, j'ai utilisé un script qui fais des requêtes DHCP en boucle avec une adresse MAC différente à chaque fois.
Les requêtes ont été traitées par le serveur DHCP qui à assigné des adresses IP à toutes les "machines" (les différentes adresses mac simulant des machines) ayant demandé une IP, et à ainsi rempli son fichier de leases, bloquant toute nouvelle demande d'adresse IP car il n'y avait plus d'adresses disponibles.

### ARP Poisoning

Pour l'attaque d'ARP Poisoning, je créé une réponse ARP que j'envoie à l'ip donnée en paramètres du script.
Je lui donne l'information que sa propre adresse IP est associée à une adresse MAC factice.




## Remédiations

### DHCP Spoofing
Pour empêcher d'avoir du DHCP Spoofing sur notre réseau, il faut activer le DHCP Snooping sur les switches du réseau pour autoriser uniquement les serveurs DHCP légitimes (whitelistés) à agir sur le réseau.

### DHCP Starvation
On peut activer la limitiation du taux de requêtes pour éviter les attaques de starvation. Il est également possible de désactiver simplement la possiblité à une machine de demander plusieurs adresses IP pour la même adresse MAC.

### ARP Poisoning
On peut configurer des entrées ARP statiques sur les appareils critiques, ou utiliser la fonctionnalité "DAI" - Dynamic ARP Inspection - sur les switches, qui vérifie la validité des paquets ARP sur le réseau.
