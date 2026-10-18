from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_plugin_entry_encoded_options import ConfigPluginEntryEncodedOptions





T = TypeVar("T", bound="ConfigPluginEntryEncoded")



@_attrs_define
class ConfigPluginEntryEncoded:
    """ 
        Attributes:
            package (str):
            options (ConfigPluginEntryEncodedOptions | Unset):
     """

    package: str
    options: ConfigPluginEntryEncodedOptions | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_plugin_entry_encoded_options import ConfigPluginEntryEncodedOptions # noqa: PLC0415
        package = self.package

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "package": package,
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_plugin_entry_encoded_options import ConfigPluginEntryEncodedOptions # noqa: PLC0415
        d = dict(src_dict)
        package = d.pop("package")

        _options = d.pop("options", UNSET)
        options: ConfigPluginEntryEncodedOptions | Unset
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = ConfigPluginEntryEncodedOptions.from_dict(_options)




        config_plugin_entry_encoded = cls(
            package=package,
            options=options,
        )

        return config_plugin_entry_encoded

