from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_assistant_text_type import SessionMessageAssistantTextType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_provider_state import SessionMessageProviderState





T = TypeVar("T", bound="SessionMessageAssistantText")



@_attrs_define
class SessionMessageAssistantText:
    """ 
        Attributes:
            text (str):
            type_ (SessionMessageAssistantTextType):
            state (SessionMessageProviderState | Unset):
     """

    text: str
    type_: SessionMessageAssistantTextType
    state: SessionMessageProviderState | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_provider_state import SessionMessageProviderState # noqa: PLC0415
        text = self.text

        type_ = self.type_.value

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
            "type": type_,
        })
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_provider_state import SessionMessageProviderState # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        type_ = SessionMessageAssistantTextType(d.pop("type"))




        _state = d.pop("state", UNSET)
        state: SessionMessageProviderState | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = SessionMessageProviderState.from_dict(_state)




        session_message_assistant_text = cls(
            text=text,
            type_=type_,
            state=state,
        )

        return session_message_assistant_text

