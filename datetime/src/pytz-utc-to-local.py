from datetime import datetime
import pytz

utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
warsaw = pytz.timezone('Europe/Warsaw')


armstrong = datetime(1969, 7, 21, 14, 56, 15, tzinfo=utc)


utc_time = armstrong.astimezone(utc)
# datetime.datetime(1969, 7, 21, 14, 56, 15, tzinfo=<UTC>)

print(f'{utc_time:%Y-%m-%d %H:%M:%S %Z%z}')
# 1969-07-21 14:56:15 UTC+0000


waw_time = armstrong.astimezone(warsaw)
# datetime.datetime(1969, 7, 21, 15, 56, 15, tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)

print(f'{waw_time:%Y-%m-%d %H:%M:%S %Z%z}')
# 1969-07-21 15:56:15 CET+0100


est_time = armstrong.astimezone(eastern)
# datetime.datetime(1969, 7, 21, 10, 56, 15, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)

print(f'{est_time:%Y-%m-%d %H:%M:%S %Z%z}')
# 1969-07-21 10:56:15 EDT-0400





