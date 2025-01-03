from typing import Any
from typing_extensions import Self

__tracebackhide__: bool

class DictMixin:
    def contains_key(self, *keys: Any) -> Self: ...
    def does_not_contain_key(self, *keys: Any) -> Self: ...
    def contains_value(self, *values: Any) -> Self: ...
    def does_not_contain_value(self, *values: Any) -> Self: ...
    def contains_entry(self, *args: Any, **kwargs: dict[str, Any]) -> Self: ...
    def does_not_contain_entry(self, *args: Any, **kwargs: dict[str, Any]) -> Self: ...
