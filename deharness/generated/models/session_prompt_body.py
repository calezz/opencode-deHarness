from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_agent_attachment import PromptAgentAttachment
  from ..models.prompt_input_file_attachment import PromptInputFileAttachment
  from ..models.prompt_input_skill_attachment import PromptInputSkillAttachment
  from ..models.session_prompt_body_metadata import SessionPromptBodyMetadata





T = TypeVar("T", bound="SessionPromptBody")



@_attrs_define
class SessionPromptBody:
    """ 
        Attributes:
            text (str):
            agents (list[PromptAgentAttachment] | Unset):
            delivery (None | SessionInboxDelivery | Unset):
            files (list[PromptInputFileAttachment] | Unset):
            id (None | str | Unset):
            metadata (SessionPromptBodyMetadata | Unset):
            resume (bool | None | Unset):
            skills (list[PromptInputSkillAttachment] | Unset):
     """

    text: str
    agents: list[PromptAgentAttachment] | Unset = UNSET
    delivery: None | SessionInboxDelivery | Unset = UNSET
    files: list[PromptInputFileAttachment] | Unset = UNSET
    id: None | str | Unset = UNSET
    metadata: SessionPromptBodyMetadata | Unset = UNSET
    resume: bool | None | Unset = UNSET
    skills: list[PromptInputSkillAttachment] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_agent_attachment import PromptAgentAttachment # noqa: PLC0415
        from ..models.prompt_input_file_attachment import PromptInputFileAttachment # noqa: PLC0415
        from ..models.prompt_input_skill_attachment import PromptInputSkillAttachment # noqa: PLC0415
        from ..models.session_prompt_body_metadata import SessionPromptBodyMetadata # noqa: PLC0415
        text = self.text

        agents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)



        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        elif isinstance(self.delivery, SessionInboxDelivery):
            delivery = self.delivery.value
        else:
            delivery = self.delivery

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        resume: bool | None | Unset
        if isinstance(self.resume, Unset):
            resume = UNSET
        else:
            resume = self.resume

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
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if files is not UNSET:
            field_dict["files"] = files
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if resume is not UNSET:
            field_dict["resume"] = resume
        if skills is not UNSET:
            field_dict["skills"] = skills

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_agent_attachment import PromptAgentAttachment # noqa: PLC0415
        from ..models.prompt_input_file_attachment import PromptInputFileAttachment # noqa: PLC0415
        from ..models.prompt_input_skill_attachment import PromptInputSkillAttachment # noqa: PLC0415
        from ..models.session_prompt_body_metadata import SessionPromptBodyMetadata # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        _agents = d.pop("agents", UNSET)
        agents: list[PromptAgentAttachment] | Unset = UNSET
        if _agents is not UNSET:
            agents = []
            for agents_item_data in _agents:
                agents_item = PromptAgentAttachment.from_dict(agents_item_data)



                agents.append(agents_item)


        def _parse_delivery(data: object) -> None | SessionInboxDelivery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_type_0 = SessionInboxDelivery(data)



                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionInboxDelivery | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        _files = d.pop("files", UNSET)
        files: list[PromptInputFileAttachment] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = PromptInputFileAttachment.from_dict(files_item_data)



                files.append(files_item)


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionPromptBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionPromptBodyMetadata.from_dict(_metadata)




        def _parse_resume(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resume = _parse_resume(d.pop("resume", UNSET))


        _skills = d.pop("skills", UNSET)
        skills: list[PromptInputSkillAttachment] | Unset = UNSET
        if _skills is not UNSET:
            skills = []
            for skills_item_data in _skills:
                skills_item = PromptInputSkillAttachment.from_dict(skills_item_data)



                skills.append(skills_item)


        session_prompt_body = cls(
            text=text,
            agents=agents,
            delivery=delivery,
            files=files,
            id=id,
            metadata=metadata,
            resume=resume,
            skills=skills,
        )

        return session_prompt_body

