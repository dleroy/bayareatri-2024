import strawberry

# XXX Todo create enums for r_VenueEventType, r_VenueType and leg unit enum. See https://strawberry.rocks/docs/types/enums
@strawberry.type
class Venue:
    r_VenueId: int
    r_VenueInstance: int 
    r_VenueName: str
    r_VenueEventType: int
    r_VenueType: int
    r_VenueSwim: float
    r_VenueSwimunits: int
    r_VenueBike: float
    r_VenueBikeunits: int
    r_VenueRun: float
    r_VenueRununits: int
    r_VenueWebsite: str
    r_VenueMgmt: str
    r_VenueDesc: str
    r_VenueCity: str
    r_VenueState: str 
    r_VenueLocId: int
    r_VenueCurrent: bool
