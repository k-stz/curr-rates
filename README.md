# Currency Rates viewer
A web application displaying currency exchange rates present and past. 

Tt uses the "Free Currency Exchange Rates API" https://github.com/fawazahmed0/currency-api

## Webframework
Uses the python web framework `Flask` with its development webserver (TODO move to nginx), to provide a frontend with html form input processing, redirections, html page rendering and to call the currency API and processes the data.

`Jinja2`-templating engine is used to generate the html website code.

The `flask extentension WTForms` provides the input form so the user can input to let the user choose which currency and date they care about being rendered into a chart.

The `chart.js` JS library is used to render a interactive bar-chart displaying the currency exchange rate data.

## Containerization
The web application is containerized on top a python:3.10.5-apline `image layer`. Here a `python virtualenvironment` is created containing all the necessary flask modules and prepared to launch the application inside it.

The container is managed via `docker-compose`, by providing a service with abuildpath of the `Dockerfile` and the port to be attached to the host machine. 

## Ansible: provisioning

## Installation
docker compose: run `docker compose up` or `docker-compose up` inside `app/docker-compose.yml`. This will by default make the web service available on Port 5000.

Ansible: use Ansible playbook to install the service on a given server (written for Ubuntu 22.04 LTS) with:
```shell
ansible-playbook -i hosts.ini curr-rates-playbook.yml
```

# example api call:
https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-10-21/currencies/eur.json
