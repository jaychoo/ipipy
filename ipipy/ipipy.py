# -*- coding: utf-8 -*-

import logging
import argparse

import requests
import flask
from flask.ext.restful import Resource, Api


app = None
api = None


def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()
    except TimeoutError as e:
        logging.debug(e)
        return {'message': 'Time Out'}
    except Exception as e:
        logging.exception(e)
        return {'message': 'Unknown Error'}


class Ipipy(Resource):

    def get(self):
        return get_ip_address()


def setup_web():
    global app
    global api

    app = flask.Flask(__name__)
    api = Api(app)

    api.add_resource(Ipipy, '/')
    return app


def main_web(port=8000, **kwargs):
    global app

    app = setup_web()
    app.run(host='0.0.0.0', port=port, **kwargs)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--http', action="store",
                        type=int, dest='http_port')

    args, argv = parser.parse_known_args()

    if args.http_port:
        main_web(port=args.http_port)
    else:
        result = get_ip_address()
        print(result)

        return result


if __name__ == '__main__':
    main()
