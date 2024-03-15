from pydantic import typing
from enum import Enum
import strawberry


@strawberry.enum
class EventType(Enum):
    TRIATHLON = "triathlon"
    DUATHLON = "duathlon"
    SPLASHNDASH = "splashndash"
    AQUABIKE = "aquabike"

# XXX Todo create enums for r_VenueEventType, r_VenueType and leg unit enum. See https://strawberry.rocks/docs/types/enums
# XXX how do I make ENUM type optional
@strawberry.type
class Venue:
    r_VenueId: typing.Optional[int] = 0
    r_VenueInstance: typing.Optional[int] = 0
    r_VenueName: typing.Optional[str] = ""
    r_VenueEventType: typing.Optional[int] = 0
    r_VenueType: typing.Optional[int] = 0
    r_VenueSwim: typing.Optional[float] = 0.0
    r_VenueSwimunits: typing.Optional[int] = 0
    r_VenueBike: typing.Optional[float] = 0.0
    r_VenueBikeunits: typing.Optional[int] = 0
    r_VenueRun: typing.Optional[float] = 0.0
    r_VenueRununits: typing.Optional[int] = 0
    r_VenueWebsite: typing.Optional[str] = ""
    r_VenueMgmt: typing.Optional[str] = ""
    r_VenueDesc: typing.Optional[str] = ""
    r_VenueCity: typing.Optional[str] = ""
    r_VenueState: typing.Optional[str] = ""
    r_VenueLocId: typing.Optional[int] = 0
    r_VenueCurrent: typing.Optional[bool] = False
