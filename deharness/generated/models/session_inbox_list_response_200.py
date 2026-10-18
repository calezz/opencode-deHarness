from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_compaction import SessionInboxCompaction
  from ..models.session_inbox_move import SessionInboxMove
  from ..models.session_inbox_synthetic import SessionInboxSynthetic
  from ..models.session_inbox_user import SessionInboxUser





T = TypeVar("T", bound="SessionInboxListResponse200")



@_attrs_define
class SessionInboxListResponse200:
    """ 
        Attributes:
            data (list[SessionInboxCompaction | SessionInboxMove | SessionInboxSynthetic | SessionInboxUser]):
     """

    data: list[SessionInboxCompaction | SessionInboxMove | SessionInboxSynthetic | SessionInboxUser]





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_compaction import SessionInboxCompaction # noqa: PLC0415
        from ..models.session_inbox_move import SessionInboxMove # noqa: PLC0415
        from ..models.session_inbox_synthetic import SessionInboxSynthetic # noqa: PLC0415
        from ..models.session_inbox_user import SessionInboxUser # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, SessionInboxUser):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionInboxSynthetic):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionInboxCompaction):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_inbox_compaction import SessionInboxCompaction # noqa: PLC0415
        from ..models.session_inbox_move import SessionInboxMove # noqa: PLC0415
        from ..models.session_inbox_synthetic import SessionInboxSynthetic # noqa: PLC0415
        from ..models.session_inbox_user import SessionInboxUser # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            def _parse_data_item(data: object) -> SessionInboxCompaction | SessionInboxMove | SessionInboxSynthetic | SessionInboxUser:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_inbox_info_type_0 = SessionInboxUser.from_dict(data)



                    return componentsschemas_session_inbox_info_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_inbox_info_type_1 = SessionInboxSynthetic.from_dict(data)



                    return componentsschemas_session_inbox_info_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_inbox_info_type_2 = SessionInboxCompaction.from_dict(data)



                    return componentsschemas_session_inbox_info_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_inbox_info_type_3 = SessionInboxMove.from_dict(data)



                return componentsschemas_session_inbox_info_type_3

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)


        session_inbox_list_response_200 = cls(
            data=data,
        )

        return session_inbox_list_response_200

