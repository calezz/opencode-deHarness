from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.form_answer import FormAnswer





T = TypeVar("T", bound="FormReply")



@_attrs_define
class FormReply:
    """ 
        Attributes:
            answer (FormAnswer):
     """

    answer: FormAnswer





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_answer import FormAnswer # noqa: PLC0415
        answer = self.answer.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "answer": answer,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_answer import FormAnswer # noqa: PLC0415
        d = dict(src_dict)
        answer = FormAnswer.from_dict(d.pop("answer"))




        form_reply = cls(
            answer=answer,
        )

        return form_reply

