from json import loads as json_loads
from dataclasses import dataclass, field

from sanic.request import Request

@dataclass
class Realm:
    @classmethod
    async def from_header(cls, request: Request):
        return cls()


@dataclass
class RequestContext:
    realm: Realm

    @classmethod
    def create(cls, request: Request, realm: Realm):
        return cls(realm=realm)
