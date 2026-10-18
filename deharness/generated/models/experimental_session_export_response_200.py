from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_transfer_data import SessionTransferData





T = TypeVar("T", bound="ExperimentalSessionExportResponse200")



@_attrs_define
class ExperimentalSessionExportResponse200:
    """ 
        Attributes:
            data (SessionTransferData):
     """

    data: SessionTransferData





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_transfer_data import SessionTransferData # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_transfer_data import SessionTransferData # noqa: PLC0415
        d = dict(src_dict)
        data = SessionTransferData.from_dict(d.pop("data"))




        experimental_session_export_response_200 = cls(
            data=data,
        )

        return experimental_session_export_response_200

