


# coding: utf-8
#
# Generated by sqlacodegen
#
from sqlalchemy import Column, DECIMAL, Date, Enum, Float, ForeignKey, SmallInteger, String, TIMESTAMP, Time, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class RVenueitem(Base):
    __tablename__ = 'r_venueitem'

    r_VenueId = Column(INTEGER, primary_key=True, server_default=text("'0'"))
    r_VenueInstance = Column(INTEGER, nullable=False, server_default=text("'0'"))
    r_VenueName = Column(String(128))
    r_VenueEventType = Column(Enum('TRIATHLON','DUATHLON','SPLASHNDASH','AQUABIKE'), nullable=False, server_default=text("'TRIATHLON'"))
    r_VenueType = Column(Enum('OTHER', 'MTNBIKE', 'SPRINT', 'OLYMPIC', 'INTL', 'HALF', 'IM'))
    r_VenueSwim = Column(Float)
    r_VenueSwimunits = Column(Enum('KMS', 'YARDS', 'MILES'))
    r_VenueBike = Column(Float)
    r_VenueBikeunits = Column(Enum('KMS', 'YARDS', 'MILES'))
    r_VenueRun = Column(Float)
    r_VenueRununits = Column(Enum('KMS', 'YARDS', 'MILES'))
    r_VenueWebsite = Column(String(128))
    r_VenueMgmt = Column(String(128))
    r_VenueDesc = Column(String(128))
    r_VenueCity = Column(String(64))
    r_VenueState = Column(String(8))
    r_VenueLocId = Column(INTEGER, nullable=False, server_default=text("'0'"))
    r_VenueCurrent = Column(TINYINT(1))


class RVenuelocateitem(Base):
    __tablename__ = 'r_venuelocateitem'
    __table_args__ = {'comment': 'Lat/Long for each unique venue location'}

    r_LocationId = Column(INTEGER, primary_key=True)
    r_VenueCount = Column(INTEGER, server_default=text("'0'"))
    r_VenueLat = Column(Float(9), nullable=False, server_default=text("'0.000000'"))
    r_VenueLong = Column(Float(9), nullable=False, server_default=text("'0.000000'"))


class RRaceitem(Base):
    __tablename__ = 'r_raceitem'

    r_RaceId = Column(INTEGER(10), primary_key=True, server_default=text("'0000000000'"))
    r_UpdateDate = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    r_RaceVenueId = Column(ForeignKey('r_venueitem.r_VenueId'), index=True)
    r_RaceDate = Column(Date)
    r_TransData = Column(TINYINT(1))
    r_SplitData = Column(TINYINT(1))
    r_AgeData = Column(TINYINT)
    r_IMQual = Column(TINYINT(1))
    r_703Qual = Column(TINYINT(1))
    r_OrigResults = Column(String(128))
    r_RaceNote = Column(String(128))

    r_venueitem = relationship('RVenueitem')


class RResultitem(Base):
    __tablename__ = 'r_resultitem'

    r_Id = Column(INTEGER, primary_key=True, unique=True)
    r_RaceId = Column(ForeignKey('r_raceitem.r_RaceId'), nullable=False, index=True, server_default=text("'0000000000'"))
    r_BibNumber = Column(SMALLINT)
    r_OverallPlace = Column(SMALLINT)
    r_DivisionPlace = Column(SMALLINT)
    r_GenderPlace = Column(SMALLINT)
    r_TotalTime = Column(Time)
    r_LastName = Column(String(32))
    r_FirstName = Column(String(32))
    r_Gender = Column(Enum('NONE', 'M', 'F'), index=True)
    r_Age = Column(SMALLINT)
    r_City = Column(String(32))
    r_State = Column(String(4))
    r_Country = Column(String(32))
    r_Division = Column(Enum('NONE', 'MPRO', 'WPRO', 'MELITE', 'WELITE', 'CLYDE', 'ATHENA', 'RELAYO', 'RELAYM', 'RELAYF', 'M1-19', 'M18-24', 'M20-24', 'M25-29', 'M30-34', 'M35-39', 'M40-44', 'M45-49', 'M50-54', 'M55-59', 'M60-64', 'M65-69', 'M70-74', 'M75-79', 'M80-84', 'M85-89', 'M90-94', 'W1-19', 'W18-24', 'W20-24', 'W25-29', 'W30-34', 'W35-39', 'W40-44', 'W45-49', 'W50-54', 'W55-59', 'W60-64', 'W65-69', 'W70-74', 'W75-79', 'W80-84', 'W85-89', 'W90-94'), index=True)
    r_SwimDiv = Column(SMALLINT)
    r_SwimGender = Column(SMALLINT)
    r_SwimOverall = Column(SMALLINT)
    r_SwimTime = Column(Time)
    r_SwimPace = Column(Time)
    r_T1Div = Column(SMALLINT)
    r_T1Gender = Column(SMALLINT)
    r_T1Overall = Column(SMALLINT)
    r_T1Time = Column(Time)
    r_BikeDiv = Column(SMALLINT)
    r_BikeGender = Column(SMALLINT)
    r_BikeOverall = Column(SMALLINT)
    r_BikeTime = Column(Time)
    r_BikePace = Column(DECIMAL(3, 1))
    r_T2Div = Column(SMALLINT)
    r_T2Gender = Column(SMALLINT)
    r_T2Overall = Column(SMALLINT)
    r_T2Time = Column(Time)
    r_RunDiv = Column(SMALLINT)
    r_RunGender = Column(SMALLINT)
    r_RunOverall = Column(SMALLINT)
    r_RunTime = Column(Time)
    r_RunPace = Column(Time)
    r_NoTransDiv = Column(SmallInteger)
    r_NoTransGender = Column(SmallInteger)
    r_NoTransOverall = Column(SmallInteger)
    r_Penalty = Column(Time)
    r_HawaiiQual = Column(TINYINT(1))
    r_HalfQual = Column(TINYINT(1))

    r_raceitem = relationship('RRaceitem')
