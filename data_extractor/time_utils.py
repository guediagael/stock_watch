from strenum import StrEnum


class Period(StrEnum):
    DAY = "1d"
    WEEK ="5d"
    MONTH ="1mo"
    QUARTER = "3mo"
    BIANNUAL ="6mo"
    YEAR= "1y"
    BIENNIAL= "2y"
    QUINQUENNIAL="5y"
    DECENNIAL ="10y"
    YESTERDAY= "ytd"
    MAX="max"

class Interval(StrEnum):
    A_MINUTE = "1m"
    TWO_MINUTES = "2m"
    FIVE_MINUTES="5m"
    FITHTEEN_MINUTES= "15m"
    HALF_HOUR = "30m"
    HOUR = "1h"
    DAY = "1d"
    WEEK = "1wk"
    MONTH = "1mo"
    TRIMESTER = "3mo"
