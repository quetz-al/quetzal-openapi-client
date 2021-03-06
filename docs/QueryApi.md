# quetzal.openapi_client.QueryApi

All URIs are relative to *https://api.quetz.al/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_query_create**](QueryApi.md#public_query_create) | **POST** /data/queries/ | Prepare a query.
[**public_query_details**](QueryApi.md#public_query_details) | **GET** /data/queries/{qid} | Query details.
[**public_query_fetch**](QueryApi.md#public_query_fetch) | **GET** /data/queries/ | List public queries.
[**workspace_query_create**](QueryApi.md#workspace_query_create) | **POST** /data/workspaces/{wid}/queries/ | Prepare a query.
[**workspace_query_details**](QueryApi.md#workspace_query_details) | **GET** /data/workspaces/{wid}/queries/{qid} | Query details.
[**workspace_query_fetch**](QueryApi.md#workspace_query_fetch) | **GET** /data/workspaces/{wid}/queries/ | List queries.


# **public_query_create**
> Query public_query_create(query, page=page, per_page=per_page)

Prepare a query.

Queries in Quetzal are saved as a resource, in this case, associated with the global workspace. This endpoint creates one and responds with a *see other* status referencing the query details endpoint.  Since the query details contains the query results as a paginated list, this endpoint also accepts the normal pagination parameters.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
query = quetzal.openapi_client.Query() # Query | 
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Prepare a query.
    api_response = api_instance.public_query_create(query, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_create: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
query = quetzal.openapi_client.Query() # Query | 
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Prepare a query.
    api_response = api_instance.public_query_create(query, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**Query**](Query.md)|  | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**Query**](Query.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_query_details**
> Query public_query_details(qid, page=page, per_page=per_page)

Query details.

The details of a query, which contains the query itself and a paginated list of its results.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
qid = 56 # int | Query identifier
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Query details.
    api_response = api_instance.public_query_details(qid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_details: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
qid = 56 # int | Query identifier
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Query details.
    api_response = api_instance.public_query_details(qid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **int**| Query identifier | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**Query**](Query.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_query_fetch**
> PaginatedQueries public_query_fetch(page=page, per_page=per_page)

List public queries.

List all the queries that are associated with the global workspace. Note that each query listed here is shown _without_ its results, for brevity.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # List public queries.
    api_response = api_instance.public_query_fetch(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_fetch: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # List public queries.
    api_response = api_instance.public_query_fetch(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->public_query_fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**PaginatedQueries**](PaginatedQueries.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_query_create**
> Query workspace_query_create(wid, query, page=page, per_page=per_page)

Prepare a query.

Queries in Quetzal are saved as a resource associated to a workspace. This endpoint creates one and responds with a *see other* status referencing the query details endpoint.  Since the query details contains the query results as a paginated list, this endpoint also accepts the normal pagination parameters.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
query = quetzal.openapi_client.Query() # Query | 
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Prepare a query.
    api_response = api_instance.workspace_query_create(wid, query, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_create: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
query = quetzal.openapi_client.Query() # Query | 
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Prepare a query.
    api_response = api_instance.workspace_query_create(wid, query, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **int**| Workspace identifier. | 
 **query** | [**Query**](Query.md)|  | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**Query**](Query.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_query_details**
> Query workspace_query_details(wid, qid, page=page, per_page=per_page)

Query details.

The details of a query, which contains the query itself and a paginated list of its results.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
qid = 56 # int | Query identifier
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Query details.
    api_response = api_instance.workspace_query_details(wid, qid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_details: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
qid = 56 # int | Query identifier
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # Query details.
    api_response = api_instance.workspace_query_details(wid, qid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **int**| Workspace identifier. | 
 **qid** | **int**| Query identifier | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**Query**](Query.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_query_fetch**
> PaginatedQueries workspace_query_fetch(wid, page=page, per_page=per_page)

List queries.

List all the queries that are associated with a workspace. Note that each query listed here is shown _without_ its results, for brevity.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # List queries.
    api_response = api_instance.workspace_query_fetch(wid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_fetch: %s\n" % e)
```

* Bearer Authentication (bearer):
```python
from __future__ import print_function
import time
import quetzal.openapi_client
from quetzal.openapi_client.rest import ApiException
from pprint import pprint
configuration = quetzal.openapi_client.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'
configuration = quetzal.openapi_client.Configuration()
# Configure Bearer authorization: bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# create an instance of the API class
api_instance = quetzal.openapi_client.QueryApi(quetzal.openapi_client.ApiClient(configuration))
wid = 56 # int | Workspace identifier.
page = 1 # int | The page of a collection to return. (optional) (default to 1)
per_page = 100 # int | Number of items to return per page. (optional) (default to 100)

try:
    # List queries.
    api_response = api_instance.workspace_query_fetch(wid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryApi->workspace_query_fetch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wid** | **int**| Workspace identifier. | 
 **page** | **int**| The page of a collection to return. | [optional] [default to 1]
 **per_page** | **int**| Number of items to return per page. | [optional] [default to 100]

### Return type

[**PaginatedQueries**](PaginatedQueries.md)

### Authorization

[apiKey](../README.md#apiKey), [bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

