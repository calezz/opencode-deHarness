from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_file_source_type_0 import PromptFileSourceType0
  from ..models.prompt_file_source_type_1 import PromptFileSourceType1
  from ..models.prompt_mention import PromptMention





T = TypeVar("T", bound="PromptFileAttachment")



@_attrs_define
class PromptFileAttachment:
    """ 
        Attributes:
            data (str):
            mime (str):
            source (PromptFileSourceType0 | PromptFileSourceType1):
            description (str | Unset):
            mention (PromptMention | Unset):
            name (str | Unset):
     """

    data: str
    mime: str
    source: PromptFileSourceType0 | PromptFileSourceType1
    description: str | Unset = UNSET
    mention: PromptMention | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_file_source_type_0 import PromptFileSourceType0 # noqa: PLC0415
        from ..models.prompt_file_source_type_1 import PromptFileSourceType1 # noqa: PLC0415
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        data = self.data

        mime = self.mime

        source: dict[str, Any]
        if isinstance(self.source, PromptFileSourceType0):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()


        description = self.description

        mention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mention, Unset):
            mention = self.mention.to_dict()

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "mime": mime,
            "source": source,
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
        from ..models.prompt_file_source_type_0 import PromptFileSourceType0 # noqa: PLC0415
        from ..models.prompt_file_source_type_1 import PromptFileSourceType1 # noqa: PLC0415
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        d = dict(src_dict)
        data = d.pop("data")

        mime = d.pop("mime")

        def _parse_source(data: object) -> PromptFileSourceType0 | PromptFileSourceType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_prompt_file_source_type_0 = PromptFileSourceType0.from_dict(data)



                return componentsschemas_prompt_file_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_prompt_file_source_type_1 = PromptFileSourceType1.from_dict(data)



            return componentsschemas_prompt_file_source_type_1

        source = _parse_source(d.pop("source"))


        description = d.pop("description", UNSET)

        _mention = d.pop("mention", UNSET)
        mention: PromptMention | Unset
        if isinstance(_mention,  Unset):
            mention = UNSET
        else:
            mention = PromptMention.from_dict(_mention)




        name = d.pop("name", UNSET)

        prompt_file_attachment = cls(
            data=data,
            mime=mime,
            source=source,
            description=description,
            mention=mention,
            name=name,
        )

        return prompt_file_attachment

