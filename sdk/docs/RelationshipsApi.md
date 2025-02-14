# lusid.RelationshipsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipsApi.md#create_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships | [EXPERIMENTAL] Create Relationship
[**delete_relationship**](RelationshipsApi.md#delete_relationship) | **POST** /api/relationshipdefinitions/{scope}/{code}/relationships/$delete | [EXPERIMENTAL] Delete Relationship


# **create_relationship**
> CompleteRelationship create_relationship(scope, code, create_relationship_request, effective_at=effective_at)

[EXPERIMENTAL] Create Relationship

Create a relationship between two entity objects by their identifiers

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
api_instance = lusid.RelationshipsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the relationship
code = 'code_example' # str | The code of the relationship
create_relationship_request = {"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # CreateRelationshipRequest | The details of the relationship to create.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relationship should be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [EXPERIMENTAL] Create Relationship
    api_response = api_instance.create_relationship(scope, code, create_relationship_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipsApi->create_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **create_relationship_request** | [**CreateRelationshipRequest**](CreateRelationshipRequest.md)| The details of the relationship to create. | 
 **effective_at** | **str**| The effective datetime or cut label at which the relationship should be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**CompleteRelationship**](CompleteRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relationship**
> DeletedEntityResponse delete_relationship(scope, code, delete_relationship_request, effective_at=effective_at)

[EXPERIMENTAL] Delete Relationship

Delete a relationship between two entity objects represented by their identifiers

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
api_instance = lusid.RelationshipsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the relationship
code = 'code_example' # str | The code of the relationship
delete_relationship_request = {"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # DeleteRelationshipRequest | The details of the relationship to delete.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relationship should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [EXPERIMENTAL] Delete Relationship
    api_response = api_instance.delete_relationship(scope, code, delete_relationship_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipsApi->delete_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship | 
 **code** | **str**| The code of the relationship | 
 **delete_relationship_request** | [**DeleteRelationshipRequest**](DeleteRelationshipRequest.md)| The details of the relationship to delete. | 
 **effective_at** | **str**| The effective datetime or cut label at which the relationship should the deletion be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the relationship is deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

