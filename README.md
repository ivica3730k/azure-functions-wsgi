# azure-functions-wsgi

This is a simple example of how azure functions work with wsgi. What its doing under the hood is basically running a wsgi app internally and then passsing the request to it. Once wsgi processes the request, it returns the response back to the azure function. That nowdays is all happening under the hood, but you can check out the inital idea here: https://www.youtube.com/watch?v=bEsgi1oi8qc&ab_channel=MicrosoftDeveloper

## What it does

### 1. Proxies to the wsgi using `azure_functions_wsgi_call` function set.

In this folder, we have set the route to match all the requests to `*`. This means that all the requests will be proxied to the wsgi app.

```json
"route":"{*route}",
```

This is our main api function which is used to serve your requests. It will be called for every request that comes to your function app.

### 2. Proxies the request to `static` folder using `azure_functions_static_files_call` function set.

In this folder, we have set the route to match anyyhing that starts with `/static/`. This means that all the requests that start with `/static/` will be proxied to the static folder. If your Django/flask or any other framework is configured with a different static folder, you can change the route to match that folder.

```json
"route":"static/{*route}",
```

This is our static files api function which is used to serve your static files. It will be called for every request that comes to your function app and starts with `/static/`. A custom python code is written to serve the static files. You can check it out in the function directory.

## Testing locally

### Using docker

Docker is the easiest way to test http azure functions locally, as it will take care of all the dependencies for you.
Simply run the provided docker-compose file and your functions will be auto-detected and deployed.
Docker-compose is set up with a volume, so any changes you make to the code will be automatically reflected in the container.

To run the docker-compose file, simply run `docker-compose up` in the root directory.

### Using Azure Functions Core Tools

Install the neccessary tools using `npm install -g azure-functions-core-tools@4 --unsafe-perm true` and then run `func host start` to start the functions.
Make sure you have your python environment activated before running the functions and that you have installed all the dependencies using `pip install -r requirements.txt`.
