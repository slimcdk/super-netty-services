
md_prefix = "home_server_docker"

container_names = [ entity_id.split('.')[1] for entity_id in hass.states.entity_ids('switch') if entity_id.split('.')[1].startswith(md_prefix) ]


for container_name in container_names:

  switch = hass.states.get(f'switch.{container_name}')
  hass.states.set(switch.entity_id, switch.state, {
    'friendly_name': container_name.replace(f'{md_prefix}_', ''),
    'container_name': container_name.replace(f'{md_prefix}_', ''),
    '1cpu': hass.states.get(f'sensor.{container_name}_1cpu').state,
    'cpu': hass.states.get(f'sensor.{container_name}_cpu').state,
    'image': hass.states.get(f'sensor.{container_name}_image').state,
    'memory': hass.states.get(f'sensor.{container_name}_memory').state,
    'memory_percent': hass.states.get(f'sensor.{container_name}_memory_percent').state,
    'state': hass.states.get(f'sensor.{container_name}_state').state,
    'status': hass.states.get(f'sensor.{container_name}_status').state,
    'up_time': hass.states.get(f'sensor.{container_name}_up_time').state,
    'network_speed_down': hass.states.get(f'sensor.{container_name}_network_speed_down').state,
    'network_speed_up': hass.states.get(f'sensor.{container_name}_network_speed_up').state,
    'network_total_down': hass.states.get(f'sensor.{container_name}_network_total_down').state,
    'network_total_up': hass.states.get(f'sensor.{container_name}_network_total_up').state
  })

  ''' not working as homeassistant_db matches homeassistant = not good'''
  ''' 
  container_sensors = [entity_id for entity_id in hass.states.entity_ids('sensor') if entity_id.split('.')[1].startswith(container_name) ]
  '''