import datetime
from dateutil.relativedelta import relativedelta


def get_time_diff_description(start: datetime.datetime,
                              end: datetime.datetime) -> str | None:
    if type(start) is not datetime.datetime or \
       type(end) is not datetime.datetime:
        return None
    time_diff: relativedelta = relativedelta(start, end)
    times: dict = {'year': time_diff.years,
                   'month': time_diff.months,
                   'week': time_diff.weeks,
                   'day': time_diff.days % 7}
    result: str = ""
    has_something: bool = False
    for key, value in times.items():
        if value <= 0:
            continue
        if has_something is True:
            result += ", "
        has_something = True
        result += f"{value} {key}s" if value != 1 else f"{value} {key}"
    return result
