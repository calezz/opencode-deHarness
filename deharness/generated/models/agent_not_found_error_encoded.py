from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_not_found_error_encoded_tag import AgentNotFoundErrorEncodedTag






T = TypeVar("T", bound="AgentNotFoundErrorEncoded")



@_attrs_define
class AgentNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (AgentNotFoundErrorEncodedTag):
            agent_id (str):
            message (str):
     """

    field_tag: AgentNotFoundErrorEncodedTag
    agent_id: str
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        agent_id = self.agent_id

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "agentID": agent_id,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = AgentNotFoundErrorEncodedTag(d.pop("_tag"))




        agent_id = d.pop("agentID")

        message = d.pop("message")

        agent_not_found_error_encoded = cls(
            field_tag=field_tag,
            agent_id=agent_id,
            message=message,
        )

        return agent_not_found_error_encoded

