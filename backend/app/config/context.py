import contextvars

request_id_ctx_var = contextvars.ContextVar("request_id", default="N/A")
request_info_ctx_var = contextvars.ContextVar("request_info", default={})
role_ctx_var = contextvars.ContextVar("role", default=None)
employee_id_ctx_var = contextvars.ContextVar("employee_id", default=None)
