### TP 2

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
