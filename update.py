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
            "title": {
                "en": "NetSamurai Offsets",
                "es": "NetSamurai Offsets",
                "ca": "NetSamurai Offsets"
            },
            "desc": {
                "en": "Primary NetSamurai list that indicates the specific fragments of code to be removed in real time to avoid tracking and fingerprinting.",
                "es": "Lista principal de NetSamurai que indica los fragmentos de código específicos que deben eliminarse en tiempo real para evitar el seguimiento y la toma de huellas digitales.",
                "ca": "Llista principal de NetSamurai que indica els fragments de codi específics que s'han d'eliminar en temps real per evitar el seguiment i la presa d'empremtes digitals."
            },
            "path": "offsets/offsets.json",
            "format": "custom",
            "mode": "cleanlist",
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
                "en": "Supplementary NetSamurai list that removes paywalls for some of the most widely used domains in the region.",
                "es": "Lista suplementaria de NetSamurai que elimina los muros de pago para algunos de los dominios más utilizados en la región.",
                "ca": "Llista suplementària de NetSamurai que elimina els murs de pagament per a alguns dels dominis més utilitzats a la regió."
            },
            "path": "rules/paywalls.json",
            "format": "custom+regex",
            "mode": "blocklist",
            "enabled_default": True,
            "hash": ""  # SHA256
        },
        {
            "name": "netsamurai-unbreak",
            "title": {
                "en": "NetSamurai Unbreak",
                "es": "NetSamurai Unbreak",
                "ca": "NetSamurai Unbreak"
            },
            "desc": {
                "en": "Supplementary NetSamurai list that indicates cases in which the resources must not be modified, to avoid breaking functionality. To be removed in newer versions.",
                "es": "Lista suplementaria de NetSamurai que indica los casos en los que los recursos no deben modificarse para evitar romper la funcionalidad. Se eliminará en versiones posteriores.",
                "ca": "Llista suplementària de NetSamurai que indica els casos en què els recursos no s'han de modificar per evitar trencar la funcionalitat. S'eliminarà en versions posteriors."
            },
            "path": "rules/unbreak.json",
            "format": "custom+regex",
            "mode": "allowlist",
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
                "en": "Primary filter list that removes most adverts from international webpages, including unwanted frames, images and objects. The EasyList authors: https://easylist.to/.",
                "es": "Lista de filtros principal que elimina la mayoría de los anuncios de las páginas web internacionales, incluyendo marcos, imágenes y objetos no deseados. Los autores de EasyList: https://easylist.to/.",
                "ca": "Llista de filtres principal que elimina la majoria dels anuncis de les pàgines web internacionals, incloent-hi marcs, imatges i objectes no desitjats. Els autors d'EasyList https://easylist.to/."
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
                "en": "Optional supplementary filter list that completely removes all forms of tracking from the internet, including web bugs, tracking scripts and information collectors. The EasyList authors: https://easylist.to/.",
                "es": "Lista de filtros suplementaria opcional que elimina por completo todas las formas de seguimiento de internet, incluyendo web bugs, scripts de seguimiento y recolectores de información. Los autores de EasyList: https://easylist.to/.",
                "ca": "Llista de filtres suplementària opcional que elimina completament totes les formes de seguiment d'internet, incloent-hi web bugs, scripts de seguiment i recol·lectors d'informació. Els autors d'EasyList: https://easylist.to/.",
            }, 
            "path": "adblock/easyprivacy.txt",
            "format": "adblockplus",
            "mode": "blocklist",
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
