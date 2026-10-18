from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef





T = TypeVar("T", bound="SessionSwitchModelBody")



@_attrs_define
class SessionSwitchModelBody:
    """ 
        Attributes:
            model (ModelRef):
     """

    model: ModelRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        model = self.model.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "model": model,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        d = dict(src_dict)
        model = ModelRef.from_dict(d.pop("model"))




        session_switch_model_body = cls(
            model=model,
        )

        return session_switch_model_body

