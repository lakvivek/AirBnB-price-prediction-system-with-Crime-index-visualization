build:
	docker build -t sms .

run-interactive:
	docker run -it -p 5000:5000 --name sms_interactive sms

run-detached:
	docker run -d -p 5000:5000 --name sms_detached sms

clean:
	docker rm -f sms_detached sms_interactive

.PHONY: clean build run-interactive run-detached

