from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExperimentalMigrationV1StatusResponse200Type1Progress")



@_attrs_define
class ExperimentalMigrationV1StatusResponse200Type1Progress:
    """ 
        Attributes:
            label (str):
            denominator (int | None | Unset):
            numerator (int | None | Unset):
     """

    label: str
    denominator: int | None | Unset = UNSET
    numerator: int | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        label = self.label

        denominator: int | None | Unset
        if isinstance(self.denominator, Unset):
            denominator = UNSET
        else:
            denominator = self.denominator

        numerator: int | None | Unset
        if isinstance(self.numerator, Unset):
            numerator = UNSET
        else:
            numerator = self.numerator


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "label": label,
        })
        if denominator is not UNSET:
            field_dict["denominator"] = denominator
        if numerator is not UNSET:
            field_dict["numerator"] = numerator

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_denominator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        denominator = _parse_denominator(d.pop("denominator", UNSET))


        def _parse_numerator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        numerator = _parse_numerator(d.pop("numerator", UNSET))


        experimental_migration_v1_status_response_200_type_1_progress = cls(
            label=label,
            denominator=denominator,
            numerator=numerator,
        )

        return experimental_migration_v1_status_response_200_type_1_progress

