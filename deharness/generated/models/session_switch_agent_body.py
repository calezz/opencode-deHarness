from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionSwitchAgentBody")



@_attrs_define
class SessionSwitchAgentBody:
    """ 
        Attributes:
            agent (str):
     """

    agent: str





    def to_dict(self) -> dict[str, Any]:
        agent = self.agent


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent = d.pop("agent")

        session_switch_agent_body = cls(
            agent=agent,
        )

        return session_switch_agent_body

