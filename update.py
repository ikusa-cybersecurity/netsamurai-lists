import json
import hashlib

from typing import Tuple
from datetime import datetime, timezone, timedelta

EXPIRATION_HOURS = 120  # 24h * 5days
OUPUT_FILE = "update.json"

file_template = {
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


def get_iso8601_timestamps(expiration_h: int) -> Tuple[str, str]:
    '''
    Return 'updated' and 'expires' timestamps in ISO 8601 format.
    '''
    current_time_utc = datetime.now(timezone.utc)
    updated_str = current_time_utc.isoformat(timespec='seconds').replace('+00:00', 'Z')
    expires_time_utc = current_time_utc + timedelta(hours=expiration_h)
    expires_str = expires_time_utc.isoformat(timespec='seconds').replace('+00:00', 'Z')
    return updated_str, expires_str


def get_list_hash(file_path: str) -> str:
    '''
    Returns the sha56 hash of the list located in file_path.
    '''
    data_bytes = None
    with open(file_path, 'rb') as file:
        data_bytes = file.read()
    return hashlib.sha256(data_bytes).hexdigest()


def get_updated_template() -> str:
    '''
    Returns json dumps of template filled with updated hashes and timestamps.
    '''
    updated_template = file_template.copy()

    for list in updated_template["lists"]:
        list["hash"] = get_list_hash(list["path"])

    updated, expires = get_iso8601_timestamps(EXPIRATION_HOURS)
    updated_template["updated"] = updated
    updated_template["expires"] = expires

    return updated_template


def main():
    updated_template = get_updated_template()
    updated_content_str = json.dumps(updated_template, indent=2)
    print(updated_content_str)
    with open(OUPUT_FILE, 'w') as file:
        file.write(updated_content_str)


if __name__ == "__main__":
    main()
