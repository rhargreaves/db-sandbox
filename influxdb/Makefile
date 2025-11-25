
influxdb-up:
	mkdir -p influxdb3/core/data
	mkdir -p influxdb3/core/plugins
	docker compose up influxdb3-core --build -d
.PHONY: influxdb-up

influxdb-down:
	docker compose down
.PHONY: influxdb-down

influxdb-clean:
	rm -rf influxdb3/core/data
	rm -rf influxdb3/core/plugins
	docker compose down
	docker compose rm -rf
.PHONY: influxdb-clean

influxdb-create-admin-token:
	docker compose exec influxdb3-core influxdb3 create token --admin
.PHONY: influxdb-create-admin-token

test:
	docker compose run python-tests
.PHONY: test