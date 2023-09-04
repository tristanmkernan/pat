import calendar
import datetime

from dateutil import rrule
from dateutil.relativedelta import relativedelta


class EmojiHTMLCalendar(calendar.HTMLCalendar):
    cssclass_month = "table table-sm"

    def __init__(self, *args, year=None, month=None, active_dates=None, **kwargs):
        super().__init__(firstweekday=0)

        self.active_dates = active_dates or set()
        self.year = year or datetime.date.today().year
        self.month = month or datetime.date.today().month

    def formatday(self, day, weekday):
        if day == 0:
            # used for empty dates
            return super().formatday(day, weekday)
        else:
            # Calculate the date
            current_date = datetime.date(day=day, month=self.month, year=self.year)

            # Replace day numbers with emojis
            if current_date in self.active_dates:
                # green square emoji
                emoji = "🟩"
            else:
                # red square emoji
                emoji = "⬜"

            return f"<td class='day fs-1'>{emoji}</td>"


def make_activity_calendars(active_dates: set):
    start_date = min(active_dates) + relativedelta(day=1)
    end_date = max(active_dates) + relativedelta(day=31)

    calendars = []

    # Iterate over each month using rrule, backwards
    for dt in rrule.rrule(
        rrule.MONTHLY,
        dtstart=start_date,
        until=end_date,
        bymonthday=1,
        count=3,
    ):
        year = dt.year
        month = dt.month

        cal = EmojiHTMLCalendar(active_dates=active_dates, year=year, month=month)

        calendars.append(cal.formatmonth(year, month))

    return reversed(calendars)
