import json
import os
import urllib.parse
import urllib.request

import flask

from . import application, payment

ADDRESS = 'https://translation.googleapis.com'
ENCODING = 'utf-8'


@application.route('/')
@payment.required(1)
def index():
    path = '/language/translate/v2'
    query = {'key': os.environ['API_KEY']}
    for parameter in ('q', 'target', 'format', 'source', 'model',):
        query[parameter] = flask.request.args.get(parameter, '')
    parameters = urllib.parse.urlencode(query)
    address = ''.join((ADDRESS, path, '?', parameters))
    request = urllib.request.Request(address, method='POST')
    try:
        response = urllib.request.urlopen(request)
        payload = response.read().decode(ENCODING)
    except urllib.error.HTTPError as e:
        payload = e.read().decode(ENCODING)
        return flask.Response(
            response=payload,
            status=e.code,
            mimetype='application/json'
        )
    instance = json.loads(payload)['data']['translations'][0]['translatedText']
    return flask.jsonify(instance)
