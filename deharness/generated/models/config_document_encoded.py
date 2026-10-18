from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.config_document_encoded_type import ConfigDocumentEncodedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded import ConfigInfoEncoded





T = TypeVar("T", bound="ConfigDocumentEncoded")



@_attrs_define
class ConfigDocumentEncoded:
    """ 
        Attributes:
            info (ConfigInfoEncoded):
            type_ (ConfigDocumentEncodedType):
            path (str | Unset):
     """

    info: ConfigInfoEncoded
    type_: ConfigDocumentEncodedType
    path: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded import ConfigInfoEncoded # noqa: PLC0415
        info = self.info.to_dict()

        type_ = self.type_.value

        path = self.path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "info": info,
            "type": type_,
        })
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded import ConfigInfoEncoded # noqa: PLC0415
        d = dict(src_dict)
        info = ConfigInfoEncoded.from_dict(d.pop("info"))




        type_ = ConfigDocumentEncodedType(d.pop("type"))




        path = d.pop("path", UNSET)

        config_document_encoded = cls(
            info=info,
            type_=type_,
            path=path,
        )

        return config_document_encoded

