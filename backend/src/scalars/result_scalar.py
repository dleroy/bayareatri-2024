from datetime import time
import strawberry
#from race_scalar import Race

# XXX Todo create enums for r_Division and r_Gender. See https://strawberry.rocks/docs/types/enums
@strawberry.type
class Result:
    r_Id: int
#    r_RaceId: "Race"
    r_RaceId: int = strawberry.field(description="Race ID in form of a date YYYYMMDDxx.")
    r_BibNumber: int
    r_OverallPlace: int
    r_DivisionPlace: int
    r_GenderPlace: int
    r_TotalTime: time
    r_LastName: str
    r_FirstName: str
    r_Gender: str
    r_Age: int
    r_City: str
    r_State: str
    r_Country: str
    r_Division: str
    r_SwimDiv: int
    r_SwimGender: int
    r_SwimOverall: int
    r_SwimTime: time
    r_SwimPace: time
    r_T1Div: int
    r_T1Gender: int
    r_T1Overall: int
    r_T1Time: time
    r_BikeDiv: int
    r_BikeGender: int
    r_BikeOverall: int
    r_BikeTime: time
    r_BikePace: float
    r_T2Div: int
    r_T2Gender: int
    r_T2Overall: int
    r_T2Time: time
    r_RunDiv: int
    r_RunGender: int
    r_RunOverall: int
    r_RunTime: time
    r_RunPace: time
    r_NoTransDiv: int
    r_NoTransGender: int
    r_NoTransOverall: int
    r_Penalty: time
    r_HawaiiQual: bool
    r_HalfQual: bool

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
