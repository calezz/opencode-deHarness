from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.server_info_capabilities_type_0 import ServerInfoCapabilitiesType0
  from ..models.server_info_paths import ServerInfoPaths





T = TypeVar("T", bound="ServerInfo")



@_attrs_define
class ServerInfo:
    """ 
        Attributes:
            paths (ServerInfoPaths):
            pid (int):
            urls (list[str]):
            version (str):
            capabilities (None | ServerInfoCapabilitiesType0 | Unset):
     """

    paths: ServerInfoPaths
    pid: int
    urls: list[str]
    version: str
    capabilities: None | ServerInfoCapabilitiesType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.server_info_capabilities_type_0 import ServerInfoCapabilitiesType0 # noqa: PLC0415
        from ..models.server_info_paths import ServerInfoPaths # noqa: PLC0415
        paths = self.paths.to_dict()

        pid = self.pid

        urls = self.urls



        version = self.version

        capabilities: dict[str, Any] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, ServerInfoCapabilitiesType0):
            capabilities = self.capabilities.to_dict()
        else:
            capabilities = self.capabilities


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "paths": paths,
            "pid": pid,
            "urls": urls,
            "version": version,
        })
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_info_capabilities_type_0 import ServerInfoCapabilitiesType0 # noqa: PLC0415
        from ..models.server_info_paths import ServerInfoPaths # noqa: PLC0415
        d = dict(src_dict)
        paths = ServerInfoPaths.from_dict(d.pop("paths"))




        pid = d.pop("pid")

        urls = cast(list[str], d.pop("urls"))


        version = d.pop("version")

        def _parse_capabilities(data: object) -> None | ServerInfoCapabilitiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                capabilities_type_0 = ServerInfoCapabilitiesType0.from_dict(data)



                return capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ServerInfoCapabilitiesType0 | Unset, data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))


        server_info = cls(
            paths=paths,
            pid=pid,
            urls=urls,
            version=version,
            capabilities=capabilities,
        )

        return server_info

