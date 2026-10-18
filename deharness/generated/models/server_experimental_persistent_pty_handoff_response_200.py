from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_handoff import PersistentPtyHandoff





T = TypeVar("T", bound="ServerExperimentalPersistentPtyHandoffResponse200")



@_attrs_define
class ServerExperimentalPersistentPtyHandoffResponse200:
    """ 
        Attributes:
            handoff (None | PersistentPtyHandoff):
     """

    handoff: None | PersistentPtyHandoff





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_handoff import PersistentPtyHandoff # noqa: PLC0415
        handoff: dict[str, Any] | None
        if isinstance(self.handoff, PersistentPtyHandoff):
            handoff = self.handoff.to_dict()
        else:
            handoff = self.handoff


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "handoff": handoff,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_handoff import PersistentPtyHandoff # noqa: PLC0415
        d = dict(src_dict)
        def _parse_handoff(data: object) -> None | PersistentPtyHandoff:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                handoff_type_0 = PersistentPtyHandoff.from_dict(data)



                return handoff_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersistentPtyHandoff, data)

        handoff = _parse_handoff(d.pop("handoff"))


        server_experimental_persistent_pty_handoff_response_200 = cls(
            handoff=handoff,
        )

        return server_experimental_persistent_pty_handoff_response_200

