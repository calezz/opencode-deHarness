from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pty_create_body_env import PtyCreateBodyEnv





T = TypeVar("T", bound="PtyCreateBody")



@_attrs_define
class PtyCreateBody:
    """ 
        Attributes:
            args (list[str] | Unset):
            command (str | Unset):
            cwd (str | Unset):
            env (PtyCreateBodyEnv | Unset):
            title (str | Unset):
     """

    args: list[str] | Unset = UNSET
    command: str | Unset = UNSET
    cwd: str | Unset = UNSET
    env: PtyCreateBodyEnv | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.pty_create_body_env import PtyCreateBodyEnv # noqa: PLC0415
        args: list[str] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args



        command = self.command

        cwd = self.cwd

        env: dict[str, Any] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if args is not UNSET:
            field_dict["args"] = args
        if command is not UNSET:
            field_dict["command"] = command
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env is not UNSET:
            field_dict["env"] = env
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pty_create_body_env import PtyCreateBodyEnv # noqa: PLC0415
        d = dict(src_dict)
        args = cast(list[str], d.pop("args", UNSET))


        command = d.pop("command", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env = d.pop("env", UNSET)
        env: PtyCreateBodyEnv | Unset
        if isinstance(_env,  Unset):
            env = UNSET
        else:
            env = PtyCreateBodyEnv.from_dict(_env)




        title = d.pop("title", UNSET)

        pty_create_body = cls(
            args=args,
            command=command,
            cwd=cwd,
            env=env,
            title=title,
        )

        return pty_create_body

