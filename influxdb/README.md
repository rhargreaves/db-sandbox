# InfluxDB

## First Time Setup

1. Start InfluxDB:
	```
	make db-up
	```

2. Create an admin token:
	```
	make create-admin-token
	```

3. Copy the admin token and save it to the .env file:
	```
	export INFLUXDB_TOKEN=<admin-token>
	```

## Run Tests

With InfluxDB running:

```
make test
```