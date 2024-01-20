import azure.functions as func
from ..sample_flask_app import app as application

main = func.WsgiMiddleware(application).main
