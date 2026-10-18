from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pty_status import PtyStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Pty")



@_attrs_define
class Pty:
    """ 
        Attributes:
            args (list[str]):
            command (str):
            cwd (str):
            id (str):
            pid (int):
            status (PtyStatus):
            title (str):
            exit_code (int | Unset):
     """

    args: list[str]
    command: str
    cwd: str
    id: str
    pid: int
    status: PtyStatus
    title: str
    exit_code: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        args = self.args



        command = self.command

        cwd = self.cwd

        id = self.id

        pid = self.pid

        status = self.status.value

        title = self.title

        exit_code = self.exit_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "args": args,
            "command": command,
            "cwd": cwd,
            "id": id,
            "pid": pid,
            "status": status,
            "title": title,
        })
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        args = cast(list[str], d.pop("args"))


        command = d.pop("command")

        cwd = d.pop("cwd")

        id = d.pop("id")

        pid = d.pop("pid")

        status = PtyStatus(d.pop("status"))




        title = d.pop("title")

        exit_code = d.pop("exitCode", UNSET)

        pty = cls(
            args=args,
            command=command,
            cwd=cwd,
            id=id,
            pid=pid,
            status=status,
            title=title,
            exit_code=exit_code,
        )

        return pty

