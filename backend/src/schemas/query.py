import strawberry
from pydantic import typing
from strawberry.types import Info

from resolvers.bayareatri_resolver import get_race, get_races, get_venue, get_venues, get_result, get_results
from scalars.race_scalar import Race
from scalars.result_scalar import Result, UserResult
from scalars.venue_scalar import Venue

@strawberry.type
class Query:

    @strawberry.field
    async def results(self, info:Info) -> typing.List[Result]:
        """ Get all results """
        result_data_list = await get_results(info)
        return result_data_list
    
    @strawberry.field
    async def result(self, info:Info, raceid: int) -> Result:
        """ Get resulst by raceid """
        result_dict = await get_result(raceid, info)
        return result_dict
    
    @strawberry.field
    async def races(self, info:Info) -> typing.List[Race]:
        """ Get all races """
        race_data_list = await get_races(info)
        return race_data_list
    
    @strawberry.field
    async def race(self, info:Info, raceid: int) -> Race:
        """ Get race by id """
        race_dict = await get_race(raceid, info)
        return race_dict
    
    @strawberry.field
    async def venues(self, info:Info) -> typing.List[Venue]:
        """ Get all venues """
        venue_data_list = await get_venues(info)
        return venue_data_list
    
    @strawberry.field
    async def venue(self, info:Info, venueid: int) -> Venue:
        """ Get venue by id """
        venue_dict = await get_venue(venueid, info)
        return venue_dict