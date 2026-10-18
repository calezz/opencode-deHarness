from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_fork_boundary_type_0 import SessionForkBoundaryType0
  from ..models.session_fork_boundary_type_1 import SessionForkBoundaryType1





T = TypeVar("T", bound="SessionInfoFork")



@_attrs_define
class SessionInfoFork:
    """ 
        Attributes:
            boundary (SessionForkBoundaryType0 | SessionForkBoundaryType1):
            session_id (str):
     """

    boundary: SessionForkBoundaryType0 | SessionForkBoundaryType1
    session_id: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_fork_boundary_type_0 import SessionForkBoundaryType0 # noqa: PLC0415
        from ..models.session_fork_boundary_type_1 import SessionForkBoundaryType1 # noqa: PLC0415
        boundary: dict[str, Any]
        if isinstance(self.boundary, SessionForkBoundaryType0):
            boundary = self.boundary.to_dict()
        else:
            boundary = self.boundary.to_dict()


        session_id = self.session_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "boundary": boundary,
            "sessionID": session_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_fork_boundary_type_0 import SessionForkBoundaryType0 # noqa: PLC0415
        from ..models.session_fork_boundary_type_1 import SessionForkBoundaryType1 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_boundary(data: object) -> SessionForkBoundaryType0 | SessionForkBoundaryType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_fork_boundary_type_0 = SessionForkBoundaryType0.from_dict(data)



                return componentsschemas_session_fork_boundary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_session_fork_boundary_type_1 = SessionForkBoundaryType1.from_dict(data)



            return componentsschemas_session_fork_boundary_type_1

        boundary = _parse_boundary(d.pop("boundary"))


        session_id = d.pop("sessionID")

        session_info_fork = cls(
            boundary=boundary,
            session_id=session_id,
        )

        return session_info_fork

