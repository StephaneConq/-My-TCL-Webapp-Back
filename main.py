from flask import Flask
from flask_cors import CORS

from blueprints.stopsBP import stops_bp
from blueprints.trafficBP import traffic_bp

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

app.register_blueprint(stops_bp, url_prefix='/api/stops')
app.register_blueprint(traffic_bp, url_prefix='/api/traffic')


if __name__ == '__main__':
    app.run()
