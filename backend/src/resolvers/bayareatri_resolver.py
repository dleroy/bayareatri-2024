from sqlalchemy import select

from db.db import get_session
from models import bayareatri_model

from scalars.race_scalar import Race

async def get_races():
    """ Get all races resolver """
    async with get_session() as s:
        sql = select(bayareatri_model.Raceitem).order_by(bayareatri_model.Raceitem.r_RaceId)
        db_races = (await s.execute(sql)).scalars().unique().all()
    race_list = []
    for races in db_races:
        race_dict = get_valid_data(races, bayareatri_model.Raceitem)
        print(race_dict)
        race_list.append(Race(**race_dict))
    return race_list

async def get_results_by_id(id: int):
    """ Get all results by id resolver """
    async with get_session() as s:
        sql = select(bayareatri_model.Resultitem).where(bayareatri_model.Result.r_RaceId == id)
        db_results = (await s.execute(sql)).scalars().unique().all()
    result_list = []
    for results in db_results:
        result_dict = get_valid_data(results, bayareatri_model.Resultitem)
    result_list.append(Result(**result_dict))
    return result_list

def get_valid_data(model_data_object, model_class):
    data_dict = {}
    for column in model_class.__table__.columns:
        try:
            data_dict[column.name] = getattr(model_data_object, column.name)
        except:
            pass
    return data_dict