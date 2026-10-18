from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_agent_encoded_request_body import ConfigAgentEncodedRequestBody
  from ..models.config_agent_encoded_request_headers import ConfigAgentEncodedRequestHeaders





T = TypeVar("T", bound="ConfigAgentEncodedRequest")



@_attrs_define
class ConfigAgentEncodedRequest:
    """ 
        Attributes:
            body (ConfigAgentEncodedRequestBody | Unset):
            headers (ConfigAgentEncodedRequestHeaders | Unset):
     """

    body: ConfigAgentEncodedRequestBody | Unset = UNSET
    headers: ConfigAgentEncodedRequestHeaders | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_agent_encoded_request_body import ConfigAgentEncodedRequestBody # noqa: PLC0415
        from ..models.config_agent_encoded_request_headers import ConfigAgentEncodedRequestHeaders # noqa: PLC0415
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_agent_encoded_request_body import ConfigAgentEncodedRequestBody # noqa: PLC0415
        from ..models.config_agent_encoded_request_headers import ConfigAgentEncodedRequestHeaders # noqa: PLC0415
        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: ConfigAgentEncodedRequestBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ConfigAgentEncodedRequestBody.from_dict(_body)




        _headers = d.pop("headers", UNSET)
        headers: ConfigAgentEncodedRequestHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ConfigAgentEncodedRequestHeaders.from_dict(_headers)




        config_agent_encoded_request = cls(
            body=body,
            headers=headers,
        )

        return config_agent_encoded_request

