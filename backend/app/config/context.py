import contextvars

request_id_ctx_var = contextvars.ContextVar("request_id", default="N/A")
request_info_ctx_var = contextvars.ContextVar("request_info", default={})
employee_id_ctx_var = contextvars.ContextVar("employee_id", default=None)
