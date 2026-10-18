from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.persistent_pty_info_status import PersistentPtyInfoStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_info_output import PersistentPtyInfoOutput
  from ..models.persistent_pty_info_size import PersistentPtyInfoSize





T = TypeVar("T", bound="PersistentPtyInfo")



@_attrs_define
class PersistentPtyInfo:
    """ 
        Attributes:
            args (list[str]):
            command (str):
            cwd (str):
            foreground_process (None | str):
            id (str):
            output (PersistentPtyInfoOutput):
            pid (int):
            session_id (str):
            size (PersistentPtyInfoSize):
            status (PersistentPtyInfoStatus):
            title (str):
            exit_code (int | Unset):
     """

    args: list[str]
    command: str
    cwd: str
    foreground_process: None | str
    id: str
    output: PersistentPtyInfoOutput
    pid: int
    session_id: str
    size: PersistentPtyInfoSize
    status: PersistentPtyInfoStatus
    title: str
    exit_code: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_info_output import PersistentPtyInfoOutput # noqa: PLC0415
        from ..models.persistent_pty_info_size import PersistentPtyInfoSize # noqa: PLC0415
        args = self.args



        command = self.command

        cwd = self.cwd

        foreground_process: None | str
        foreground_process = self.foreground_process

        id = self.id

        output = self.output.to_dict()

        pid = self.pid

        session_id = self.session_id

        size = self.size.to_dict()

        status = self.status.value

        title = self.title

        exit_code = self.exit_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "args": args,
            "command": command,
            "cwd": cwd,
            "foregroundProcess": foreground_process,
            "id": id,
            "output": output,
            "pid": pid,
            "sessionID": session_id,
            "size": size,
            "status": status,
            "title": title,
        })
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_info_output import PersistentPtyInfoOutput # noqa: PLC0415
        from ..models.persistent_pty_info_size import PersistentPtyInfoSize # noqa: PLC0415
        d = dict(src_dict)
        args = cast(list[str], d.pop("args"))


        command = d.pop("command")

        cwd = d.pop("cwd")

        def _parse_foreground_process(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        foreground_process = _parse_foreground_process(d.pop("foregroundProcess"))


        id = d.pop("id")

        output = PersistentPtyInfoOutput.from_dict(d.pop("output"))




        pid = d.pop("pid")

        session_id = d.pop("sessionID")

        size = PersistentPtyInfoSize.from_dict(d.pop("size"))




        status = PersistentPtyInfoStatus(d.pop("status"))




        title = d.pop("title")

        exit_code = d.pop("exitCode", UNSET)

        persistent_pty_info = cls(
            args=args,
            command=command,
            cwd=cwd,
            foreground_process=foreground_process,
            id=id,
            output=output,
            pid=pid,
            session_id=session_id,
            size=size,
            status=status,
            title=title,
            exit_code=exit_code,
        )

        return persistent_pty_info

