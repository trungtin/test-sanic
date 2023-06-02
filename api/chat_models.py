from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.request import Request
from sanic_ext import openapi, validate
from api.auth import authenticated
from api.injectable import Realm, RequestContext

from sanic_ext import openapi


class ModelsView(HTTPMethodView):
    @authenticated
    async def get(self, request: Request, ctx: RequestContext):
        "Get all avatars"
        return json({'ok': True})
