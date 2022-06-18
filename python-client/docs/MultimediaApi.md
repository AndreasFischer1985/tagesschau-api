# tagesschau.MultimediaApi

All URIs are relative to *https://www.tagesschau.de*

Method | HTTP request | Description
------------- | ------------- | -------------

[**multimedia**](MultimediaApi.md#multimedia) | **GET** /api2/multimedia/ | Multimedia



# **multimedia**
> MultimediaResponse multimedia()

Multimedia

Multimedia-Beiträge

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import multimedia_api
from deutschland.tagesschau.model.multimedia_response import MultimediaResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.tagesschau.de
# See configuration.py for a list of all supported configuration parameters.
configuration = tagesschau.Configuration(
    host = "https://www.tagesschau.de"
)


# Enter a context with an instance of the API client
with tagesschau.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = multimedia_api.MultimediaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Multimedia
        api_response = api_instance.multimedia()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling MultimediaApi->multimedia: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MultimediaResponse**](MultimediaResponse.md)

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

