# haihai.link-API
programmatically access [haihai.link](https://haihai.link)

## configuration:
[only required if accessing all data for a specified user] - to setup account configuration for API access, set credentials in [api_config.py](https://github.com/senaonp/haihai.link-API/blob/main/api_config.py#L3-L4)

## how to use:

The API is accessed through [script.py](https://github.com/senaonp/haihai.link-API/blob/main/script.py); several examples have been provided for reference

There are 2 ways to access data in the API:
### - public access
  - does not require credentials to be setup in `api_config.py`
  - provides access to publicly available information for user accounts and widget data
### - user account access
  - requires credentials to be setup in `api_config.py`
  - allows access to all data belonging to the configured user account
  - steps to properly start and end an API session:
    - call `initializeSession()` to start an API session
    - do stuff
    - call `endSession()` to end the API session
