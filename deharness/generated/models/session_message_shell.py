from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_shell_exit_type_1 import SessionMessageShellExitType1
from ..models.session_message_shell_status import SessionMessageShellStatus
from ..models.session_message_shell_type import SessionMessageShellType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_shell_metadata import SessionMessageShellMetadata
  from ..models.session_message_shell_output import SessionMessageShellOutput
  from ..models.session_message_shell_time import SessionMessageShellTime





T = TypeVar("T", bound="SessionMessageShell")



@_attrs_define
class SessionMessageShell:
    """ 
        Attributes:
            command (str):
            id (str):
            shell_id (str):
            status (SessionMessageShellStatus):
            time (SessionMessageShellTime):
            type_ (SessionMessageShellType):
            exit_ (float | SessionMessageShellExitType1 | Unset):
            metadata (SessionMessageShellMetadata | Unset):
            output (SessionMessageShellOutput | Unset):
     """

    command: str
    id: str
    shell_id: str
    status: SessionMessageShellStatus
    time: SessionMessageShellTime
    type_: SessionMessageShellType
    exit_: float | SessionMessageShellExitType1 | Unset = UNSET
    metadata: SessionMessageShellMetadata | Unset = UNSET
    output: SessionMessageShellOutput | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_shell_metadata import SessionMessageShellMetadata # noqa: PLC0415
        from ..models.session_message_shell_output import SessionMessageShellOutput # noqa: PLC0415
        from ..models.session_message_shell_time import SessionMessageShellTime # noqa: PLC0415
        command = self.command

        id = self.id

        shell_id = self.shell_id

        status = self.status.value

        time = self.time.to_dict()

        type_ = self.type_.value

        exit_: float | str | Unset
        if isinstance(self.exit_, Unset):
            exit_ = UNSET
        elif isinstance(self.exit_, SessionMessageShellExitType1):
            exit_ = self.exit_.value
        else:
            exit_ = self.exit_

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
            "id": id,
            "shellID": shell_id,
            "status": status,
            "time": time,
            "type": type_,
        })
        if exit_ is not UNSET:
            field_dict["exit"] = exit_
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_shell_metadata import SessionMessageShellMetadata # noqa: PLC0415
        from ..models.session_message_shell_output import SessionMessageShellOutput # noqa: PLC0415
        from ..models.session_message_shell_time import SessionMessageShellTime # noqa: PLC0415
        d = dict(src_dict)
        command = d.pop("command")

        id = d.pop("id")

        shell_id = d.pop("shellID")

        status = SessionMessageShellStatus(d.pop("status"))




        time = SessionMessageShellTime.from_dict(d.pop("time"))




        type_ = SessionMessageShellType(d.pop("type"))




        def _parse_exit_(data: object) -> float | SessionMessageShellExitType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exit_type_1 = SessionMessageShellExitType1(data)



                return exit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | SessionMessageShellExitType1 | Unset, data)

        exit_ = _parse_exit_(d.pop("exit", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageShellMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageShellMetadata.from_dict(_metadata)




        _output = d.pop("output", UNSET)
        output: SessionMessageShellOutput | Unset
        if isinstance(_output,  Unset):
            output = UNSET
        else:
            output = SessionMessageShellOutput.from_dict(_output)




        session_message_shell = cls(
            command=command,
            id=id,
            shell_id=shell_id,
            status=status,
            time=time,
            type_=type_,
            exit_=exit_,
            metadata=metadata,
            output=output,
        )

        return session_message_shell

