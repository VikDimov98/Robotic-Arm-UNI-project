### API
Here you can find our api wrapper. This folder is designed as a python package. Import it into any project and you are good to go. The `wrapper.py` contains all functions for sending HTTP requests. It will not do anything if run by itself. The `config.py` is responsible for creating a small UI for easy modification of the configuration. This includes changing the target ip and port. Whenever the api package or parts of it are imported, the `__init__.py` will run. This makes sure a `config.json` is created if not alreay present.

### Requirements
 - Python 3.8
 - `wrapper.py` makes use of the [requests](https://requests.readthedocs.io/en/master/) package

### Notes
You can use the wrapper standalone as basis for any other project.