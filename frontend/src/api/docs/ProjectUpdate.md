# ProjectUpdate

プロジェクト更新（PUT）用スキーマ。全項目必須で更新します。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **string** | プロジェクト名 | [default to undefined]
**project_description** | **string** |  | [optional] [default to undefined]
**start_time** | **string** | 開始時間 (HH:mm) | [default to undefined]
**end_time** | **string** | 終了時間 (HH:mm) | [default to undefined]
**start_break_time** | **string** | 休憩開始時間 (HH:mm) | [default to undefined]
**end_break_time** | **string** | 休憩終了時間 (HH:mm) | [default to undefined]
**update_key** | **number** | 更新キー（0〜9999） | [default to undefined]
**updated_by** | **string** | 更新者 | [default to undefined]

## Example

```typescript
import { ProjectUpdate } from './api';

const instance: ProjectUpdate = {
    project_name,
    project_description,
    start_time,
    end_time,
    start_break_time,
    end_break_time,
    update_key,
    updated_by,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
