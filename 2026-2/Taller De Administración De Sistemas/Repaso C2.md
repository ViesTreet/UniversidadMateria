## ens18 sin ip 
![[Pasted image 20261119171343.png]]
Para solucionar esto primero dejamos la configuración personalizada del netplan como .bak temporalmente, luego activamos el puerto 67 y 68 desde el UFW
```
sudo ufw allow 67
sudo ufw allow 68
sudo ufw allow 80
sudo ufw allow 443
tas@tas-c2-2025:/etc/apache2$ sudo ufw allow 80/tcp  
Rule added  
Rule added (v6)  
tas@tas-c2-2025:/etc/apache2$ sudo ufw allow 433/tcp
sudo ufw allow ssh
sudo ufw status
```
Luego de eso hacemos un netplan try 
```
sudo netplan try
```
tambien si no funciona podemos correr los siguientes comandos:
```
sudo networkctl renew ens18
sudo systemctl restart systemd-networkd
```
y restablecemos la config default:
```
tas@tas-c2-2025:~$ sudo mv /etc/netplan/00-tas2026-nameserver.yaml.bak /etc/netplan/00-tas2026-nameserver.yaml  
tas@tas-c2-2025:~$ cat /etc/netplan/00-tas2026-nameserver.yaml    
network:  
   version: 2  
   ethernets:  
       ens18:                                                                  # Private network interface  
           nameservers:  
               addresses:  
               - 10.33.195.191  
#                - 10.33.192.131                                # Private IP for ns1  
               search: [ tas2025.local, cs.ilab.cl ]   # DNS zone  
tas@tas-c2-2025:~$ ip a  
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000  
   link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00  
   inet 127.0.0.1/8 scope host lo  
      valid_lft forever preferred_lft forever  
   inet6 ::1/128 scope host    
      valid_lft forever preferred_lft forever  
2: ens18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000  
   link/ether bc:24:11:61:8a:b1 brd ff:ff:ff:ff:ff:ff  
   altname enp0s18  
   inet 10.33.195.188/25 metric 100 brd 10.33.195.255 scope global dynamic ens18  
      valid_lft 6436sec preferred_lft 6436sec  
   inet6 fe80::be24:11ff:fe61:8ab1/64 scope link    
      valid_lft forever preferred_lft forever  
tas@tas-c2-2025:~$ sudo nano /etc/netplan/00-tas2026-nameserver.yaml    
tas@tas-c2-2025:~$ sudo netplan try
```
## Vista general
La pagina al entrar por ip no carga, pero al hacer cURL desde la mv este carga, primero vamos a ver los servicios activos
```
tas@tas-c2-2025:~$ sudo systemctl list-units --type=service --all --no-page
tas@tas-c2-2025:~$ sudo systemctl list-unit-files --type=service --state=disabled  
UNIT FILE                              STATE    VENDOR PRESET  
apache-htcacheclean.service            disabled enabled         
apache-htcacheclean@.service           disabled enabled         
apache2@.service                       disabled enabled         
console-getty.service                  disabled disabled        
debug-shell.service                    disabled disabled        
iscsid.service                         disabled enabled         
mariadb.service                        disabled enabled         
mariadb@.service                       disabled enabled         
named-resolvconf.service               disabled enabled         
named.service                          disabled enabled         
nftables.service                       disabled enabled         
rsync.service                          disabled enabled         
serial-getty@.service                  disabled enabled         
systemd-boot-check-no-failures.service disabled disabled        
systemd-network-generator.service      disabled enabled         
systemd-sysext.service                 disabled enabled         
systemd-time-wait-sync.service         disabled disabled        
upower.service                         disabled enabled         
  
18 unit files listed.
```
Tenemos mariadb, named y apache apagado, por lo que vamos a activarlos, luego de activarlos sigue sin cargar la página.
Nuestro primer objetivo es ver la página 
Primero nos fijamos que los puertos de apache2 están mal configurados, lo cambiamos y tambien apagamos nginx para evitar conflictos
```
tas@tas-c2-2025:/etc/apache2$ cat ports.conf    
# If you just change the port or add more ports here, you will likely also  
# have to change the VirtualHost statement in  
# /etc/apache2/sites-enabled/000-default.conf  
  
Listen 8080  
  
<IfModule ssl_module>  
       Listen 8443  
</IfModule>  
  
<IfModule mod_gnutls.c>  
       Listen 8443  
</IfModule>  
  
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet  
tas@tas-c2-2025:/etc/apache2$ sudo nano ports.conf    
tas@tas-c2-2025:/etc/apache2$ cat ports.conf    
# If you just change the port or add more ports here, you will likely also  
# have to change the VirtualHost statement in  
# /etc/apache2/sites-enabled/000-default.conf  
  
Listen 80  
  
<IfModule ssl_module>  
       Listen 443  
</IfModule>  
  
<IfModule mod_gnutls.c>  
       Listen 443  
</IfModule>  
  
# vim: syntax=apache ts=4 sw=4 sts=4 sr noet  
tas@tas-c2-2025:/etc/apache2$ sudo systemctl stop nginx  
tas@tas-c2-2025:/etc/apache2$ sudo systemctl disable nginx  
Synchronizing state of nginx.service with SysV service script with /lib/systemd/systemd-sysv-install.  
Executing: /lib/systemd/systemd-sysv-install disable nginx  
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.  
tas@tas-c2-2025:/etc/apache2$ sudo systemctl restart apache2
```
revisamos y era un error del ufw que corregimos y listo 
```
tas@tas-c2-2025:/etc/apache2$ sudo ufw allow 80/tcp  
Rule added  
Rule added (v6)  
tas@tas-c2-2025:/etc/apache2$ sudo ufw allow 433/tcp
```

