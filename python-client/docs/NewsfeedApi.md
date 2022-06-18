# tagesschau.NewsfeedApi

All URIs are relative to *https://www.tagesschau.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newsfeed**](NewsfeedApi.md#newsfeed) | **GET** /api2/newsfeed-101~_date-{datumsangabe}.json | Newsfeed


# **newsfeed**
> NewsResponse newsfeed(datumsangabe)

Newsfeed

Nachrichten und Eilmeldungen zu einem ausgewählten Datum der jüngeren Vergangenheit (bis zu etwa einem Monat) im Format yymmdd (z.B. 220228 für den 28.02.2022).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import newsfeed_api
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
    api_instance = newsfeed_api.NewsfeedApi(api_client)
    datumsangabe = 220228 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Newsfeed
        api_response = api_instance.newsfeed(datumsangabe)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling NewsfeedApi->newsfeed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datumsangabe** | **int**|  |

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

