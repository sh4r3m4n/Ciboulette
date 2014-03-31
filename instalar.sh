#/usr/bin/env sh
#
#	Instalación tipica de ciboulette
#

# Crea el directorio
CIBOULETTE="ciboulette"
mkdir -p ~/.$CIBOULETTE/md

# Instala dependencias
sudo aptitude install tor mini-httpd chronicle liferea

# Anuncia el servicio en Tor
echo "HiddenServiceDir /var/lib/tor/$CIBOULETTE/
HiddenServicePort 80 127.0.0.1:4232" > /etc/tor/torrc

# Reinicia el Tor
sudo /etc/init.d/tor restart

# Nombre en Tor
sudo cat /var/lib/tor/$CIBOULETTE/hostname > ~/.$CIBOULETTE/hostname
