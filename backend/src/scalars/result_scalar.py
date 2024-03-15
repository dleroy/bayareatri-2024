from datetime import time
import strawberry
from enum import Enum
from pydantic import typing
from .race_scalar import Race



@strawberry.enum
class Gender(Enum):
    MALE = "Male"
    FEMAIL = "Female"
    NONE = "None"


# XXX Todo create enums for r_Division and r_Gender. See https://strawberry.rocks/docs/types/enums
@strawberry.type
class Result:
    r_Id: typing.Optional[int] = 0
    r_RaceId: typing.Optional["Race"] = None
    r_BibNumber: typing.Optional[int] = 0
    r_OverallPlace: typing.Optional[int] = 0
    r_DivisionPlace: typing.Optional[int] = 0
    r_GenderPlace: typing.Optional[int] = 0
    r_TotalTime: typing.Optional[time] = None
    r_LastName: typing.Optional[str] = ""
    r_FirstName: typing.Optional[str] = ""
    r_Gender: typing.Optional[str] = ""
    r_Age: typing.Optional[int] = 0
    r_City: typing.Optional[str] = ""
    r_State: typing.Optional[str] = ""
    r_Country: typing.Optional[str] = ""
    r_Division: typing.Optional[str] = ""
    r_SwimDiv: typing.Optional[int] = 0
    r_SwimGender: typing.Optional[int] = 0
    r_SwimOverall: typing.Optional[int] = 0
    r_SwimTime: typing.Optional[time] = None
    r_SwimPace: typing.Optional[time] = None
    r_T1Div: typing.Optional[int] = 0
    r_T1Gender: typing.Optional[int] = 0
    r_T1Overall: typing.Optional[int] = 0
    r_T1Time: typing.Optional[time] = None
    r_BikeDiv: typing.Optional[int] = 0
    r_BikeGender: typing.Optional[int] = 0
    r_BikeOverall: typing.Optional[int] = 0
    r_BikeTime: typing.Optional[time] = None
    r_BikePace: typing.Optional[float] =0.0
    r_T2Div: typing.Optional[int] = 0
    r_T2Gender: typing.Optional[int] = 0
    r_T2Overall: typing.Optional[int] = 0
    r_T2Time: typing.Optional[time] = None
    r_RunDiv: typing.Optional[int] = 0
    r_RunGender: typing.Optional[int] = 0
    r_RunOverall: typing.Optional[int] = 0
    r_RunTime: typing.Optional[time] = None
    r_RunPace: typing.Optional[time] = None
    r_NoTransDiv: typing.Optional[int] = 0
    r_NoTransGender: typing.Optional[int] = 0
    r_NoTransOverall: typing.Optional[int] = 0
    r_Penalty: typing.Optional[time] = None
    r_HawaiiQual: typing.Optional[bool] = False
    r_HalfQual: typing.Optional[bool] = False

@strawberry.type
class UserResult:
    r_RaceDate: int
    r_LastName: str
    r_FirstName: str
    r_TotalTime: time
    r_OverallPlace: int
    r_DivisionPlace: int
    r_Age: int
    r_SwimTime: time
    r_BikeTime: time
    r_RunTime: time
    r_VenueName: str
