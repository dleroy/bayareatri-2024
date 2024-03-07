from typing import List

import strawberry

from resolvers.bayareatri_resolver import get_races
from scalars.race_scalar import Race


@strawberry.type
class Query:

    @strawberry.field
    async def races(self) -> List[Race]:
        """ Get all races """
        race_data_list = await get_races()
        return race_data_list