![[Pasted image 20261119174806.png]]
## DNS
primero revisamos la dns que vamos a consultar, sera:
```
tas@tas-c2-2025:/etc/bind$ cat named.conf.local    
//  
// Do any local configuration here  
//  
  
// Consider adding the 1918 zones here, if they are not used in your  
// organization  
//include "/etc/bind/zones.rfc1918";  
  
  
zone "tas2025.local" {  
   type master;  
   file "/etc/bind/zones/db.tas2026-.local"; # zone file path  
};  
tas@tas-c2-2025:/etc/bind$
```
no responde, entonces arreglamos 
```
tas@tas-c2-2025:/etc/bind$ dig @127.0.0.1 tas2025.local  
  
; <<>> DiG 9.18.39-0ubuntu0.22.04.8-Ubuntu <<>> @127.0.0.1 tas2025.local  
; (1 server found)  
;; global options: +cmd  
;; Got answer:  
;; WARNING: .local is reserved for Multicast DNS  
;; You are currently testing what happens when an mDNS query is leaked to DNS  
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 35673  
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1  
  
;; OPT PSEUDOSECTION:  
; EDNS: version: 0, flags:; udp: 1232  
; COOKIE: 69d40029c6d9695e010000006aff614cd2c251ae1634696a (good)  
;; QUESTION SECTION:  
;tas2025.local.                 IN      A  
  
;; Query time: 4 msec  
;; SERVER: 127.0.0.1#53(127.0.0.1) (UDP)  
;; WHEN: Thu Nov 19 20:51:24 UTC 2026  
;; MSG SIZE  rcvd: 70  
  
tas@tas-c2-2025:/etc/bind$
```
primero arreglamos el conf options:
```
tas@tas-c2-2025:/etc/bind$ cat named.conf.options    
options {  
       directory "/var/cache/bind";  
  
  
       recursion yes;                 # enables resursive queries  
       allow-recursion { any; };  # allows recursive queries from "trusted" clients  
       listen-on { any; };   # ns1 private IP address - listen on private network only  
       allow-transfer { none; };      # disable zone transfers by default  
  
       forwarders {  
         10.33.195.188;  
         8.8.8.8;         
       };  
  
       //========================================================================  
       // If BIND logs error messages about the root key being expired,  
       // you will need to update your keys.  See https://www.isc.org/bind-keys  
       //========================================================================  
       dnssec-validation auto;  
  
       listen-on-v6 { any; };  
};  
tas@tas-c2-2025:/etc/bind$ ^C  
tas@tas-c2-2025:/etc/bind$
```
corregimos el nombre de la zona:
```
  
tas@tas-c2-2025:/etc/bind$ ls zones  
db.tas2026.local  
tas@tas-c2-2025:/etc/bind$ cat named.conf.local    
//  
// Do any local configuration here  
//  
  
// Consider adding the 1918 zones here, if they are not used in your  
// organization  
//include "/etc/bind/zones.rfc1918";  
  
  
zone "tas2025.local" {  
   type master;  
   file "/etc/bind/zones/db.tas2026-.local"; # zone file path  
};  
tas@tas-c2-2025:/etc/bind$ ^C  
tas@tas-c2-2025:/etc/bind$
```
corregimos la zona, especificamente 2026 a 2025, la ip y el serial:
```
cat zones/db.tas2026.local    
;  
; BIND data file for local loopback interface  
;  
$TTL    604800  
@       IN      SOA     tas2026.local. admin.tas2026.local. (  
                             4         ; Serial  
                        604800         ; Refresh  
                         86400         ; Retry  
                       2419200         ; Expire  
                        604800 )       ; Negative Cache TTL  
;  
  
; name servers - NS records  
   IN      NS      ns1.tas2026.local.  
  
ns1.tas2026.local.          IN      A       10.33.195.196  
@       IN      A       10.33.195.196  
  
tas@tas-c2-2025:/etc/bind$ sudo nano zones/db.tas2026.local    
tas@tas-c2-2025:/etc/bind$ cat zones/db.tas2026.local    
$TTL    604800  
@       IN      SOA     tas2025.local. admin.tas2025.local. (  
                        2026111902     ; Serial  
                        604800         ; Refresh  
                         86400         ; Retry  
                       2419200         ; Expire  
                        604800 )       ; Negative Cache TTL  
;  
       IN      NS      ns1.tas2025.local.  
  
ns1.tas2025.local.  IN      A       10.33.195.188  
@                   IN      A       10.33.195.188  
www                 IN      A       10.33.195.188  
tas@tas-c2-2025:/etc/bind$
tas@tas-c2-2025:/etc/bind$ sudo rndc reload
```
ahora al hacer un dig nos muestra la ip:
```
tas@tas-c2-2025:/etc/bind$ dig @127.0.0.1 tas2025.local  
  
; <<>> DiG 9.18.39-0ubuntu0.22.04.8-Ubuntu <<>> @127.0.0.1 tas2025.local  
; (1 server found)  
;; global options: +cmd  
;; Got answer:  
;; WARNING: .local is reserved for Multicast DNS  
;; You are currently testing what happens when an mDNS query is leaked to DNS  
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16573  
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1  
  
;; OPT PSEUDOSECTION:  
; EDNS: version: 0, flags:; udp: 1232  
; COOKIE: f234f8f14c080d5c010000006aff632a301ee7e1ee581302 (good)  
;; QUESTION SECTION:  
;tas2025.local.                 IN      A  
  
;; ANSWER SECTION:  
tas2025.local.          604800  IN      A       10.33.195.188  
  
;; Query time: 0 msec  
;; SERVER: 127.0.0.1#53(127.0.0.1) (UDP)  
;; WHEN: Thu Nov 19 20:59:22 UTC 2026  
;; MSG SIZE  rcvd: 86
```
Ademas activamos el puerto 53 en ufw:
```
sudo ufw allow 53
```
Desde mi PC devuelve la pagina usando:
```
curl -H "Host: tas2025.local" http://10.33.195.188/
```
## Wordpress
tenemos que activar primero la pagina:
```
tas@tas-c2-2025:/etc/apache2$ ls sites-available/  
000-default.conf  default-ssl.conf  wp-tas2025.conf  
tas@tas-c2-2025:/etc/apache2$ ls sites-enabled/  
tas@tas-c2-2025:/etc/apache2$ ^C  
tas@tas-c2-2025:/etc/apache2$
```
```
tas@tas-c2-2025:/etc/apache2$ ls  
apache2.conf  conf-available  conf-enabled  envvars  magic  mods-available  mods-enabled  ports.conf  sites-available  sites-enabled  
tas@tas-c2-2025:/etc/apache2$ ls sites-available/  
000-default.conf  default-ssl.conf  wp-tas2025.conf  
tas@tas-c2-2025:/etc/apache2$ ls sites-enabled/  
tas@tas-c2-2025:/etc/apache2$ ^C  
tas@tas-c2-2025:/etc/apache2$ sudo a2ensite wp-tas2025.conf  
[sudo] password for tas:    
Enabling site wp-tas2025.  
To activate the new configuration, you need to run:  
 systemctl reload apache2  
tas@tas-c2-2025:/etc/apache2$ systemctl reload apache2  
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===  
Authentication is required to reload 'apache2.service'.  
Authenticating as: tas  
Password:    
==== AUTHENTICATION COMPLETE ===  
tas@tas-c2-2025:/etc/apache2$ cat sites-enabled/wp-tas2025.conf    
<VirtualHost *:80>  
       ServerName www.tas2025.local  
  
       ServerAdmin webmaster@localhost  
       DocumentRoot /sitios/wp-tas2025  
  
        <Directory /sitios/wp-tas2025>  
               Options FollowSymLinks  
               AllowOverride All  
               Require all granted  
       </Directory>  
  
       ErrorLog ${APACHE_LOG_DIR}/error.log  
       CustomLog ${APACHE_LOG_DIR}/access.log combined  
  
</VirtualHost>
```
tambien vemos que no tenemos acceso a la carpeta del wordpress:
```
  
tas@tas-c2-2025:/etc/apache2$ cd /sitios/wp-tas2025/  
-bash: cd: /sitios/wp-tas2025/: Permission denied  
tas@tas-c2-2025:/etc/apache2$
```
cambiamos los permisos:
```
root@tas-c2-2025:/sitios/wp-tas2025# chown -R www-data:www-data /sitios/wp-tas2025  
root@tas-c2-2025:/sitios/wp-tas2025# find /sitios/wp-tas2025 -type d -exec chmod 755 {} +  
root@tas-c2-2025:/sitios/wp-tas2025# find /sitios/wp-tas2025 -type f -exec chmod 644 {} +  
root@tas-c2-2025:/sitios/wp-tas2025#
```
## MariaDB
![[Pasted image 20261119184933.png]]ahora vemos que settings tiene wordpress sobre mariadb
```
tas@tas-c2-2025:/sitios/wp-tas2025$ cat wp-config.php |grep "DB"  
define( 'DB_NAME', ' wp_db' );  
define( 'DB_USER', 'wp_user' );  
define( 'DB_PASSWORD', 'password' );  
define( 'DB_HOST', 'localhost' );  
define( 'DB_CHARSET', 'utf8' );  
define( 'DB_COLLATE', '' );  
tas@tas-c2-2025:/sitios/wp-tas2025$
```
vemos que la db seleccionada no tiene nada, entonces la cambiamos y **le borramos el espacio**.
ahora modificamos al usuarios en la db:
```
4 rows in set (0.005 sec)  
  
MariaDB [mysql]> select host,user from user;  
+-----------+-------------+  
| Host      | User        |  
+-----------+-------------+  
| %         | wp_user     |  
| localhost | mariadb.sys |  
| localhost | mysql       |  
| localhost | root        |  
+-----------+-------------+  
4 rows in set (0.003 sec)  
  
MariaDB [mysql]> RENAME USER 'wp_user'@'%' TO 'wp_user'@'localhost';  
Query OK, 0 rows affected (0.010 sec)  
  
MariaDB [mysql]> select host,user from user;  
+-----------+-------------+  
| Host      | User        |  
+-----------+-------------+  
| localhost | mariadb.sys |  
| localhost | mysql       |  
| localhost | root        |  
| localhost | wp_user     |  
+-----------+-------------+  
4 rows in set (0.002 sec)  
  
MariaDB [mysql]> ALTER USER wp_user@localhost IDENTIFIED BY PASSWORD 'password';  
ERROR 1396 (HY000): Operation ALTER USER failed for 'wp_user'@'localhost'  
MariaDB [mysql]> FLUSH PRIVILEGES;  
Query OK, 0 rows affected (0.002 sec)  
  
MariaDB [mysql]> ALTER USER wp_user@localhost IDENTIFIED BY PASSWORD 'password';  
ERROR 1396 (HY000): Operation ALTER USER failed for 'wp_user'@'localhost'  
MariaDB [mysql]> ALTER USER 'wp_user'@'localhost' IDENTIFIED BY 'password';  
Query OK, 0 rows affected (0.002 sec)  
  
MariaDB [mysql]> FLUSH PRIVILEGES;  
Query OK, 0 rows affected (0.002 sec)  
  
MariaDB [mysql]> SHOW GRANTS FOR 'wp_user'@'localhost';  
+-------------------------------------------------------------------------------------------------------------  
---+  
| Grants for wp_user@localhost                                                                                  
  |  
+-------------------------------------------------------------------------------------------------------------  
---+  
| GRANT USAGE ON *.* TO `wp_user`@`localhost` IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E1  
9' |  
| GRANT ALL PRIVILEGES ON `wp_db`.* TO `wp_user`@`localhost`                                                    
  |  
| GRANT ALL PRIVILEGES ON `wordpress_db`.* TO `wp_user`@`localhost`                                             
  |  
+-------------------------------------------------------------------------------------------------------------  
---+  
3 rows in set (0.000 sec)  
  
MariaDB [mysql]>
```
## Ultimo error con bind
![[Pasted image 20261119191918.png]]
para eso tenemos que cambiar el resolver de la vm con el siguiente comando
```
tas@tas-c2-2025:/etc/bind$ sudo resolvectl dns ens18 10.33.195.188 && sudo resolvectl domain ens18 'tas2025.lo  
cal' && sudo resolvectl flush-caches  
tas@tas-c2-2025:/etc/bind$
```
En este caso solo era un erro en el netplan con un espacio en los namerservers, podemos hacerlo directmante desde el archivo 
```
sudo nano /etc/resolv.conf
```
```
nameserver 10.33.195.188
search tas2025.local cs.ilab.usm.cl
```
```
sudo systemctl restart systemd-resolved
```
![[Pasted image 20261119192854.png]]