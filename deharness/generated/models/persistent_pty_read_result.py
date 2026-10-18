from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_read_result_screen import PersistentPtyReadResultScreen





T = TypeVar("T", bound="PersistentPtyReadResult")



@_attrs_define
class PersistentPtyReadResult:
    """ 
        Attributes:
            cwd (str):
            foreground_process (None | str):
            pty_id (str):
            screen (PersistentPtyReadResultScreen):
            title (str):
     """

    cwd: str
    foreground_process: None | str
    pty_id: str
    screen: PersistentPtyReadResultScreen
    title: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_read_result_screen import PersistentPtyReadResultScreen # noqa: PLC0415
        cwd = self.cwd

        foreground_process: None | str
        foreground_process = self.foreground_process

        pty_id = self.pty_id

        screen = self.screen.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cwd": cwd,
            "foregroundProcess": foreground_process,
            "ptyID": pty_id,
            "screen": screen,
            "title": title,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_read_result_screen import PersistentPtyReadResultScreen # noqa: PLC0415
        d = dict(src_dict)
        cwd = d.pop("cwd")

        def _parse_foreground_process(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        foreground_process = _parse_foreground_process(d.pop("foregroundProcess"))


        pty_id = d.pop("ptyID")

        screen = PersistentPtyReadResultScreen.from_dict(d.pop("screen"))




        title = d.pop("title")

        persistent_pty_read_result = cls(
            cwd=cwd,
            foreground_process=foreground_process,
            pty_id=pty_id,
            screen=screen,
            title=title,
        )

        return persistent_pty_read_result

