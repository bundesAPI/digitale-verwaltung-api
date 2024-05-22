# digitale_verwaltung.ARSApi

All URIs are relative to *https://digitale-verwaltung.api.proxy.bund.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all1**](ARSApi.md#find_all1) | **GET** /v1/ars | Informationen zu Gebietskörperschaften in Deutschland


# **find_all1**
> PageArsDto find_all1()

Informationen zu Gebietskörperschaften in Deutschland

Liefert amtliche Regionalschlüssel und Bezeichnungen zu allen Gebietskörperschaften innerhalb Deutschlands.

### Example


```python
import time
from deutschland import digitale_verwaltung
from deutschland.digitale_verwaltung.api import ars_api
from deutschland.digitale_verwaltung.model.page_ars_dto import PageArsDto
from pprint import pprint
# Defining the host is optional and defaults to https://digitale-verwaltung.api.proxy.bund.dev/api
# See configuration.py for a list of all supported configuration parameters.
configuration = digitale_verwaltung.Configuration(
    host = "https://digitale-verwaltung.api.proxy.bund.dev/api"
)


# Enter a context with an instance of the API client
with digitale_verwaltung.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ars_api.ARSApi(api_client)
    order = "asc" # str | Gibt an, wie die Ergebnismenge sortiert werden soll. (optional) if omitted the server will use the default value of "asc"
    page = "0" # str | Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. (optional) if omitted the server will use the default value of "0"
    size = "100" # str | Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. (optional) if omitted the server will use the default value of "100"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Informationen zu Gebietskörperschaften in Deutschland
        api_response = api_instance.find_all1(order=order, page=page, size=size)
        pprint(api_response)
    except digitale_verwaltung.ApiException as e:
        print("Exception when calling ARSApi->find_all1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Gibt an, wie die Ergebnismenge sortiert werden soll. | [optional] if omitted the server will use the default value of "asc"
 **page** | **str**| Gibt an, welche Seite der Ergebnismenge zurückgegeben werden soll. Die erste Seite entspricht dem Wert 0. | [optional] if omitted the server will use the default value of "0"
 **size** | **str**| Gibt an, wie groß die Ergebnismenge für die abgefragte Seite maximal sein darf. | [optional] if omitted the server will use the default value of "100"

### Return type

[**PageArsDto**](PageArsDto.md)

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

