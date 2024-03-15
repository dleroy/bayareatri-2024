import datetime
from pydantic import typing
import strawberry

from .venue_scalar import Venue

@strawberry.type
class Race:
    r_RaceId: typing.Optional[int] = 0
    r_RaceVenueId: typing.Optional["Venue"] = None
    r_AgeData: typing.Optional[bool] = False
    r_SplitData: typing.Optional[bool] = False
    r_TransData: typing.Optional[bool] = False
    r_UpdateDate: typing.Optional[datetime.datetime] = None
    r_RaceDate: typing.Optional[datetime.datetime] = None
    r_IMQual: typing.Optional[bool] = False
    r_703Qual: typing.Optional[bool] = False
    r_OrigResults: typing.Optional[str] = ""
    r_RaceNote: typing.Optional[str] = ""