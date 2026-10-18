from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_agent_attachment import PromptAgentAttachment
  from ..models.prompt_file_attachment import PromptFileAttachment
  from ..models.prompt_skill_attachment import PromptSkillAttachment
  from ..models.session_inbox_user_payload_metadata import SessionInboxUserPayloadMetadata





T = TypeVar("T", bound="SessionInboxUserPayload")



@_attrs_define
class SessionInboxUserPayload:
    """ 
        Attributes:
            text (str):
            agents (list[PromptAgentAttachment] | Unset):
            files (list[PromptFileAttachment] | Unset):
            metadata (SessionInboxUserPayloadMetadata | Unset):
            skills (list[PromptSkillAttachment] | Unset):
     """

    text: str
    agents: list[PromptAgentAttachment] | Unset = UNSET
    files: list[PromptFileAttachment] | Unset = UNSET
    metadata: SessionInboxUserPayloadMetadata | Unset = UNSET
    skills: list[PromptSkillAttachment] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_agent_attachment import PromptAgentAttachment # noqa: PLC0415
        from ..models.prompt_file_attachment import PromptFileAttachment # noqa: PLC0415
        from ..models.prompt_skill_attachment import PromptSkillAttachment # noqa: PLC0415
        from ..models.session_inbox_user_payload_metadata import SessionInboxUserPayloadMetadata # noqa: PLC0415
        text = self.text

        agents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)



        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        skills: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = []
            for skills_item_data in self.skills:
                skills_item = skills_item_data.to_dict()
                skills.append(skills_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
        })
        if agents is not UNSET:
            field_dict["agents"] = agents
        if files is not UNSET:
            field_dict["files"] = files
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if skills is not UNSET:
            field_dict["skills"] = skills

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_agent_attachment import PromptAgentAttachment # noqa: PLC0415
        from ..models.prompt_file_attachment import PromptFileAttachment # noqa: PLC0415
        from ..models.prompt_skill_attachment import PromptSkillAttachment # noqa: PLC0415
        from ..models.session_inbox_user_payload_metadata import SessionInboxUserPayloadMetadata # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        _agents = d.pop("agents", UNSET)
        agents: list[PromptAgentAttachment] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = PromptAgentAttachment.from_dict(agents_item_data)



                agents.append(agents_item)


        _files = d.pop("files", UNSET)
        files: list[PromptFileAttachment] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = PromptFileAttachment.from_dict(files_item_data)



                files.append(files_item)


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionInboxUserPayloadMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionInboxUserPayloadMetadata.from_dict(_metadata)




        _skills = d.pop("skills", UNSET)
        skills: list[PromptSkillAttachment] | Unset = UNSET
        if _skills is not UNSET:
            skills = []
            for skills_item_data in _skills:
                skills_item = PromptSkillAttachment.from_dict(skills_item_data)



                skills.append(skills_item)


        session_inbox_user_payload = cls(
            text=text,
            agents=agents,
            files=files,
            metadata=metadata,
            skills=skills,
        )

        return session_inbox_user_payload

