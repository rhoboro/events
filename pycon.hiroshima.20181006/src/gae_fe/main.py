import json

from flask import Flask, request
from google.cloud import vision

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_labels():
    uri = request.args.get('uri')
    if not uri:
        return 'uri required', 400
    results = _get_labels(uri)
    return json.dumps(results, indent=2), 200, {'Content-Type': 'application/json'}


def _get_labels(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    labels = client.label_detection(image=image).label_annotations
    return {'labels': [l.description for l in labels]}

