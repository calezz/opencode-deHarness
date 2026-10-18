from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PtyTicketConnectToken")



@_attrs_define
class PtyTicketConnectToken:
    """ 
        Attributes:
            expires_in (int):
            ticket (str):
     """

    expires_in: int
    ticket: str





    def to_dict(self) -> dict[str, Any]:
        expires_in = self.expires_in

        ticket = self.ticket


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expires_in": expires_in,
            "ticket": ticket,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_in = d.pop("expires_in")

        ticket = d.pop("ticket")

        pty_ticket_connect_token = cls(
            expires_in=expires_in,
            ticket=ticket,
        )

        return pty_ticket_connect_token

