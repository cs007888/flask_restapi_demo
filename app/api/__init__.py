from flask_restplus import Api
from .test import ns as testNS

api = Api()
api.add_namespace(testNS)
