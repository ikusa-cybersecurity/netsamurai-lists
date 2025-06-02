`update.json` format sample:
```
{
  "base_url": "https://raw.githubusercontent.com/ikusa-cybersecurity/netsamurai-lists/main/",
  "updated": "",  # ISO 8601
  "expires": "",  # ISO 8601
  "lists": [
    {
      "name": "netsamurai-offsets",
      "desc": {
          "en": "Primary NetSamurai list (...)",
          "es": "Lista principal de NetSamurai (...)",
          "ca": "Llista principal de NetSamurai (...)"
      },
      "path": "offsets/offsets.json",
      "format": "custom",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-paywalls",
      "desc": {
          "en": "Supplementary NetSamurai list (...)",
          "es": "Lista suplementaria de NetSamurai (...)",
          "ca": "Llista suplementària de NetSamurai (...)"
      },
      "path": "rules/paywalls.json",
      "format": "custom+regex",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-unbreak",
      "desc": {
          "en": "Supplementary NetSamurai list (...)",
          "es": "Lista suplementaria de NetSamurai (...)",
          "ca": "Llista suplementària de NetSamurai (...)"
      },
      "path": "rules/unbreak.json",
      "format": "custom+regex",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easylist",
      "desc": {
          "en": "Primary filter list (...)",
          "es": "Lista de filtros principal (...)",
          "ca": "Llista de filtres principal (...)"
      },
      "path": "adblock/easylist.txt",
      "format": "adblockplus",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easyprivacy",
      "desc": {
          "en": "Optional supplementary filter list (...)",
          "es": "Lista de filtros suplementaria opcional (...)",
          "ca": "Llista de filtres suplementària opcional (...)",
      }, 
      "path": "adblock/easyprivacy.txt",
      "format": "adblockplus",
      "enabled_default": False,
      "hash": ""  # SHA256
    }
  ]
}
```
