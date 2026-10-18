from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.experimental_migration_v1_status_response_200_type_0_status import ExperimentalMigrationV1StatusResponse200Type0Status






T = TypeVar("T", bound="ExperimentalMigrationV1StatusResponse200Type0")



@_attrs_define
class ExperimentalMigrationV1StatusResponse200Type0:
    """ 
        Attributes:
            status (ExperimentalMigrationV1StatusResponse200Type0Status):
     """

    status: ExperimentalMigrationV1StatusResponse200Type0Status





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ExperimentalMigrationV1StatusResponse200Type0Status(d.pop("status"))




        experimental_migration_v1_status_response_200_type_0 = cls(
            status=status,
        )

        return experimental_migration_v1_status_response_200_type_0

