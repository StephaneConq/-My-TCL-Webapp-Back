from flask import Blueprint, request
import json
import requests
from requests.auth import HTTPBasicAuth

from credentials import GRANDLYON_AUTH

stops_bp = Blueprint('stops_bp', __name__)


@stops_bp.route('')
def get_stops():
    data = None
    with open('geojson/tcl_sytral.tclarret.json') as json_file:
        data = json.load(json_file)
    return data


@stops_bp.route('/passages/<stop_id>')
def get_passages(stop_id):
    res = requests.get('https://download.data.grandlyon.com/ws/rdata/tcl_sytral.tclpassagearret/all.json?maxfeatures=999999999&start=1&field=id&value={}'.format(stop_id),
                       auth=HTTPBasicAuth(GRANDLYON_AUTH['username'], GRANDLYON_AUTH['pass']))
    return {'passages': res.json().get('values', [])}
