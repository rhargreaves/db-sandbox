import os
from influxdb_client_3 import InfluxDBClient3, Point


INFLUXDB_HOST = os.getenv("INFLUXDB_HOST")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
DB_NAME = "test-db"


def test_influxdb_write():
    client = InfluxDBClient3(
        host=INFLUXDB_HOST,
        token=INFLUXDB_TOKEN,
    )

    p = Point("test").tag("location", "Prague").field("value", 1)
    client.write(database=DB_NAME, record=p.to_line_protocol())

    table = client.query(
        "SELECT * FROM test WHERE time > now() - INTERVAL '3 seconds'",
        language="sql",
        database=DB_NAME,
    )
    rows = table.to_pylist()
    assert len(rows) == 1
