from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_lsp_server_encoded_env import ConfigLSPServerEncodedEnv
  from ..models.config_lsp_server_encoded_initialization import ConfigLSPServerEncodedInitialization





T = TypeVar("T", bound="ConfigLSPServerEncoded")



@_attrs_define
class ConfigLSPServerEncoded:
    """ 
        Attributes:
            command (list[str]):
            disabled (bool | Unset):
            env (ConfigLSPServerEncodedEnv | Unset):
            extensions (list[str] | Unset):
            initialization (ConfigLSPServerEncodedInitialization | Unset):
     """

    command: list[str]
    disabled: bool | Unset = UNSET
    env: ConfigLSPServerEncodedEnv | Unset = UNSET
    extensions: list[str] | Unset = UNSET
    initialization: ConfigLSPServerEncodedInitialization | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_lsp_server_encoded_env import ConfigLSPServerEncodedEnv # noqa: PLC0415
        from ..models.config_lsp_server_encoded_initialization import ConfigLSPServerEncodedInitialization # noqa: PLC0415
        command = self.command



        disabled = self.disabled

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        extensions: list[str] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions



        initialization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.initialization, Unset):
            initialization = self.initialization.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if env is not UNSET:
            field_dict["env"] = env
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if initialization is not UNSET:
            field_dict["initialization"] = initialization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_lsp_server_encoded_env import ConfigLSPServerEncodedEnv # noqa: PLC0415
        from ..models.config_lsp_server_encoded_initialization import ConfigLSPServerEncodedInitialization # noqa: PLC0415
        d = dict(src_dict)
        command = cast(list[str], d.pop("command"))


        disabled = d.pop("disabled", UNSET)

        _env = d.pop("env", UNSET)
        env: ConfigLSPServerEncodedEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = ConfigLSPServerEncodedEnv.from_dict(_env)




        extensions = cast(list[str], d.pop("extensions", UNSET))


        _initialization = d.pop("initialization", UNSET)
        initialization: ConfigLSPServerEncodedInitialization | Unset
        if isinstance(_initialization,  Unset):
            initialization = UNSET
        else:
            initialization = ConfigLSPServerEncodedInitialization.from_dict(_initialization)




        config_lsp_server_encoded = cls(
            command=command,
            disabled=disabled,
            env=env,
            extensions=extensions,
            initialization=initialization,
        )

        return config_lsp_server_encoded

