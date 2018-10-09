from datetime import datetime, timezone
import json


DATA = """
{
    "email": "jose.jimenez@nasa.gov",
    "date": "1961-04-12",
    "datetime": "1969-07-21T14:56:15.000Z"
}
"""


def decoder(obj):
    for key, value in obj.items():
        if key == 'datetime':
            dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
            obj['datetime'] = dt.replace(tzinfo=timezone.utc)

        elif key == 'date':
            dt = datetime.strptime(value, '%Y-%m-%d')
            obj['date'] = dt.replace(tzinfo=timezone.utc).date()

    return obj


output = json.loads(DATA, object_hook=decoder)

print(output)
# {
#     'email': 'jose.jimenez@nasa.gov',
#     'date': datetime.date(1961, 4, 12),
#     'datetime': datetime.datetime(1969, 7, 21, 14, 56, 15, tzinfo=datetime.timezone.utc),
# }
