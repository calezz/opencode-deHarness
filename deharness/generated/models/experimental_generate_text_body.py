from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef





T = TypeVar("T", bound="ExperimentalGenerateTextBody")



@_attrs_define
class ExperimentalGenerateTextBody:
    """ 
        Attributes:
            prompt (str):
            model (ModelRef | None | Unset):
     """

    prompt: str
    model: ModelRef | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        prompt = self.prompt

        model: dict[str, Any] | None | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ModelRef):
            model = self.model.to_dict()
        else:
            model = self.model


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "prompt": prompt,
        })
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        d = dict(src_dict)
        prompt = d.pop("prompt")

        def _parse_model(data: object) -> ModelRef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = ModelRef.from_dict(data)



                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelRef | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        experimental_generate_text_body = cls(
            prompt=prompt,
            model=model,
        )

        return experimental_generate_text_body

