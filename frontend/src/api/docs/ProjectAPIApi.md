# ProjectAPIApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createNewProjectProjectsPost**](#createnewprojectprojectspost) | **POST** /projects | プロジェクト作成|
|[**deleteProjectProjectsProjectIdDelete**](#deleteprojectprojectsprojectiddelete) | **DELETE** /projects/{project_id} | プロジェクト削除|
|[**getProjectDetailProjectsProjectIdGet**](#getprojectdetailprojectsprojectidget) | **GET** /projects/{project_id} | プロジェクト詳細取得|
|[**getProjectsProjectsGet**](#getprojectsprojectsget) | **GET** /projects | プロジェクト一覧取得|
|[**updateExistingProjectProjectsProjectIdPut**](#updateexistingprojectprojectsprojectidput) | **PUT** /projects/{project_id} | プロジェクト更新|

# **createNewProjectProjectsPost**
> ProjectRead createNewProjectProjectsPost(projectCreate)

新しいプロジェクトを登録する

### Example

```typescript
import {
    ProjectAPIApi,
    Configuration,
    ProjectCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectAPIApi(configuration);

let projectCreate: ProjectCreate; //
let xEmployeeId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.createNewProjectProjectsPost(
    projectCreate,
    xEmployeeId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectCreate** | **ProjectCreate**|  | |
| **xEmployeeId** | [**string**] |  | (optional) defaults to undefined|


### Return type

**ProjectRead**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteProjectProjectsProjectIdDelete**
> deleteProjectProjectsProjectIdDelete()

指定IDのプロジェクトを削除します。update_keyが一致しない場合はエラーになります。

### Example

```typescript
import {
    ProjectAPIApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectAPIApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let updateKey: number; //更新キー（0〜9999） (default to undefined)
let xEmployeeId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.deleteProjectProjectsProjectIdDelete(
    projectId,
    updateKey,
    xEmployeeId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **updateKey** | [**number**] | 更新キー（0〜9999） | defaults to undefined|
| **xEmployeeId** | [**string**] |  | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getProjectDetailProjectsProjectIdGet**
> ProjectDetailRead getProjectDetailProjectsProjectIdGet()

プロジェクトIDで詳細取得

### Example

```typescript
import {
    ProjectAPIApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectAPIApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let xEmployeeId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.getProjectDetailProjectsProjectIdGet(
    projectId,
    xEmployeeId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **xEmployeeId** | [**string**] |  | (optional) defaults to undefined|


### Return type

**ProjectDetailRead**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getProjectsProjectsGet**
> PaginatedResponseProjectRead getProjectsProjectsGet()

プロジェクトIDや名前で絞り込み・ページング対応

### Example

```typescript
import {
    ProjectAPIApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectAPIApi(configuration);

let projectId: number; // (optional) (default to undefined)
let projectName: string; // (optional) (default to undefined)
let pageNumber: number; // (optional) (default to 1)
let pageSize: number; // (optional) (default to 30)
let xEmployeeId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.getProjectsProjectsGet(
    projectId,
    projectName,
    pageNumber,
    pageSize,
    xEmployeeId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] |  | (optional) defaults to undefined|
| **projectName** | [**string**] |  | (optional) defaults to undefined|
| **pageNumber** | [**number**] |  | (optional) defaults to 1|
| **pageSize** | [**number**] |  | (optional) defaults to 30|
| **xEmployeeId** | [**string**] |  | (optional) defaults to undefined|


### Return type

**PaginatedResponseProjectRead**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateExistingProjectProjectsProjectIdPut**
> ProjectRead updateExistingProjectProjectsProjectIdPut(projectUpdate)

指定IDのプロジェクトを更新する

### Example

```typescript
import {
    ProjectAPIApi,
    Configuration,
    ProjectUpdate
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectAPIApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let projectUpdate: ProjectUpdate; //
let xEmployeeId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.updateExistingProjectProjectsProjectIdPut(
    projectId,
    projectUpdate,
    xEmployeeId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectUpdate** | **ProjectUpdate**|  | |
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **xEmployeeId** | [**string**] |  | (optional) defaults to undefined|


### Return type

**ProjectRead**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

