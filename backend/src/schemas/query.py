from typing import List

import strawberry

from resolvers.bayareatri_resolver import get_races, get_results_by_id, get_user_results_by_name
from scalars.race_scalar import Race
from scalars.result_scalar import Result, UserResult
from scalars.venue_scalar import Venue


@strawberry.type
class Query:

    @strawberry.field
    async def races(self) -> List[Race]:
        """ Get all races """
        race_data_list = await get_races()
        return race_data_list

    @strawberry.field
    async def results(self, raceid: int) -> List[Result]:
        """ Get all results"""
        result_data_list = await get_results_by_id(raceid)
        return result_data_list
    
    @strawberry.field
    async def user_results(self, firstname: str, lastname: str) -> List[Result]:
        """ Get all users results"""
        result_data_list = await get_user_results_by_name(firstname, lastname)
        return result_data_list
