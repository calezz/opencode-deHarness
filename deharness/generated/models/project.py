from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_commands import ProjectCommands
  from ..models.project_icon import ProjectIcon
  from ..models.project_time import ProjectTime





T = TypeVar("T", bound="Project")



@_attrs_define
class Project:
    """ 
        Attributes:
            canonical (str):
            id (str):
            sandboxes (list[str]):
            time (ProjectTime):
            commands (ProjectCommands | Unset):
            icon (ProjectIcon | Unset):
            name (str | Unset):
            vcs (str | Unset):
     """

    canonical: str
    id: str
    sandboxes: list[str]
    time: ProjectTime
    commands: ProjectCommands | Unset = UNSET
    icon: ProjectIcon | Unset = UNSET
    name: str | Unset = UNSET
    vcs: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_commands import ProjectCommands # noqa: PLC0415
        from ..models.project_icon import ProjectIcon # noqa: PLC0415
        from ..models.project_time import ProjectTime # noqa: PLC0415
        canonical = self.canonical

        id = self.id

        sandboxes = self.sandboxes



        time = self.time.to_dict()

        commands: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = self.commands.to_dict()

        icon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        name = self.name

        vcs = self.vcs


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "canonical": canonical,
            "id": id,
            "sandboxes": sandboxes,
            "time": time,
        })
        if commands is not UNSET:
            field_dict["commands"] = commands
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name
        if vcs is not UNSET:
            field_dict["vcs"] = vcs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_commands import ProjectCommands # noqa: PLC0415
        from ..models.project_icon import ProjectIcon # noqa: PLC0415
        from ..models.project_time import ProjectTime # noqa: PLC0415
        d = dict(src_dict)
        canonical = d.pop("canonical")

        id = d.pop("id")

        sandboxes = cast(list[str], d.pop("sandboxes"))


        time = ProjectTime.from_dict(d.pop("time"))




        _commands = d.pop("commands", UNSET)
        commands: ProjectCommands | Unset
        if isinstance(_commands,  Unset):
            commands = UNSET
        else:
            commands = ProjectCommands.from_dict(_commands)




        _icon = d.pop("icon", UNSET)
        icon: ProjectIcon | Unset
        if isinstance(_icon,  Unset):
            icon = UNSET
        else:
            icon = ProjectIcon.from_dict(_icon)




        name = d.pop("name", UNSET)

        vcs = d.pop("vcs", UNSET)

        project = cls(
            canonical=canonical,
            id=id,
            sandboxes=sandboxes,
            time=time,
            commands=commands,
            icon=icon,
            name=name,
            vcs=vcs,
        )

        return project

