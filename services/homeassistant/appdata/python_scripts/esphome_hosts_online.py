
hosts = data.get('hosts')

# Get suffixes for all sensors
restart_sw_suffix = data.get('restart_sw_suffix', 'restart')
status_suffix 	  = data.get('status_suffix'	, 'status')
version_suffix	  = data.get('version_suffix'	, 'esphome_version')
uptime_suffix 	  = data.get('uptime_suffix'	, 'uptime')
bssid_suffix 	  = data.get('bssid_suffix'	, 'connected_bssid')
ssid_suffix 	  = data.get('ssid_suffix'	, 'connected_ssid')
ip_addr_suffix    = data.get('ip_addr_suffix'	, 'ip_address')
wifi_rssi_suffix  = data.get('wifi_rssi_suffix' , 'wifi_rssi')


# Variables
#hostnames = list(map(lambda each:each.partition('.')[0], hosts))
hosts_total = len(hosts)
hosts_online = 0
hosts_offline = hosts_total
online_list = []
offline_list = []

## Populate sensors for each node
for host in hosts:

  hostname = host.partition('.')[0]

  friendly_name = (hass.states.get( f'binary_sensor.{hostname}_{status_suffix}' )).name[:-len(' Status')]
  status    	= (hass.states.get( f'binary_sensor.{hostname}_{status_suffix}' )).state
  restart_sw	= (hass.states.get( f'switch.{hostname}_{restart_sw_suffix}' )).state
  version   	= (hass.states.get( f'sensor.{hostname}_{version_suffix}' )).state
  uptime    	= (hass.states.get( f'sensor.{hostname}_{uptime_suffix}' )).state
  bssid     	= (hass.states.get( f'sensor.{hostname}_{bssid_suffix}' )).state
  ssid      	= (hass.states.get( f'sensor.{hostname}_{ssid_suffix}' )).state
  ip_addr   	= (hass.states.get( f'sensor.{hostname}_{ip_addr_suffix}' )).state
  wifi_rssi 	= (hass.states.get( f'sensor.{hostname}_{wifi_rssi_suffix}' )).state
  version_short = version.split(' ')[0]

  hass.states.set( f'switch.{hostname}_esphome_node', restart_sw, {
    'friendly_name':		friendly_name,
    status_suffix:		status,
    version_suffix: 		version,
    f'{version_suffix}_short': 	version_short,
    uptime_suffix: 		uptime,
    bssid_suffix: 		bssid,
    ssid_suffix: 		ssid,
    ip_addr_suffix: 		ip_addr,
    wifi_rssi_suffix: 		wifi_rssi,
    'host':			host
  })


  if status == 'on':
    hosts_online = hosts_online + 1
    hosts_offline = hosts_offline - 1
    online_list.append(host)
  else:
    offline_list.append(host)


# General network data sensors
hass.states.set('sensor.esphome_nodes', hosts_total, {
  'friendly_name':	'ESPHome Nodes',
  'nodes_online': 	hosts_online,
  'nodes_offline': 	hosts_offline,
  'online_list':	online_list
})
