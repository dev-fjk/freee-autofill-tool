# ProjectApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createProject**](#createproject) | **POST** /projects | プロジェクト作成|
|[**deleteProject**](#deleteproject) | **DELETE** /projects/{project_id} | プロジェクト削除|
|[**getProjectDetail**](#getprojectdetail) | **GET** /projects/{project_id} | プロジェクト詳細取得|
|[**getProjects**](#getprojects) | **GET** /projects | プロジェクト一覧取得|
|[**updateProject**](#updateproject) | **PUT** /projects/{project_id} | プロジェクト更新|

# **createProject**
> ProjectRead createProject(projectCreate)

新しいプロジェクトを登録する

### Example

```typescript
import {
    ProjectApi,
    Configuration,
    ProjectCreate
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectApi(configuration);

let projectCreate: ProjectCreate; //
let xEmployeeId: string; //社員ID (例: e024) (optional) (default to 'e024')
let xRole: string; //権限 (user または admin) (optional) (default to 'user')

const { status, data } = await apiInstance.createProject(
    projectCreate,
    xEmployeeId,
    xRole
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectCreate** | **ProjectCreate**|  | |
| **xEmployeeId** | [**string**] | 社員ID (例: e024) | (optional) defaults to 'e024'|
| **xRole** | [**string**] | 権限 (user または admin) | (optional) defaults to 'user'|


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

# **deleteProject**
> deleteProject()

指定IDのプロジェクトを削除します。update_keyが一致しない場合はエラーになります。

### Example

```typescript
import {
    ProjectApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let updateKey: number; //更新キー（0〜9999） (default to undefined)
let xEmployeeId: string; //社員ID (例: e024) (optional) (default to 'e024')
let xRole: string; //権限 (user または admin) (optional) (default to 'user')

const { status, data } = await apiInstance.deleteProject(
    projectId,
    updateKey,
    xEmployeeId,
    xRole
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **updateKey** | [**number**] | 更新キー（0〜9999） | defaults to undefined|
| **xEmployeeId** | [**string**] | 社員ID (例: e024) | (optional) defaults to 'e024'|
| **xRole** | [**string**] | 権限 (user または admin) | (optional) defaults to 'user'|


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

# **getProjectDetail**
> ProjectDetailRead getProjectDetail()

プロジェクトIDで詳細取得

### Example

```typescript
import {
    ProjectApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let xEmployeeId: string; //社員ID (例: e024) (optional) (default to 'e024')
let xRole: string; //権限 (user または admin) (optional) (default to 'user')

const { status, data } = await apiInstance.getProjectDetail(
    projectId,
    xEmployeeId,
    xRole
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **xEmployeeId** | [**string**] | 社員ID (例: e024) | (optional) defaults to 'e024'|
| **xRole** | [**string**] | 権限 (user または admin) | (optional) defaults to 'user'|


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

# **getProjects**
> PaginatedResponseProjectRead getProjects()

プロジェクトIDや名前で絞り込み・ページング対応

### Example

```typescript
import {
    ProjectApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectApi(configuration);

let projectId: number; // (optional) (default to undefined)
let projectName: string; // (optional) (default to undefined)
let pageNumber: number; // (optional) (default to 1)
let pageSize: number; // (optional) (default to 30)
let xEmployeeId: string; //社員ID (例: e024) (optional) (default to 'e024')
let xRole: string; //権限 (user または admin) (optional) (default to 'user')

const { status, data } = await apiInstance.getProjects(
    projectId,
    projectName,
    pageNumber,
    pageSize,
    xEmployeeId,
    xRole
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectId** | [**number**] |  | (optional) defaults to undefined|
| **projectName** | [**string**] |  | (optional) defaults to undefined|
| **pageNumber** | [**number**] |  | (optional) defaults to 1|
| **pageSize** | [**number**] |  | (optional) defaults to 30|
| **xEmployeeId** | [**string**] | 社員ID (例: e024) | (optional) defaults to 'e024'|
| **xRole** | [**string**] | 権限 (user または admin) | (optional) defaults to 'user'|


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

# **updateProject**
> ProjectRead updateProject(projectUpdate)

指定IDのプロジェクトを更新する

### Example

```typescript
import {
    ProjectApi,
    Configuration,
    ProjectUpdate
} from './api';

const configuration = new Configuration();
const apiInstance = new ProjectApi(configuration);

let projectId: number; //プロジェクトID (default to undefined)
let projectUpdate: ProjectUpdate; //
let xEmployeeId: string; //社員ID (例: e024) (optional) (default to 'e024')
let xRole: string; //権限 (user または admin) (optional) (default to 'user')

const { status, data } = await apiInstance.updateProject(
    projectId,
    projectUpdate,
    xEmployeeId,
    xRole
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **projectUpdate** | **ProjectUpdate**|  | |
| **projectId** | [**number**] | プロジェクトID | defaults to undefined|
| **xEmployeeId** | [**string**] | 社員ID (例: e024) | (optional) defaults to 'e024'|
| **xRole** | [**string**] | 権限 (user または admin) | (optional) defaults to 'user'|


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

