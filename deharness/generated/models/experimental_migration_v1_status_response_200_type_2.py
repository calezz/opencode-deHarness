from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.experimental_migration_v1_status_response_200_type_2_status import ExperimentalMigrationV1StatusResponse200Type2Status






T = TypeVar("T", bound="ExperimentalMigrationV1StatusResponse200Type2")



@_attrs_define
class ExperimentalMigrationV1StatusResponse200Type2:
    """ 
        Attributes:
            error (str):
            status (ExperimentalMigrationV1StatusResponse200Type2Status):
     """

    error: str
    status: ExperimentalMigrationV1StatusResponse200Type2Status





    def to_dict(self) -> dict[str, Any]:
        error = self.error

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        status = ExperimentalMigrationV1StatusResponse200Type2Status(d.pop("status"))




        experimental_migration_v1_status_response_200_type_2 = cls(
            error=error,
            status=status,
        )

        return experimental_migration_v1_status_response_200_type_2

