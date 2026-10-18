from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_encoding import ProviderEncoding
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.provider_compaction_type_0 import ProviderCompactionType0
  from ..models.provider_compaction_type_1 import ProviderCompactionType1





T = TypeVar("T", bound="ConfigModelSettings")



@_attrs_define
class ConfigModelSettings:
    """ 
        Attributes:
            compaction (ProviderCompactionType0 | ProviderCompactionType1 | Unset):
            encoding (ProviderEncoding | Unset):
     """

    compaction: ProviderCompactionType0 | ProviderCompactionType1 | Unset = UNSET
    encoding: ProviderEncoding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_compaction_type_0 import ProviderCompactionType0 # noqa: PLC0415
        from ..models.provider_compaction_type_1 import ProviderCompactionType1 # noqa: PLC0415
        compaction: dict[str, Any] | Unset
        if isinstance(self.compaction, Unset):
            compaction = UNSET
        elif isinstance(self.compaction, ProviderCompactionType0):
            compaction = self.compaction.to_dict()
        else:
            compaction = self.compaction.to_dict()


        encoding: str | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compaction is not UNSET:
            field_dict["compaction"] = compaction
        if encoding is not UNSET:
            field_dict["encoding"] = encoding

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_compaction_type_0 import ProviderCompactionType0 # noqa: PLC0415
        from ..models.provider_compaction_type_1 import ProviderCompactionType1 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_compaction(data: object) -> ProviderCompactionType0 | ProviderCompactionType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_provider_compaction_type_0 = ProviderCompactionType0.from_dict(data)



                return componentsschemas_provider_compaction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_provider_compaction_type_1 = ProviderCompactionType1.from_dict(data)



            return componentsschemas_provider_compaction_type_1

        compaction = _parse_compaction(d.pop("compaction", UNSET))


        _encoding = d.pop("encoding", UNSET)
        encoding: ProviderEncoding | Unset
        if isinstance(_encoding,  Unset):
            encoding = UNSET
        else:
            encoding = ProviderEncoding(_encoding)




        config_model_settings = cls(
            compaction=compaction,
            encoding=encoding,
        )


        config_model_settings.additional_properties = d
        return config_model_settings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
