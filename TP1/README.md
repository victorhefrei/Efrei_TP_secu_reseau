# tp_secu_reseau

## Setup topologie

Les deux VPCs sont créés et peuvent se ping entre eux.

```
VPC1 : 10.3.1.1
VPC2 : 10.3.1.2

VPC1$ ping 10.3.1.1
```
### Affichage CAM

Affichage de la table CAM du switch :

```
show mac address-table
```

La table affiche bien la correspondance entre les addresses mac et les ports du switch associés.

### Vlans

pc1 et pc2 sont dans le vlan 10
pc3 est dans le vlan 20

Les pcs 1 et 2 peuvent se ping entre eux mais le pc3 ne peux pas les joindre. Les vlans sont donc fonctionnels.

Commandes utilisées :

```
conf t
interface Ethernet0/0
switchport mode access
switchport access vlan 10

```
Mêmes commandes pour pc2 et pc3 avec un vlan différent pour pc3.

### Creation du serbeur DHCP

Installation de Rocky linux 9 classique.

installation et configuration du DHCP :

```
sudo dnf install dhcp-server -y

```

Contenu de la configuration DHCP :
```
default-lease-time 25920000;
max-lease-time 3888000;
authoritative;
subnet 10.3.1.0 netmask 255.255.255.0 {
    range 10.3.1.100 10.3.1.200;
    option routers 10.3.1.254;
    option subnet-mask 255.255.255.0;
    option domain-name-servers 1.1.1.1
}
```

