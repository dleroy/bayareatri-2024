import typing
import strawberry
#from venue_scalar import Venue

@strawberry.type
class Race:
    r_RaceId: int
#  r_RaceVenueId: "Venue"
    r_RaceVenueId: int
    r_AgeData: int
    r_SplitData: int
    r_TransData: int
    r_UpdateDate: int
    r_RaceDate: int
    r_IMQual: int
    r_703Qual: int
    r_OrigResults: str
    r_RaceNote: str