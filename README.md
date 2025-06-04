`update.json` format sample:
```
{
  "base_url": "https://raw.githubusercontent.com/ikusa-cybersecurity/netsamurai-lists/main/",
  "updated": "",  # ISO 8601
  "expires": "",  # ISO 8601
  "lists": [
    {
      "name": "netsamurai-unbreak",
      "title": {
        "en": "NetSamurai Unbreak",
        "es": "NetSamurai Unbreak",
        "ca": "NetSamurai Unbreak"
      },
      "desc": {
          "en": "Supplementary NetSamurai list (...)",
          "es": "Lista suplementaria de NetSamurai (...)",
          "ca": "Llista suplementària de NetSamurai (...)"
      },
      "path": "rules/unbreak.json",
      "format": "custom+regex",
      "mode": "allowlist",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-paywalls",
      "title": {
        "en": "NetSamurai Paywalls",
        "es": "NetSamurai Paywalls",
        "ca": "NetSamurai Paywalls"
      },
      "desc": {
          "en": "Supplementary NetSamurai list (...)",
          "es": "Lista suplementaria de NetSamurai (...)",
          "ca": "Llista suplementària de NetSamurai (...)"
      },
      "path": "rules/paywalls.json",
      "format": "custom+regex",
      "mode": "blocklist",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easylist",
      "title": {
        "en": "EasyList",
        "es": "EasyList",
        "ca": "EasyList"
      },
      "desc": {
          "en": "Primary filter list (...)",
          "es": "Lista de filtros principal (...)",
          "ca": "Llista de filtres principal (...)"
      },
      "path": "adblock/easylist.txt",
      "format": "adblockplus",
      "mode": "blocklist",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easyprivacy",
      "title": {
        "en": "EasyPrivacy",
        "es": "EasyPrivacy",
        "ca": "EasyPrivacy"
      },
      "desc": {
          "en": "Optional supplementary filter list (...)",
          "es": "Lista de filtros suplementaria opcional (...)",
          "ca": "Llista de filtres suplementària opcional (...)",
      }, 
      "path": "adblock/easyprivacy.txt",
      "format": "adblockplus",
      "mode": "blocklist",
      "enabled_default": False,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-offsets",
      "title": {
        "en": "NetSamurai Offsets",
        "es": "NetSamurai Offsets",
        "ca": "NetSamurai Offsets"
      },
      "desc": {
          "en": "Primary NetSamurai list (...)",
          "es": "Lista principal de NetSamurai (...)",
          "ca": "Llista principal de NetSamurai (...)"
      },
      "path": "offsets/offsets.json",
      "format": "custom",
      "mode": "cleanlist",
      "enabled_default": True,
      "hash": ""  # SHA256
    }
  ]
}
```
