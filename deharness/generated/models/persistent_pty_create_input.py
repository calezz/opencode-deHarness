from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_create_input_env import PersistentPtyCreateInputEnv
  from ..models.persistent_pty_create_input_size import PersistentPtyCreateInputSize





T = TypeVar("T", bound="PersistentPtyCreateInput")



@_attrs_define
class PersistentPtyCreateInput:
    """ 
        Attributes:
            args (list[str]):
            env (PersistentPtyCreateInputEnv):
            title (str):
            command (str | Unset):
            cwd (str | Unset):
            size (PersistentPtyCreateInputSize | Unset):
     """

    args: list[str]
    env: PersistentPtyCreateInputEnv
    title: str
    command: str | Unset = UNSET
    cwd: str | Unset = UNSET
    size: PersistentPtyCreateInputSize | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_create_input_env import PersistentPtyCreateInputEnv # noqa: PLC0415
        from ..models.persistent_pty_create_input_size import PersistentPtyCreateInputSize # noqa: PLC0415
        args = self.args



        env = self.env.to_dict()

        title = self.title

        command = self.command

        cwd = self.cwd

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "args": args,
            "env": env,
            "title": title,
        })
        if command is not UNSET:
            field_dict["command"] = command
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_create_input_env import PersistentPtyCreateInputEnv # noqa: PLC0415
        from ..models.persistent_pty_create_input_size import PersistentPtyCreateInputSize # noqa: PLC0415
        d = dict(src_dict)
        args = cast(list[str], d.pop("args"))


        env = PersistentPtyCreateInputEnv.from_dict(d.pop("env"))




        title = d.pop("title")

        command = d.pop("command", UNSET)

        cwd = d.pop("cwd", UNSET)

        _size = d.pop("size", UNSET)
        size: PersistentPtyCreateInputSize | Unset
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = PersistentPtyCreateInputSize.from_dict(_size)




        persistent_pty_create_input = cls(
            args=args,
            env=env,
            title=title,
            command=command,
            cwd=cwd,
            size=size,
        )

        return persistent_pty_create_input

