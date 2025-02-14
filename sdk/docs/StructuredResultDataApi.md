# lusid.StructuredResultDataApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_map**](StructuredResultDataApi.md#create_data_map) | **POST** /api/unitresults/datamap/{scope} | [EXPERIMENTAL] Upsert a set of structured result address definition maps. This creates or updates the data in Lusid.
[**delete_structured_result_data**](StructuredResultDataApi.md#delete_structured_result_data) | **POST** /api/unitresults/{scope}/$delete | [EXPERIMENTAL] Delete one or more items of structured result data, assuming they are present.
[**get_data_map**](StructuredResultDataApi.md#get_data_map) | **POST** /api/unitresults/datamap/{scope}/$get | [EXPERIMENTAL] Get the result address definition maps from the store
[**get_structured_result_data**](StructuredResultDataApi.md#get_structured_result_data) | **POST** /api/unitresults/{scope}/$get | [EXPERIMENTAL] Get structured result data
[**upsert_structured_result_data**](StructuredResultDataApi.md#upsert_structured_result_data) | **POST** /api/unitresults/{scope} | [EXPERIMENTAL] Upsert a set of structured result data items. This creates or updates the data in Lusid.


# **create_data_map**
> UpsertStructuredDataResponse create_data_map(scope, request_body)

[EXPERIMENTAL] Upsert a set of structured result address definition maps. This creates or updates the data in Lusid.

Create one or more structured result address definition map items in a single scope. These are immutable and cannot be changed once inserted                In the request each data map item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each structured result data in the response.                The response will return both the collection of successfully updated or inserted data maps, as well as those that failed.  For the failures a reason will be provided explaining why the item could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.StructuredResultDataApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope in which to upsert the result address definition maps
request_body = {} # dict(str, CreateDataMapRequest) | Individual result address definition map creation requests

try:
    # [EXPERIMENTAL] Upsert a set of structured result address definition maps. This creates or updates the data in Lusid.
    api_response = api_instance.create_data_map(scope, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredResultDataApi->create_data_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope in which to upsert the result address definition maps | 
 **request_body** | [**dict(str, CreateDataMapRequest)**](CreateDataMapRequest.md)| Individual result address definition map creation requests | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully created data maps along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_structured_result_data**
> AnnulStructuredDataResponse delete_structured_result_data(scope, request_body)

[EXPERIMENTAL] Delete one or more items of structured result data, assuming they are present.

Delete one or more specified structured result data items from a single scope. Each item is identified by a unique id which includes  information about its type as well as the exact effective datetime (to the microsecond) at which it entered the system (became valid).                In the request each market data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each quote in the response.                The response will return both the collection of successfully deleted market data items, as well as those that failed.  For the failures a reason will be provided explaining why the it could not be deleted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.StructuredResultDataApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the structured result data to delete.
request_body = {"someCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # dict(str, StructuredResultDataId) | The structured result data Ids to delete, each keyed by a unique correlation id.

try:
    # [EXPERIMENTAL] Delete one or more items of structured result data, assuming they are present.
    api_response = api_instance.delete_structured_result_data(scope, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredResultDataApi->delete_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the structured result data to delete. | 
 **request_body** | [**dict(str, StructuredResultDataId)**](StructuredResultDataId.md)| The structured result data Ids to delete, each keyed by a unique correlation id. | 

### Return type

[**AnnulStructuredDataResponse**](AnnulStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully deleted result data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_map**
> GetDataMapResponse get_data_map(scope, request_body)

[EXPERIMENTAL] Get the result address definition maps from the store

Get one or more result address definition map from a single scope.                Each item can be identified by its invariant Data Map key, which can be thought of as a permanent URL.                For each id LUSID will return the most recent matched item.                In the request each structured result data id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each item in the response.                The response will return three collections. One, the successfully retrieved structured result data. Two, those that had a  valid identifier but could not be found. Three, those that failed because LUSID could not construct a valid identifier from the request.                For the ids that failed to resolve or could not be found a reason will be provided explaining why that is the case.                It is important to always check the failed and not found sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.StructuredResultDataApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the result address definition map keys
request_body = {} # dict(str, DataMapKey) | The result address definition map keys to lookup

try:
    # [EXPERIMENTAL] Get the result address definition maps from the store
    api_response = api_instance.get_data_map(scope, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredResultDataApi->get_data_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the result address definition map keys | 
 **request_body** | [**dict(str, DataMapKey)**](DataMapKey.md)| The result address definition map keys to lookup | 

### Return type

[**GetDataMapResponse**](GetDataMapResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved data maps along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_structured_result_data**
> GetStructuredResultDataResponse get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)

[EXPERIMENTAL] Get structured result data

Get one or more items of structured result data from a single scope.                Each item can be identified by its time invariant structured result data identifier.                For each id LUSID will return the most recent matched item with respect to the provided (or default) effective datetime.                 An optional maximum age range window can be specified which defines how far back to look back for data from the specified effective datetime.  LUSID will return the most recent item within this window.                In the request each structured result data id must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each item in the response.                The response will return three collections. One, the successfully retrieved structured result data. Two, those that had a  valid identifier but could not be found. Three, those that failed because LUSID could not construct a valid identifier from the request.    For the ids that failed to resolve or could not be found a reason will be provided explaining why that is the case.                It is important to always check the failed and not found sets for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.StructuredResultDataApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the structured result data to retrieve.
request_body = {"someCorrelationId1":{"source":"MiddleOffice","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"}} # dict(str, StructuredResultDataId) | The time invariant set of structured data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the structured result data. Defaults to return the latest version if not specified. (optional)
max_age = 'max_age_example' # str | The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a structured result data item must exist to be retrieved. (optional)

try:
    # [EXPERIMENTAL] Get structured result data
    api_response = api_instance.get_structured_result_data(scope, request_body, as_at=as_at, max_age=max_age)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredResultDataApi->get_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the structured result data to retrieve. | 
 **request_body** | [**dict(str, StructuredResultDataId)**](StructuredResultDataId.md)| The time invariant set of structured data identifiers to retrieve the data for. These need to be               keyed by a unique correlation id allowing the retrieved item to be identified in the response. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the structured result data. Defaults to return the latest version if not specified. | [optional] 
 **max_age** | **str**| The duration of the look back window in an ISO8601 time interval format e.g. P1Y2M3DT4H30M (1 year, 2 months, 3 days, 4 hours and 30 minutes).               This is subtracted from the provided effectiveAt datetime to generate a effective datetime window inside which a structured result data item must exist to be retrieved. | [optional] 

### Return type

[**GetStructuredResultDataResponse**](GetStructuredResultDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved structured result data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_structured_result_data**
> UpsertStructuredDataResponse upsert_structured_result_data(scope, request_body)

[EXPERIMENTAL] Upsert a set of structured result data items. This creates or updates the data in Lusid.

Update or insert one or more structured result data items in a single scope. An item will be updated if it already exists  and inserted if it does not.                In the request each structured result data item must be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID.  It serves only as a way to easily identify each structured result data in the response.                The response will return both the collection of successfully updated or inserted structured result data, as well as those that failed.  For the failures a reason will be provided explaining why the item could not be updated or inserted.                It is important to always check the failed set for any unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.StructuredResultDataApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope to use when updating or inserting the structured result data.
request_body = {"first-item":{"id":{"source":"Client","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Xml","version":"1.0.0","name":"free text identifier of document 1","document":"<xml>data</xml>"}},"second-item":{"id":{"source":"Client","code":"MyUploadedRiskResults","effectiveAt":"2018-03-05T00:00:00.0000000+00:00","resultType":"Risk"},"data":{"documentFormat":"Json","version":"1.0.0","name":"free text identifier of document 2","document":"{ \"some\":\"valid json\"}"}}} # dict(str, UpsertStructuredResultDataRequest) | The set of structured result data items to update or insert keyed by a unique correlation id.

try:
    # [EXPERIMENTAL] Upsert a set of structured result data items. This creates or updates the data in Lusid.
    api_response = api_instance.upsert_structured_result_data(scope, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StructuredResultDataApi->upsert_structured_result_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the structured result data. | 
 **request_body** | [**dict(str, UpsertStructuredResultDataRequest)**](UpsertStructuredResultDataRequest.md)| The set of structured result data items to update or insert keyed by a unique correlation id. | 

### Return type

[**UpsertStructuredDataResponse**](UpsertStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted result data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

