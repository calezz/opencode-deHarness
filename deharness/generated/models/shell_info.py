from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.shell_info_status import ShellInfoStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shell_info_metadata import ShellInfoMetadata
  from ..models.shell_info_time import ShellInfoTime





T = TypeVar("T", bound="ShellInfo")



@_attrs_define
class ShellInfo:
    """ 
        Attributes:
            command (str):
            cwd (str):
            file (str):
            id (str):
            metadata (ShellInfoMetadata):
            shell (str):
            status (ShellInfoStatus):
            time (ShellInfoTime):
            exit_ (float | Unset):
            pid (int | Unset):
            signal (str | Unset):
     """

    command: str
    cwd: str
    file: str
    id: str
    metadata: ShellInfoMetadata
    shell: str
    status: ShellInfoStatus
    time: ShellInfoTime
    exit_: float | Unset = UNSET
    pid: int | Unset = UNSET
    signal: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.shell_info_metadata import ShellInfoMetadata # noqa: PLC0415
        from ..models.shell_info_time import ShellInfoTime # noqa: PLC0415
        command = self.command

        cwd = self.cwd

        file = self.file

        id = self.id

        metadata = self.metadata.to_dict()

        shell = self.shell

        status = self.status.value

        time = self.time.to_dict()

        exit_ = self.exit_

        pid = self.pid

        signal = self.signal


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
            "cwd": cwd,
            "file": file,
            "id": id,
            "metadata": metadata,
            "shell": shell,
            "status": status,
            "time": time,
        })
        if exit_ is not UNSET:
            field_dict["exit"] = exit_
        if pid is not UNSET:
            field_dict["pid"] = pid
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shell_info_metadata import ShellInfoMetadata # noqa: PLC0415
        from ..models.shell_info_time import ShellInfoTime # noqa: PLC0415
        d = dict(src_dict)
        command = d.pop("command")

        cwd = d.pop("cwd")

        file = d.pop("file")

        id = d.pop("id")

        metadata = ShellInfoMetadata.from_dict(d.pop("metadata"))




        shell = d.pop("shell")

        status = ShellInfoStatus(d.pop("status"))




        time = ShellInfoTime.from_dict(d.pop("time"))




        exit_ = d.pop("exit", UNSET)

        pid = d.pop("pid", UNSET)

        signal = d.pop("signal", UNSET)

        shell_info = cls(
            command=command,
            cwd=cwd,
            file=file,
            id=id,
            metadata=metadata,
            shell=shell,
            status=status,
            time=time,
            exit_=exit_,
            pid=pid,
            signal=signal,
        )

        return shell_info

