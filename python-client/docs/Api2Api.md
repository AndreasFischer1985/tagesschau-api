# tagesschau.Api2Api

All URIs are relative to *https://www.tagesschau.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api2**](Api2Api.md#api2) | **GET** /api2/ | Wichtige Nachrichten und Eilmeldungen


# **api2**
> HomepageResponse api2()

Wichtige Nachrichten und Eilmeldungen

Wichtige Nachrichten und Eilmeldungen, sowie regionale Nachrichten aus dem Pfad '/api2/homepage'. API2 tritt die Nachfolge der vorangegangenen API an, die nach eigenen Angaben seit 01.10.2018 obsolet ist (vgl. https://www.tagesschau.de/api/ - obwohl z.B. unter https://www.tagesschau.de/api/inland/, https://www.tagesschau.de/api/ausland/, https://www.tagesschau.de/api/wirtschaft/ und https://www.tagesschau.de/api/regional/ durchaus noch aktuelle Beiträge zu finden sind).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import api2_api
from deutschland.tagesschau.model.homepage_response import HomepageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.tagesschau.de
# See configuration.py for a list of all supported configuration parameters.
configuration = tagesschau.Configuration(
    host = "https://www.tagesschau.de"
)


# Enter a context with an instance of the API client
with tagesschau.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api2_api.Api2Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wichtige Nachrichten und Eilmeldungen
        api_response = api_instance.api2()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling Api2Api->api2: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HomepageResponse**](HomepageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

