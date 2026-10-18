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





T = TypeVar("T", bound="ProjectUpdateBody")



@_attrs_define
class ProjectUpdateBody:
    """ 
        Attributes:
            canonical (str | Unset):
            commands (ProjectCommands | Unset):
            icon (ProjectIcon | Unset):
            name (str | Unset):
     """

    canonical: str | Unset = UNSET
    commands: ProjectCommands | Unset = UNSET
    icon: ProjectIcon | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_commands import ProjectCommands # noqa: PLC0415
        from ..models.project_icon import ProjectIcon # noqa: PLC0415
        canonical = self.canonical

        commands: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commands, Unset):
            commands = self.commands.to_dict()

        icon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if commands is not UNSET:
            field_dict["commands"] = commands
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_commands import ProjectCommands # noqa: PLC0415
        from ..models.project_icon import ProjectIcon # noqa: PLC0415
        d = dict(src_dict)
        canonical = d.pop("canonical", UNSET)

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

        project_update_body = cls(
            canonical=canonical,
            commands=commands,
            icon=icon,
            name=name,
        )

        return project_update_body

