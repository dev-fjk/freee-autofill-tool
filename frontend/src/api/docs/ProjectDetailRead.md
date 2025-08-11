# ProjectDetailRead

Project詳細(Excelフォーマット情報を含む)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **number** | プロジェクトID | [default to undefined]
**project_name** | **string** | プロジェクト名 | [default to undefined]
**project_description** | **string** |  | [optional] [default to undefined]
**start_time** | **string** | 開始時間 | [default to undefined]
**end_time** | **string** | 終了時間 | [default to undefined]
**start_break_time** | **string** | 休憩開始時間 | [default to undefined]
**end_break_time** | **string** | 休憩終了時間 | [default to undefined]
**update_key** | **number** | 更新キー（0〜9999） | [default to undefined]
**created_at** | **string** | 作成日時 | [default to undefined]
**created_by** | **string** | 作成者 | [default to undefined]
**updated_at** | **string** | 更新日時 | [default to undefined]
**updated_by** | **string** | 更新者 | [default to undefined]
**excel_format** | [**ProjectExcelFormatRead**](ProjectExcelFormatRead.md) |  | [optional] [default to undefined]

## Example

```typescript
import { ProjectDetailRead } from './api';

const instance: ProjectDetailRead = {
    project_id,
    project_name,
    project_description,
    start_time,
    end_time,
    start_break_time,
    end_break_time,
    update_key,
    created_at,
    created_by,
    updated_at,
    updated_by,
    excel_format,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
