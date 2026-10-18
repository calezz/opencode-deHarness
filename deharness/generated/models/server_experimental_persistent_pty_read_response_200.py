from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_read_result import PersistentPtyReadResult





T = TypeVar("T", bound="ServerExperimentalPersistentPtyReadResponse200")



@_attrs_define
class ServerExperimentalPersistentPtyReadResponse200:
    """ 
        Attributes:
            data (None | PersistentPtyReadResult):
     """

    data: None | PersistentPtyReadResult





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_read_result import PersistentPtyReadResult # noqa: PLC0415
        data: dict[str, Any] | None
        if isinstance(self.data, PersistentPtyReadResult):
            data = self.data.to_dict()
        else:
            data = self.data


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_read_result import PersistentPtyReadResult # noqa: PLC0415
        d = dict(src_dict)
        def _parse_data(data: object) -> None | PersistentPtyReadResult:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = PersistentPtyReadResult.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersistentPtyReadResult, data)

        data = _parse_data(d.pop("data"))


        server_experimental_persistent_pty_read_response_200 = cls(
            data=data,
        )

        return server_experimental_persistent_pty_read_response_200

