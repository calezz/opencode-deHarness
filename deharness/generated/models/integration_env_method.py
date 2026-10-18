from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_env_method_type import IntegrationEnvMethodType
from typing import cast






T = TypeVar("T", bound="IntegrationEnvMethod")



@_attrs_define
class IntegrationEnvMethod:
    """ 
        Attributes:
            names (list[str]):
            type_ (IntegrationEnvMethodType):
     """

    names: list[str]
    type_: IntegrationEnvMethodType





    def to_dict(self) -> dict[str, Any]:
        names = self.names



        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "names": names,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        names = cast(list[str], d.pop("names"))


        type_ = IntegrationEnvMethodType(d.pop("type"))




        integration_env_method = cls(
            names=names,
            type_=type_,
        )

        return integration_env_method

