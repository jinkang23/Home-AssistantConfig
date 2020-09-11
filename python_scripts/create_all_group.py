# pylint: disable=C0103,C0114
domain = data.get('domain', '')
group = data.get('group', '')

if not isinstance(domain, str) or not isinstance(group, str) or not domain or not group:
    logger.warning("bad domain or group! Not executing.")
else:
    service_data = {"object_id": group, "entities": hass.states.entity_ids(domain)}
    hass.services.call("group", "set", service_data, False)
