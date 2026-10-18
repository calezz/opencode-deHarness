from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.vcs_branch import VcsBranch





T = TypeVar("T", bound="VcsInfo")



@_attrs_define
class VcsInfo:
    """ 
        Attributes:
            branch (VcsBranch):
            provider (str | Unset):
     """

    branch: VcsBranch
    provider: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.vcs_branch import VcsBranch # noqa: PLC0415
        branch = self.branch.to_dict()

        provider = self.provider


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "branch": branch,
        })
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vcs_branch import VcsBranch # noqa: PLC0415
        d = dict(src_dict)
        branch = VcsBranch.from_dict(d.pop("branch"))




        provider = d.pop("provider", UNSET)

        vcs_info = cls(
            branch=branch,
            provider=provider,
        )

        return vcs_info

