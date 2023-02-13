from datetime import datetime, timedelta


def get_half_hour_timedelta(date: datetime) -> (datetime, datetime):
    half_hour_timedelta = (date - timedelta(minutes=30), date + timedelta(minutes=30))

    return half_hour_timedelta
