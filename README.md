`update.json` format sample:
```
{
  "base_url": "https://raw.githubusercontent.com/ikusa-cybersecurity/netsamurai-lists/main/",
  "updated": "",  # ISO 8601
  "expires": "",  # ISO 8601
  "lists": [
    {
      "name": "netsamurai-offsets",
      "desc": "Primary NetSamurai list that indicates the specific fragments of code to be removed in real time to avoid tracking and fingerprinting.",
      "path": "offsets/offsets.json",
      "format": "custom",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-paywalls",
      "desc": "Supplementary NetSamurai list that removes paywalls for some of the most widely used domains in the region.",
      "path": "rules/paywalls.json",
      "format": "custom+regex",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "netsamurai-unbreak",
      "desc": "Supplementary NetSamurai list that indicates cases in which the resources must not be modified, to avoid breaking functionality. To be removed in newer versions.",
      "path": "rules/unbreak.json",
      "format": "custom+regex",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easylist",
      "desc": "Primary filter list that removes most adverts from international webpages, including unwanted frames, images and objects. The EasyList authors (https://easylist.to/).",
      "path": "adblock/easylist.txt",
      "format": "adblockplus",
      "enabled_default": True,
      "hash": ""  # SHA256
    },
    {
      "name": "easyprivacy",
      "desc": "Optional supplementary filter list that completely removes all forms of tracking from the internet, including web bugs, tracking scripts and information collectors. The EasyList authors (https://easylist.to/).",
      "path": "adblock/easyprivacy.txt",
      "format": "adblockplus",
      "enabled_default": False,
      "hash": ""  # SHA256
    }
  ]
}
```
