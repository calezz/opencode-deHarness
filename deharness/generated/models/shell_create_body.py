from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shell_create_body_metadata import ShellCreateBodyMetadata





T = TypeVar("T", bound="ShellCreateBody")



@_attrs_define
class ShellCreateBody:
    """ 
        Attributes:
            command (str):
            cwd (str | Unset):
            metadata (ShellCreateBodyMetadata | Unset):
            timeout (int | Unset):
     """

    command: str
    cwd: str | Unset = UNSET
    metadata: ShellCreateBodyMetadata | Unset = UNSET
    timeout: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.shell_create_body_metadata import ShellCreateBodyMetadata # noqa: PLC0415
        command = self.command

        cwd = self.cwd

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        timeout = self.timeout


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
        })
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shell_create_body_metadata import ShellCreateBodyMetadata # noqa: PLC0415
        d = dict(src_dict)
        command = d.pop("command")

        cwd = d.pop("cwd", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ShellCreateBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = ShellCreateBodyMetadata.from_dict(_metadata)




        timeout = d.pop("timeout", UNSET)

        shell_create_body = cls(
            command=command,
            cwd=cwd,
            metadata=metadata,
            timeout=timeout,
        )

        return shell_create_body

