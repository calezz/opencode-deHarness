from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_mention import PromptMention





T = TypeVar("T", bound="PromptInputFileAttachment")



@_attrs_define
class PromptInputFileAttachment:
    """ 
        Attributes:
            uri (str):
            description (str | Unset):
            mention (PromptMention | Unset):
            name (str | Unset):
     """

    uri: str
    description: str | Unset = UNSET
    mention: PromptMention | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        uri = self.uri

        description = self.description

        mention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mention, Unset):
            mention = self.mention.to_dict()

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "uri": uri,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if mention is not UNSET:
            field_dict["mention"] = mention
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        d = dict(src_dict)
        uri = d.pop("uri")

        description = d.pop("description", UNSET)

        _mention = d.pop("mention", UNSET)
        mention: PromptMention | Unset
        if isinstance(_mention,  Unset):
            mention = UNSET
        else:
            mention = PromptMention.from_dict(_mention)




        name = d.pop("name", UNSET)

        prompt_input_file_attachment = cls(
            uri=uri,
            description=description,
            mention=mention,
            name=name,
        )

        return prompt_input_file_attachment

