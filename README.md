`update.json` format sample:
```
{
  "base_url": "",
  "updated": "",  # ISO 8601
  "expires": "",  # ISO 8601
  "lists": [
    {
      "name": "netsamurai-offsets",
      "path": "offsets/offsets.json",
      "format": "custom",
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-paywalls",
      "path": "rules/paywalls.json",
      "format": "custom+regex",
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-unbreak",
      "path": "rules/unbreak.json",
      "format": "custom+regex",
      "hash": ""  # SHA256
    },
    {
      "name": "easylist",
      "path": "adblock/easylist.txt",
      "format": "adblockplus",
      "hash": ""  # SHA256
    },
    {
      "name": "easyprivacy",
      "path": "adblock/easyprivacy.txt",
      "format": "adblockplus",
      "hash": ""  # SHA256
    }
  ]
}
```
