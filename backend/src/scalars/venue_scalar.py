from pydantic import typing
import strawberry


@strawberry.type
class Venue:
    r_VenueId: typing.Optional[int] = 0
    r_VenueInstance: typing.Optional[int] = 0
    r_VenueName: typing.Optional[str] = ""
    r_VenueEventType: typing.Optional[str] = ""
    r_VenueType: typing.Optional[str] = ""
    r_VenueSwim: typing.Optional[float] = 0.0
    r_VenueSwimunits: typing.Optional[str] = ""
    r_VenueBike: typing.Optional[float] = 0.0
    r_VenueBikeunits: typing.Optional[str] = ""
    r_VenueRun: typing.Optional[float] = 0.0
    r_VenueRununits: typing.Optional[str] = ""
    r_VenueWebsite: typing.Optional[str] = ""
    r_VenueMgmt: typing.Optional[str] = ""
    r_VenueDesc: typing.Optional[str] = ""
    r_VenueCity: typing.Optional[str] = ""
    r_VenueState: typing.Optional[str] = ""
    r_VenueLocId: typing.Optional[int] = 0
    r_VenueCurrent: typing.Optional[bool] = False
