run:
	docker run -d --name some-clickhouse-server \
		--ulimit nofile=262144:262144 \
		clickhouse/clickhouse-server
.PHONY: run

stop:
	docker stop some-clickhouse-server
.PHONY: stop

clean: stop
	docker rm some-clickhouse-server
.PHONY: clean