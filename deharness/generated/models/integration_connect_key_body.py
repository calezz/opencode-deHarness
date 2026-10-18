from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_answer import FormAnswer





T = TypeVar("T", bound="IntegrationConnectKeyBody")



@_attrs_define
class IntegrationConnectKeyBody:
    """ 
        Attributes:
            key (str):
            answer (FormAnswer | None | Unset):
            label (None | str | Unset):
     """

    key: str
    answer: FormAnswer | None | Unset = UNSET
    label: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_answer import FormAnswer # noqa: PLC0415
        key = self.key

        answer: dict[str, Any] | None | Unset
        if isinstance(self.answer, Unset):
            answer = UNSET
        elif isinstance(self.answer, FormAnswer):
            answer = self.answer.to_dict()
        else:
            answer = self.answer

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
        })
        if answer is not UNSET:
            field_dict["answer"] = answer
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_answer import FormAnswer # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_answer(data: object) -> FormAnswer | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                answer_type_0 = FormAnswer.from_dict(data)



                return answer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FormAnswer | None | Unset, data)

        answer = _parse_answer(d.pop("answer", UNSET))


        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))


        integration_connect_key_body = cls(
            key=key,
            answer=answer,
            label=label,
        )

        return integration_connect_key_body

