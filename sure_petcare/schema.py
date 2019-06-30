from datetime import datetime
from typing import Dict, NewType

from pydantic import BaseModel

HouseholdId = NewType("HouseholdId", int)
FlapId = NewType("FlapId", int)
PetId = NewType("PetId", int)
TagId = NewType("TagId", int)


# TODO - expand all the dicts
class Household(BaseModel):
    name: str
    olson_tz: str
    utc_offset: int
    default_router: int
    default_flap: FlapId
    routers: Dict[int, str]
    flaps: Dict[int, str]
    pets: Dict[PetId, dict]


class PetStatus(BaseModel):
    pet_id: PetId
    tag_id: TagId
    device_id: int
    where: int
    since: int


class Cache(BaseModel):
    AuthToken: str
    households: Dict[HouseholdId, Household]
    default_household: HouseholdId
    router_status: dict
    flap_status: dict
    pet_status: Dict[HouseholdId, Dict[PetId, PetStatus]]
    pet_timeline: dict
    house_timeline: dict
    version: int

    # TODO - move url cache out of top level
