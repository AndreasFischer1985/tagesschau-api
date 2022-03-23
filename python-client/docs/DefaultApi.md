# tagesschau.DefaultApi

All URIs are relative to *https://www.tagesschau.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api2**](DefaultApi.md#api2) | **GET** /api2 | Wichtige Nachrichten und Eilmeldungen
[**channels**](DefaultApi.md#channels) | **GET** /api2/channels | Aktuelle Kanäle
[**homepage**](DefaultApi.md#homepage) | **GET** /api2/homepage | Ausgewählte aktuelle Nachrichten und Eilmeldungen
[**multimedia**](DefaultApi.md#multimedia) | **GET** /api2/multimedia | Multimedia
[**news**](DefaultApi.md#news) | **GET** /api2/news | Aktuelle Nachrichten und Eilmeldungen
[**newsfeed**](DefaultApi.md#newsfeed) | **GET** /api2/newsfeed-101~_date-{datumsangabe}.json | Newsfeed
[**ressort**](DefaultApi.md#ressort) | **GET** /api2/{ressort} | Ressort-spezifische Nachrichten
[**search**](DefaultApi.md#search) | **GET** /api2/search | Suche


# **api2**
> HomepageResponse api2()

Wichtige Nachrichten und Eilmeldungen

Wichtige Nachrichten und Eilmeldungen, sowie regionale Nachrichten aus dem Pfad '/api2/homepage'. API2 tritt die Nachfolge der vorangegangenen API an, die nach eigenen Angaben seit 01.10.2018 obsolet ist (vgl. https://www.tagesschau.de/api/ - obwohl z.B. unter https://www.tagesschau.de/api/inland/, https://www.tagesschau.de/api/ausland/, https://www.tagesschau.de/api/wirtschaft/ und https://www.tagesschau.de/api/regional/ durchaus noch aktuelle Beiträge zu finden sind).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Wichtige Nachrichten und Eilmeldungen
        api_response = api_instance.api2()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->api2: %s\n" % e)
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

# **channels**
> ChannelsResponse channels()

Aktuelle Kanäle

Aktuelle Kanäle (im Livestream: tagesschau24, tagesschau in 100 Sekunden, tagesschau, tagesschau 20 Uhr, tagesthemen, nachtmagazin, Bericht aus Berlin, tagesschau vor 20 Jahren, tagesschau mit Gebärdensprache

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
from deutschland.tagesschau.model.channels_response import ChannelsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.tagesschau.de
# See configuration.py for a list of all supported configuration parameters.
configuration = tagesschau.Configuration(
    host = "https://www.tagesschau.de"
)


# Enter a context with an instance of the API client
with tagesschau.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Aktuelle Kanäle
        api_response = api_instance.channels()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->channels: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ChannelsResponse**](ChannelsResponse.md)

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

# **homepage**
> HomepageResponse homepage()

Ausgewählte aktuelle Nachrichten und Eilmeldungen

Ausgewählte aktuelle Nachrichten und Eilmeldungen, sowie regionale Nachrichten, die auf der Startseite der Tagesschau-App zu sehen sind.

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Ausgewählte aktuelle Nachrichten und Eilmeldungen
        api_response = api_instance.homepage()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->homepage: %s\n" % e)
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

# **multimedia**
> MultimediaResponse multimedia()

Multimedia

Multimedia-Beiträge

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Multimedia
        api_response = api_instance.multimedia()
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->multimedia: %s\n" % e)
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

# **news**
> NewsResponse news()

Aktuelle Nachrichten und Eilmeldungen

Aktuelle Nachrichten und Eilmeldungen

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    regions = 1 # int | Bundesland - 1=Baden-Württemberg, 2=Bayern, 3=Berlin, 4=Brandenburg, 5=Bremen, 6=Hamburg, 7=Hessen, 8=Mecklenburg-Vorpommern, 9=Niedersachsen, 10=Nordrhein-Westfalen, 11=Rheinland-Pfalz, 12=Saarland, 13=Sachsen, 14=Sachsen-Anhalt, 15=Schleswig-Holstein, 16=Thüringen. Mehrere Komma-getrennte Angaben möglich (z.B. regions=1,2). (optional)
    ressort = "ausland" # str | Ressort/Themengebiet (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Aktuelle Nachrichten und Eilmeldungen
        api_response = api_instance.news(regions=regions, ressort=ressort)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->news: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regions** | **int**| Bundesland - 1&#x3D;Baden-Württemberg, 2&#x3D;Bayern, 3&#x3D;Berlin, 4&#x3D;Brandenburg, 5&#x3D;Bremen, 6&#x3D;Hamburg, 7&#x3D;Hessen, 8&#x3D;Mecklenburg-Vorpommern, 9&#x3D;Niedersachsen, 10&#x3D;Nordrhein-Westfalen, 11&#x3D;Rheinland-Pfalz, 12&#x3D;Saarland, 13&#x3D;Sachsen, 14&#x3D;Sachsen-Anhalt, 15&#x3D;Schleswig-Holstein, 16&#x3D;Thüringen. Mehrere Komma-getrennte Angaben möglich (z.B. regions&#x3D;1,2). | [optional]
 **ressort** | **str**| Ressort/Themengebiet | [optional]

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

# **newsfeed**
> NewsResponse newsfeed(datumsangabe)

Newsfeed

Nachrichten und Eilmeldungen zu einem ausgewählten Datum der jüngeren Vergangenheit (bis zu etwa einem Monat) im Format yymmdd (z.B. 220228 für den 28.02.2022).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    datumsangabe = 220228 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Newsfeed
        api_response = api_instance.newsfeed(datumsangabe)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->newsfeed: %s\n" % e)
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

# **ressort**
> NewsResponse ressort(ressort)

Ressort-spezifische Nachrichten

Ressort-spezifische Nachrichten, gefiltert über den Pfad-Parameter **ressort** (z.B. inland, ausland oder wirtschaft).

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    ressort = "ausland" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Ressort-spezifische Nachrichten
        api_response = api_instance.ressort(ressort)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->ressort: %s\n" % e)
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

# **search**
> SearchResponse search()

Suche

Suche

### Example


```python
import time
from deutschland import tagesschau
from deutschland.tagesschau.api import default_api
from deutschland.tagesschau.model.search_response import SearchResponse
from pprint import pprint
# Defining the host is optional and defaults to https://www.tagesschau.de
# See configuration.py for a list of all supported configuration parameters.
configuration = tagesschau.Configuration(
    host = "https://www.tagesschau.de"
)


# Enter a context with an instance of the API client
with tagesschau.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    search_text = "Ukraine" # str | Suchtext (optional)
    page_size = 0 # int | Seite (optional)
    result_page = 2 # int | Suchergebnisse pro Seite (1-30) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Suche
        api_response = api_instance.search(search_text=search_text, page_size=page_size, result_page=result_page)
        pprint(api_response)
    except tagesschau.ApiException as e:
        print("Exception when calling DefaultApi->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| Suchtext | [optional]
 **page_size** | **int**| Seite | [optional]
 **result_page** | **int**| Suchergebnisse pro Seite (1-30) | [optional]

### Return type

[**SearchResponse**](SearchResponse.md)

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

