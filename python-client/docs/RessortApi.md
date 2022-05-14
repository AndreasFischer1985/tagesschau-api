# tagesschau.RessortApi

All URIs are relative to *https://www.tagesschau.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ressort**](RessortApi.md#ressort) | **GET** /api2/{ressort} | Ressort-spezifische Nachrichten


# **ressort**
> NewsResponse ressort(ressort)

Ressort-spezifische Nachrichten

Ressort-spezifische Nachrichten, gefiltert über den Pfad-Parameter **ressort** (z.B. inland, ausland oder wirtschaft).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import ressort_api
from deutschland.tagesschau.model.news_response import NewsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.tagesschau.de
# See configuration.py for a list of all supported configuration parameters.
configuration = tagesschau.Configuration(
    host = "https://www.tagesschau.de"
)


# Enter a context with an instance of the API client
with tagesschau.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ressort_api.RessortApi(api_client)
    ressort = "ausland" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ressort-spezifische Nachrichten
        api_response = api_instance.ressort(ressort)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling RessortApi->ressort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ressort** | **str**|  |

### Return type

[**NewsResponse**](NewsResponse.md)

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

