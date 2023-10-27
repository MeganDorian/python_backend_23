from enum import Enum


class SubjectType(Enum):
    LECTURE = "Лекция"
    PRACTICE = "Практика"


class Days(Enum):
    MON = "каждый понедельник"
    TUE = "каждый вторник"
    WED = "каждую среду"
    THU = "каждый четверг"
    FRI = "каждую пятницу"
    SAT = "каждую субботу"
    SUN = "каждое воскресенье"
