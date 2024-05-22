# digitale_verwaltung.DataApi

All URIs are relative to *https://dashboard-daten.digitale-verwaltung.de/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all**](DataApi.md#find_all) | **GET** /v1/data | Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten
[**find_by_filter**](DataApi.md#find_by_filter) | **GET** /v1/data/{ars} | Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten eingeschränkt auf Gebietskörperschaften


# **find_all**
> PageDvDataDto find_all()

Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten

Liefert Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten.

### Example


```python
import time
from deutschland import digitale_verwaltung
from deutschland.digitale_verwaltung.api import data_api
from deutschland.digitale_verwaltung.model.page_dv_data_dto import PageDvDataDto
from pprint import pprint
# Defining the host is optional and defaults to https://dashboard-daten.digitale-verwaltung.de/api
# See configuration.py for a list of all supported configuration parameters.
configuration = digitale_verwaltung.Configuration(
    host = "https://dashboard-daten.digitale-verwaltung.de/api"
)


# Enter a context with an instance of the API client
with digitale_verwaltung.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)
    order = "asc" # str | Gibt an, wie die Ergebnismenge sortiert werden soll. (optional) if omitted the server will use the default value of "asc"
    page = "0" # str | Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. (optional) if omitted the server will use the default value of "0"
    size = "100" # str | Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. (optional) if omitted the server will use the default value of "100"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten
        api_response = api_instance.find_all(order=order, page=page, size=size)
        pprint(api_response)
    except digitale_verwaltung.ApiException as e:
        print("Exception when calling DataApi->find_all: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Gibt an, wie die Ergebnismenge sortiert werden soll. | [optional] if omitted the server will use the default value of "asc"
 **page** | **str**| Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. | [optional] if omitted the server will use the default value of "0"
 **size** | **str**| Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. | [optional] if omitted the server will use the default value of "100"

### Return type

[**PageDvDataDto**](PageDvDataDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_filter**
> find_by_filter(ars)

Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten eingeschränkt auf Gebietskörperschaften

Liefert Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten eingeschränkt auf Gebietskörperschaften.

### Example


```python
import time
from deutschland import digitale_verwaltung
from deutschland.digitale_verwaltung.api import data_api
from pprint import pprint
# Defining the host is optional and defaults to https://dashboard-daten.digitale-verwaltung.de/api
# See configuration.py for a list of all supported configuration parameters.
configuration = digitale_verwaltung.Configuration(
    host = "https://dashboard-daten.digitale-verwaltung.de/api"
)


# Enter a context with an instance of the API client
with digitale_verwaltung.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = data_api.DataApi(api_client)
    ars = "010510000000" # str | Gibt den 12-stelligen amtlichen Regionalschlüssel einer Gebietskörperschaft an.
    filetype = "csv" # str | Gibt an, in welchem Dateiformat (CSV, XLSX) die Ergebnismenge zurückgegeben werden soll. (optional) if omitted the server will use the default value of "csv"
    order = "asc" # str | Gibt an, wie die Ergebnismenge sortiert werden soll. (optional) if omitted the server will use the default value of "asc"
    page = "0" # str | Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. (optional) if omitted the server will use the default value of "0"
    size = "100" # str | Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. (optional) if omitted the server will use the default value of "100"
    include_above = "true" # str | Gibt an, ob OZG-Leistungen auf darüberliegenden Gebietskörperschaften mit in der Ergebnismenge enthalten sein sollen. (optional) if omitted the server will use the default value of "true"
    include_below = "true" # str | Gibt an, ob OZG-Leistungen auf darunterliegenden Gebietskörperschaften mit in der Ergebnismenge enthalten sein sollen. (optional) if omitted the server will use the default value of "true"

    # example passing only required values which don't have defaults set
    try:
        # Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten eingeschränkt auf Gebietskörperschaften
        api_instance.find_by_filter(ars)
    except digitale_verwaltung.ApiException as e:
        print("Exception when calling DataApi->find_by_filter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Informationen zu OZG-Leistungen und deren zugehörigen Onlinediensten eingeschränkt auf Gebietskörperschaften
        api_instance.find_by_filter(ars, filetype=filetype, order=order, page=page, size=size, include_above=include_above, include_below=include_below)
    except digitale_verwaltung.ApiException as e:
        print("Exception when calling DataApi->find_by_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ars** | **str**| Gibt den 12-stelligen amtlichen Regionalschlüssel einer Gebietskörperschaft an. |
 **filetype** | **str**| Gibt an, in welchem Dateiformat (CSV, XLSX) die Ergebnismenge zurückgegeben werden soll. | [optional] if omitted the server will use the default value of "csv"
 **order** | **str**| Gibt an, wie die Ergebnismenge sortiert werden soll. | [optional] if omitted the server will use the default value of "asc"
 **page** | **str**| Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. | [optional] if omitted the server will use the default value of "0"
 **size** | **str**| Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. | [optional] if omitted the server will use the default value of "100"
 **include_above** | **str**| Gibt an, ob OZG-Leistungen auf darüberliegenden Gebietskörperschaften mit in der Ergebnismenge enthalten sein sollen. | [optional] if omitted the server will use the default value of "true"
 **include_below** | **str**| Gibt an, ob OZG-Leistungen auf darunterliegenden Gebietskörperschaften mit in der Ergebnismenge enthalten sein sollen. | [optional] if omitted the server will use the default value of "true"

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

