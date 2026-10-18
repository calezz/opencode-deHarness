from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.experimental_migration_v1_status_response_200_type_1_status import ExperimentalMigrationV1StatusResponse200Type1Status
from typing import cast

if TYPE_CHECKING:
  from ..models.experimental_migration_v1_status_response_200_type_1_progress import ExperimentalMigrationV1StatusResponse200Type1Progress





T = TypeVar("T", bound="ExperimentalMigrationV1StatusResponse200Type1")



@_attrs_define
class ExperimentalMigrationV1StatusResponse200Type1:
    """ 
        Attributes:
            progress (ExperimentalMigrationV1StatusResponse200Type1Progress):
            status (ExperimentalMigrationV1StatusResponse200Type1Status):
     """

    progress: ExperimentalMigrationV1StatusResponse200Type1Progress
    status: ExperimentalMigrationV1StatusResponse200Type1Status





    def to_dict(self) -> dict[str, Any]:
        from ..models.experimental_migration_v1_status_response_200_type_1_progress import ExperimentalMigrationV1StatusResponse200Type1Progress # noqa: PLC0415
        progress = self.progress.to_dict()

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "progress": progress,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experimental_migration_v1_status_response_200_type_1_progress import ExperimentalMigrationV1StatusResponse200Type1Progress # noqa: PLC0415
        d = dict(src_dict)
        progress = ExperimentalMigrationV1StatusResponse200Type1Progress.from_dict(d.pop("progress"))




        status = ExperimentalMigrationV1StatusResponse200Type1Status(d.pop("status"))




        experimental_migration_v1_status_response_200_type_1 = cls(
            progress=progress,
            status=status,
        )

        return experimental_migration_v1_status_response_200_type_1

