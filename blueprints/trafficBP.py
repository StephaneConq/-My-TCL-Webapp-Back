from flask import Blueprint
import requests
from requests.auth import HTTPBasicAuth

from credentials import GRANDLYON_AUTH

traffic_bp = Blueprint('traffic_bp', __name__)


@traffic_bp.route('')
def get_traffic():
    req = requests.get('https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=2.0.0&request=GetFeature&typename=pvo_patrimoine_voirie.pvotrafic&SRSNAME=EPSG:4171&outputFormat=application/json;%20subtype=geojson&startIndex=0',
                       auth=HTTPBasicAuth(GRANDLYON_AUTH['username'], GRANDLYON_AUTH['pass']))
    return req.json()
