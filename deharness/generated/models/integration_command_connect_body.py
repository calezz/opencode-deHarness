from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IntegrationCommandConnectBody")



@_attrs_define
class IntegrationCommandConnectBody:
    """ 
        Attributes:
            method_id (str):
            label (None | str | Unset):
     """

    method_id: str
    label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        method_id = self.method_id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "methodID": method_id,
        })
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_id = d.pop("methodID")

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        integration_command_connect_body = cls(
            method_id=method_id,
            label=label,
        )

        return integration_command_connect_body

