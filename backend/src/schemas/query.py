from typing import List

import strawberry

from resolvers.bayareatri_resolver import get_races, get_results_by_id
from scalars.race_scalar import Race
from scalars.result_scalar import Result


@strawberry.type
class Query:

    @strawberry.field
    async def races(self) -> List[Race]:
        """ Get all races """
        race_data_list = await get_races()
        return race_data_list

    @strawberry.field
    async def results(self, id: int) -> List[Result]:
        """ Get all results """
        result_data_list = await get_results(id)
        return result_data_list