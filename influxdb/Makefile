db-up:
	mkdir -p influxdb3/core/data
	mkdir -p influxdb3/core/plugins
	docker compose up influxdb3-core --build -d
.PHONY: db-up

db-down:
	docker compose down
.PHONY: db-down

db-clean:
	rm -rf influxdb3/core/data
	rm -rf influxdb3/core/plugins
	docker compose down
	docker compose rm -rf
.PHONY: db-clean

create-admin-token:
	docker compose exec influxdb3-core influxdb3 create token --admin
.PHONY: create-admin-token

test:
	docker compose run python-tests
.PHONY: test