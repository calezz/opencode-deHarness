from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="McpRemoteConfigEncodedTimeout")



@_attrs_define
class McpRemoteConfigEncodedTimeout:
    """ 
        Attributes:
            catalog (int | Unset):
            execution (int | Unset):
            startup (int | Unset):
     """

    catalog: int | Unset = UNSET
    execution: int | Unset = UNSET
    startup: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        catalog = self.catalog

        execution = self.execution

        startup = self.startup


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if catalog is not UNSET:
            field_dict["catalog"] = catalog
        if execution is not UNSET:
            field_dict["execution"] = execution
        if startup is not UNSET:
            field_dict["startup"] = startup

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog = d.pop("catalog", UNSET)

        execution = d.pop("execution", UNSET)

        startup = d.pop("startup", UNSET)

        mcp_remote_config_encoded_timeout = cls(
            catalog=catalog,
            execution=execution,
            startup=startup,
        )

        return mcp_remote_config_encoded_timeout

