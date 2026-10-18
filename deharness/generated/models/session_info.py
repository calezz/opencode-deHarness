from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_info_outcome import SessionInfoOutcome
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.model_ref import ModelRef
  from ..models.permission_rule import PermissionRule
  from ..models.session_info_fork import SessionInfoFork
  from ..models.session_info_time import SessionInfoTime
  from ..models.session_metadata import SessionMetadata
  from ..models.session_revert import SessionRevert
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionInfo")



@_attrs_define
class SessionInfo:
    """ 
        Attributes:
            cost (float):
            id (str):
            location (LocationPublicRef):
            project_id (str):
            time (SessionInfoTime):
            tokens (TokenUsageInfo):
            agent (str | Unset):
            fork (SessionInfoFork | Unset):
            metadata (SessionMetadata | Unset):
            model (ModelRef | Unset):
            outcome (SessionInfoOutcome | Unset):
            parent_id (str | Unset):
            permissions (list[PermissionRule] | Unset):
            revert (SessionRevert | Unset):
            subpath (str | Unset):
            title (str | Unset):
     """

    cost: float
    id: str
    location: LocationPublicRef
    project_id: str
    time: SessionInfoTime
    tokens: TokenUsageInfo
    agent: str | Unset = UNSET
    fork: SessionInfoFork | Unset = UNSET
    metadata: SessionMetadata | Unset = UNSET
    model: ModelRef | Unset = UNSET
    outcome: SessionInfoOutcome | Unset = UNSET
    parent_id: str | Unset = UNSET
    permissions: list[PermissionRule] | Unset = UNSET
    revert: SessionRevert | Unset = UNSET
    subpath: str | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_info_fork import SessionInfoFork # noqa: PLC0415
        from ..models.session_info_time import SessionInfoTime # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
        from ..models.session_revert import SessionRevert # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        cost = self.cost

        id = self.id

        location = self.location.to_dict()

        project_id = self.project_id

        time = self.time.to_dict()

        tokens = self.tokens.to_dict()

        agent = self.agent

        fork: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fork, Unset):
            fork = self.fork.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value


        parent_id = self.parent_id

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for componentsschemas_permission_ruleset_item_data in self.permissions:
                componentsschemas_permission_ruleset_item = componentsschemas_permission_ruleset_item_data.to_dict()
                permissions.append(componentsschemas_permission_ruleset_item)



        revert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revert, Unset):
            revert = self.revert.to_dict()

        subpath = self.subpath

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cost": cost,
            "id": id,
            "location": location,
            "projectID": project_id,
            "time": time,
            "tokens": tokens,
        })
        if agent is not UNSET:
            field_dict["agent"] = agent
        if fork is not UNSET:
            field_dict["fork"] = fork
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model is not UNSET:
            field_dict["model"] = model
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if parent_id is not UNSET:
            field_dict["parentID"] = parent_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if revert is not UNSET:
            field_dict["revert"] = revert
        if subpath is not UNSET:
            field_dict["subpath"] = subpath
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_info_fork import SessionInfoFork # noqa: PLC0415
        from ..models.session_info_time import SessionInfoTime # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
        from ..models.session_revert import SessionRevert # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        cost = d.pop("cost")

        id = d.pop("id")

        location = LocationPublicRef.from_dict(d.pop("location"))




        project_id = d.pop("projectID")

        time = SessionInfoTime.from_dict(d.pop("time"))




        tokens = TokenUsageInfo.from_dict(d.pop("tokens"))




        agent = d.pop("agent", UNSET)

        _fork = d.pop("fork", UNSET)
        fork: SessionInfoFork | Unset
        if isinstance(_fork,  Unset):
            fork = UNSET
        else:
            fork = SessionInfoFork.from_dict(_fork)




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMetadata.from_dict(_metadata)




        _model = d.pop("model", UNSET)
        model: ModelRef | Unset
        if isinstance(_model,  Unset):
            model = UNSET
        else:
            model = ModelRef.from_dict(_model)




        _outcome = d.pop("outcome", UNSET)
        outcome: SessionInfoOutcome | Unset
        if isinstance(_outcome,  Unset):
            outcome = UNSET
        else:
            outcome = SessionInfoOutcome(_outcome)




        parent_id = d.pop("parentID", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionRule] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for componentsschemas_permission_ruleset_item_data in _permissions:
                componentsschemas_permission_ruleset_item = PermissionRule.from_dict(componentsschemas_permission_ruleset_item_data)



                permissions.append(componentsschemas_permission_ruleset_item)


        _revert = d.pop("revert", UNSET)
        revert: SessionRevert | Unset
        if isinstance(_revert,  Unset):
            revert = UNSET
        else:
            revert = SessionRevert.from_dict(_revert)




        subpath = d.pop("subpath", UNSET)

        title = d.pop("title", UNSET)

        session_info = cls(
            cost=cost,
            id=id,
            location=location,
            project_id=project_id,
            time=time,
            tokens=tokens,
            agent=agent,
            fork=fork,
            metadata=metadata,
            model=model,
            outcome=outcome,
            parent_id=parent_id,
            permissions=permissions,
            revert=revert,
            subpath=subpath,
            title=title,
        )

        return session_info

