from sqlalchemy import select
from sqlalchemy.orm import subqueryload,load_only

from db.db import get_session
from helpers.helper import get_only_selected_fields, get_valid_data
from models.bayareatri_model import RRaceitem, RResultitem, RVenueitem

from scalars.race_scalar import Race
from scalars.result_scalar import Result
from scalars.venue_scalar import Venue


async def get_results(info):
    """ Get all results resolver """
    selected_fields = get_only_selected_fields(RResultitem,info)
    async with get_session() as s:
        sql = select(RResultitem).options(load_only(*selected_fields)) \
        .order_by(RResultitem.r_DivisionPlace)
        db_results = (await s.execute(sql)).scalars().unique().all()

    results_data_list = []
    for result in db_results:
        result_dict = get_valid_data(result,RResultitem)
        results_data_list.append(Result(**result_dict))

    return results_data_list

async def get_result(raceid, info):
    """ Get specific results by raceid resolver """
    selected_fields = get_only_selected_fields(RResultitem,info)
    async with get_session() as s:
        sql = select(RResultitem).options(load_only(*selected_fields)).join(RResultitem.r_raceitem) \
        .filter(RResultitem.r_RaceId == raceid).order_by(RResultitem.r_OverallPlace)
        db_results = (await s.execute(sql)).scalars().unique().all()
    
    results_data_list = []
    for result in db_results:
        result_dict = get_valid_data(result,RResultitem)
        results_data_list.append(Result(**result_dict))

    return results_data_list

async def get_races(info):
    """ Get all races resolver """
    selected_fields = get_only_selected_fields(RRaceitem,info)
    async with get_session() as s:
        sql = select(RRaceitem).options(load_only(*selected_fields)) \
        .order_by(RRaceitem.r_RaceId)
        db_races = (await s.execute(sql)).scalars().unique().all()

    races_data_list = []
    for race in db_races:
        race_dict = get_valid_data(race,RRaceitem)
        races_data_list.append(Race(**race_dict))

    return races_data_list

async def get_race(raceid, info):
    """ Get specific race by id resolver """
    selected_fields = get_only_selected_fields(RRaceitem,info)
    async with get_session() as s:
        sql = select(RRaceitem).options(load_only(*selected_fields)) \
        .filter(RRaceitem.r_RaceId == raceid).order_by(RRaceitem.r_RaceId)
        db_race = (await s.execute(sql)).scalars().unique().one()
    
    race_dict = get_valid_data(db_race,RRaceitem)
    return Race(**race_dict)

async def get_venues(info):
    """ Get all races resolver """
    selected_fields = get_only_selected_fields(RVenueitem,info)
    async with get_session() as s:
        sql = select(RVenueitem).options(load_only(*selected_fields)) \
        .order_by(RVenueitem.r_VenueId)
        db_venues = (await s.execute(sql)).scalars().unique().all()

    venues_data_list = []
    for venue in db_venues:
        venue_dict = get_valid_data(venue,RVenueitem)
        venues_data_list.append(Venue(**venue_dict))

    return venues_data_list

async def get_venue(venueid, info):
    """ Get specific venue by id resolver """
    selected_fields = get_only_selected_fields(RVenueitem,info)
    async with get_session() as s:
        sql = select(RVenueitem).options(load_only(*selected_fields))\
        .filter(RVenueitem.r_VenueId == venueid).order_by(RVenueitem.r_VenueId)
        db_venue = (await s.execute(sql)).scalars().unique().one()
    
    venue_dict = get_valid_data(db_venue,RVenueitem)
    return Venue(**venue_dict)