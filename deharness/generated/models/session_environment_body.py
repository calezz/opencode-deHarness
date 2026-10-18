from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_environment_body_variables import SessionEnvironmentBodyVariables





T = TypeVar("T", bound="SessionEnvironmentBody")



@_attrs_define
class SessionEnvironmentBody:
    """ 
        Attributes:
            variables (SessionEnvironmentBodyVariables):
     """

    variables: SessionEnvironmentBodyVariables





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_environment_body_variables import SessionEnvironmentBodyVariables # noqa: PLC0415
        variables = self.variables.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "variables": variables,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_environment_body_variables import SessionEnvironmentBodyVariables # noqa: PLC0415
        d = dict(src_dict)
        variables = SessionEnvironmentBodyVariables.from_dict(d.pop("variables"))




        session_environment_body = cls(
            variables=variables,
        )

        return session_environment_body

