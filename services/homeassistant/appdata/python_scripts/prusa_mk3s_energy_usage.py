


state_entity_id = data.get("print_state") # printer print state entity
power_entity_id = data.get("power_state") # power sensor entity


state_change_date = hass.states.get(state_entity_id).last_changed

logger.info("state %s", state_change_date)
