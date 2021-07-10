# SuperNetty Home Server (mostly) complete configuration


## Services
- [Proxy](#proxy)
- [WatchTower](#watchtower)
- [UniFi Controller](#unifi-controller)
- [Duplicati](#duplicati)

- [Home Assistant](#home-assistant)
- [ESPHome](#esphome)

- [PLEX](#plex)
- [NordVPN](#media-vpn)
- [Qbittorrent](#qbittorrent)
- [Jackett](#jackett)
- [Radarr](#radarr)
- [Sonarr](#sonarr)
- [Lidarr](#lidarr)
- [Bazarr](#bazarr)

- [Cupsd](#cupsd)
- [Diskspeed](#diskspeed)
- [Mosquitto](#mosquitto)
- [Hammond](#hammond)
- [UnRAID API](#unraid-api)
- [Code Server](#code-server)

---

### [Proxy](https://fleet.linuxserver.io/image?name=linuxserver/swag)
Nginx Reverse Proxy for accesing services from WAN.
Appdata [directory](./services/proxy/appdata) \
Proxy configurations [directory](./services/proxy//proxy-confs)


### [WatchTower](https://containrrr.dev/watchtower)
Automatic updating of containers.


### [UniFi Controller](https://fleet.linuxserver.io/image?name=linuxserver/unifi-controller)
Centralized controller for UniFi devices.
Appdata [directory](./services/unifi-controller/appdata)



### [Home Assistant](https://www.home-assistant.io/)
FOSS Smart Home core system.
Appdata [directory](./services/homeassistant/appdata) \
Using [MariaDB](https://fleet.linuxserver.io/image?name=linuxserver/mariadb) as database



### [ESPHome](https://esphome.io)
Custom Home Assistant aware firmware for Expressif based devices.
Appdata [directory](./services/esphome/appdata)



### [PLEX](https://fleet.linuxserver.io/image?name=linuxserver/unifi-controller)
Entertainment media organiser and player.
Appdata [directory](./services/plex/appdata)



### [Media VPN](https://github.com/bubuntux/nordvpn)
Container providing a VPN networking stack.
Appdata [directory](./services/rathole/appdata)



### [Qbittorrent](https://www.qbittorrent.org)
P2P synchronizing client with webapp.
Appdata [directory](./services/qbittorrent/appdata)



### [Jackett](https://github.com/Jackett/Jackett)
Torrent indexer.
Appdata [directory](./services/jackett/appdata)



### [Radarr](https://radarr.video)
Movie monitoring.
Appdata [directory](./services/radarr/appdata)



### [Sonarr](https://sonarr.tv)
TV-show monitoring.
Appdata [directory](./services/sonarr/appdata)



### [Lidarr](https://lidarr.audio)
Music monitoring.
Appdata [directory](./services/lidarr/appdata)



### [Bazarr](https://www.bazarr.media)
Subtitle monitoring.
Appdata [directory](./services/bazarr/appdata)



### [Duplicati](https://www.duplicati.com)
Backup solution.
Appdata [directory](./services/duplicati/appdata)



### [Cupsd](https://github.com/olbat/dockerfiles/tree/master/cupsd)
Printing server.
Appdata [directory](./services/cupsd/appdata)



### [Diskspeed](https://hub.docker.com/r/jbartlett777/diskspeed)
Disk benchmarking tool with webapp.
Appdata [directory](./services/diskspeed/appdata)



### [Hammond](https://github.com/akhilrex/hammond)
Expense tracking for cars.
Appdata [directory](./services/hammond/appdata)



### [UnRAID API](https://github.com/ElectricBrainUK/UnraidAPI)
Webscraper based MQTT API for UnRAID webapp.
Appdata [directory](./services/unraid-api/appdata)



### [Mosquitto](https://mosquitto.org)
MQTT broker.
Appdata [directory](./services/mosquitto/appdata)



### [Code Server](https://github.com/cdr/code-server)
Web based VSCode for easier remote file editing.
Appdata [directory](./services/code-server/appdata)



TODOs
* [Grocy](https://grocy.info)
* [Rancher](https://rancher.com)
* [SeaFile](https://www.seafile.com/en/home)
* [AdGuard Home](https://adguard.com/da/adguard-home/overview.html)
* [MagicMirror](https://magicmirror.builders)
