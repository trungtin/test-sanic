import os
import sys
from sanic import Sanic
import json
import functools
from datetime import datetime

from dotenv import load_dotenv
from api.chat_models import ModelsView

from api.injectable import Realm, RequestContext

load_dotenv()

def dumps_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError

dumps = functools.partial(json.dumps, default=dumps_default)

app = Sanic("sanic-test", dumps=dumps)

app.config.REQUEST_TIMEOUT = sys.maxsize
app.config.RESPONSE_TIMEOUT = sys.maxsize
app.config.OAS_UI_DEFAULT = 'swagger'
app.config.SWAGGER_UI_CONFIGURATION = {
    "docExpansion": "list"
}
app.config.INJECTION_SIGNAL = "http.handler.before"

app.ext.add_dependency(Realm, Realm.from_header)
app.ext.add_dependency(RequestContext, RequestContext.create)

app.add_route(ModelsView.as_view(), '/models', version=1)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8008))
    app.run(host="0.0.0.0", port=port,
            debug=True if "--debug" in sys.argv else False, dev=True if "--dev" in sys.argv else False)
