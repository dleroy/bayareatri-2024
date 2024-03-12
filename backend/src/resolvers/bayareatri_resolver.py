from sqlalchemy import select

from db.db import get_session
from models import bayareatri_model

from scalars.race_scalar import Race
from scalars.result_scalar import Result
from scalars.venue_scalar import Venue



async def get_races():
    """ Get all races resolver """
    async with get_session() as s:
        sql = select(bayareatri_model.RRaceitem).order_by(bayareatri_model.RRaceitem.r_RaceId)
        db_races = (await s.execute(sql)).scalars().unique().all()
    race_list = []
    for races in db_races:
        race_dict = get_valid_data(races, bayareatri_model.RRaceitem)
        race_list.append(Race(**race_dict))
    return race_list

async def get_results_by_id(raceid: int):
    """ Get all results resolver """
    async with get_session() as s:
        sql = select(bayareatri_model.RResultitem).where(bayareatri_model.RResultitem.r_RaceId == raceid)
        db_results = (await s.execute(sql)).scalars().unique().all()
    result_list = []
    for races in db_results:
        result_dict = get_valid_data(races, bayareatri_model.RResultitem)
        result_list.append(Result(**result_dict))
    return result_list

async def get_user_results_by_name(firstname: str, lastname: str):
    """ Get all user results resolver """
    async with get_session() as s:
        sql = select(bayareatri_model.RResultitem).where(bayareatri_model.RResultitem.r_FirstName.ilike(firstname) & bayareatri_model.RResultitem.r_LastName.ilike(lastname))
        db_results = (await s.execute(sql)).scalars().unique().all()
    result_list = []
    for races in db_results:
        result_dict = get_valid_data(races, bayareatri_model.RResultitem)
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

#
#Results query
#$query = "select * from r_resultitem where r_LastName like '" . $lastn . "%' and r_FirstName like '" . $firstn . "%'
#          order by CAST(r_RaceId as unsigned) DESC";


#            $racename = find_racename_by_id($row['r_RaceId']);
#    $venuequery = "select * from r_venueitem
#                 where r_VenueId = '$venueid->r_RaceVenueId'";                                          

#            $raceinfo = find_raceinfo_by_id($row['r_RaceId']);
# // We retreive race date in 2 different printable formats, different from way stored in MySQL
#    // fulldate:  June 21, 2005
#    // fmtdate:   06/21/2005
#    // MySQL default  2005-06-21
#    $infoquery = 'select *, date_format( r_RaceDate, \'%M %e, %Y\' ) as fulldate' .
#        ', date_format( r_RaceDate, \'%m/%d/%Y\' ) as fmtdate' .
#        ' from r_raceitem where' .
#        " r_RaceID='$raceid'";
