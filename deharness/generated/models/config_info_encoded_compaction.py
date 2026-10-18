from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded_compaction_keep import ConfigInfoEncodedCompactionKeep





T = TypeVar("T", bound="ConfigInfoEncodedCompaction")



@_attrs_define
class ConfigInfoEncodedCompaction:
    """ 
        Attributes:
            auto (bool | Unset):
            buffer (int | Unset):
            keep (ConfigInfoEncodedCompactionKeep | Unset):
     """

    auto: bool | Unset = UNSET
    buffer: int | Unset = UNSET
    keep: ConfigInfoEncodedCompactionKeep | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded_compaction_keep import ConfigInfoEncodedCompactionKeep # noqa: PLC0415
        auto = self.auto

        buffer = self.buffer

        keep: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keep, Unset):
            keep = self.keep.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auto is not UNSET:
            field_dict["auto"] = auto
        if buffer is not UNSET:
            field_dict["buffer"] = buffer
        if keep is not UNSET:
            field_dict["keep"] = keep

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded_compaction_keep import ConfigInfoEncodedCompactionKeep # noqa: PLC0415
        d = dict(src_dict)
        auto = d.pop("auto", UNSET)

        buffer = d.pop("buffer", UNSET)

        _keep = d.pop("keep", UNSET)
        keep: ConfigInfoEncodedCompactionKeep | Unset
        if isinstance(_keep,  Unset):
            keep = UNSET
        else:
            keep = ConfigInfoEncodedCompactionKeep.from_dict(_keep)




        config_info_encoded_compaction = cls(
            auto=auto,
            buffer=buffer,
            keep=keep,
        )

        return config_info_encoded_compaction

