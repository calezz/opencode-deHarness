from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.connection_credential_info import ConnectionCredentialInfo
  from ..models.connection_env_info import ConnectionEnvInfo
  from ..models.integration_command_method import IntegrationCommandMethod
  from ..models.integration_env_method import IntegrationEnvMethod
  from ..models.integration_external_method import IntegrationExternalMethod
  from ..models.integration_info_metadata import IntegrationInfoMetadata
  from ..models.integration_key_method import IntegrationKeyMethod
  from ..models.integration_o_auth_method import IntegrationOAuthMethod





T = TypeVar("T", bound="IntegrationInfo")



@_attrs_define
class IntegrationInfo:
    """ 
        Attributes:
            connections (list[ConnectionCredentialInfo | ConnectionEnvInfo]):
            id (str):
            methods (list[IntegrationCommandMethod | IntegrationEnvMethod | IntegrationExternalMethod | IntegrationKeyMethod
                | IntegrationOAuthMethod]):
            name (str):
            metadata (IntegrationInfoMetadata | Unset):
     """

    connections: list[ConnectionCredentialInfo | ConnectionEnvInfo]
    id: str
    methods: list[IntegrationCommandMethod | IntegrationEnvMethod | IntegrationExternalMethod | IntegrationKeyMethod | IntegrationOAuthMethod]
    name: str
    metadata: IntegrationInfoMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_credential_info import ConnectionCredentialInfo # noqa: PLC0415
        from ..models.connection_env_info import ConnectionEnvInfo # noqa: PLC0415
        from ..models.integration_command_method import IntegrationCommandMethod # noqa: PLC0415
        from ..models.integration_env_method import IntegrationEnvMethod # noqa: PLC0415
        from ..models.integration_external_method import IntegrationExternalMethod # noqa: PLC0415
        from ..models.integration_info_metadata import IntegrationInfoMetadata # noqa: PLC0415
        from ..models.integration_key_method import IntegrationKeyMethod # noqa: PLC0415
        from ..models.integration_o_auth_method import IntegrationOAuthMethod # noqa: PLC0415
        connections = []
        for connections_item_data in self.connections:
            connections_item: dict[str, Any]
            if isinstance(connections_item_data, ConnectionCredentialInfo):
                connections_item = connections_item_data.to_dict()
            else:
                connections_item = connections_item_data.to_dict()

            connections.append(connections_item)



        id = self.id

        methods = []
        for methods_item_data in self.methods:
            methods_item: dict[str, Any]
            if isinstance(methods_item_data, IntegrationOAuthMethod):
                methods_item = methods_item_data.to_dict()
            elif isinstance(methods_item_data, IntegrationCommandMethod):
                methods_item = methods_item_data.to_dict()
            elif isinstance(methods_item_data, IntegrationKeyMethod):
                methods_item = methods_item_data.to_dict()
            elif isinstance(methods_item_data, IntegrationExternalMethod):
                methods_item = methods_item_data.to_dict()
            else:
                methods_item = methods_item_data.to_dict()

            methods.append(methods_item)



        name = self.name

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "connections": connections,
            "id": id,
            "methods": methods,
            "name": name,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_credential_info import ConnectionCredentialInfo # noqa: PLC0415
        from ..models.connection_env_info import ConnectionEnvInfo # noqa: PLC0415
        from ..models.integration_command_method import IntegrationCommandMethod # noqa: PLC0415
        from ..models.integration_env_method import IntegrationEnvMethod # noqa: PLC0415
        from ..models.integration_external_method import IntegrationExternalMethod # noqa: PLC0415
        from ..models.integration_info_metadata import IntegrationInfoMetadata # noqa: PLC0415
        from ..models.integration_key_method import IntegrationKeyMethod # noqa: PLC0415
        from ..models.integration_o_auth_method import IntegrationOAuthMethod # noqa: PLC0415
        d = dict(src_dict)
        connections = []
        _connections = d.pop("connections")
        for connections_item_data in (_connections):
            def _parse_connections_item(data: object) -> ConnectionCredentialInfo | ConnectionEnvInfo:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_connection_info_type_0 = ConnectionCredentialInfo.from_dict(data)



                    return componentsschemas_connection_info_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_connection_info_type_1 = ConnectionEnvInfo.from_dict(data)



                return componentsschemas_connection_info_type_1

            connections_item = _parse_connections_item(connections_item_data)

            connections.append(connections_item)


        id = d.pop("id")

        methods = []
        _methods = d.pop("methods")
        for methods_item_data in (_methods):
            def _parse_methods_item(data: object) -> IntegrationCommandMethod | IntegrationEnvMethod | IntegrationExternalMethod | IntegrationKeyMethod | IntegrationOAuthMethod:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_integration_method_type_0 = IntegrationOAuthMethod.from_dict(data)



                    return componentsschemas_integration_method_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_integration_method_type_1 = IntegrationCommandMethod.from_dict(data)



                    return componentsschemas_integration_method_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_integration_method_type_2 = IntegrationKeyMethod.from_dict(data)



                    return componentsschemas_integration_method_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_integration_method_type_3 = IntegrationExternalMethod.from_dict(data)



                    return componentsschemas_integration_method_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_method_type_4 = IntegrationEnvMethod.from_dict(data)



                return componentsschemas_integration_method_type_4

            methods_item = _parse_methods_item(methods_item_data)

            methods.append(methods_item)


        name = d.pop("name")

        _metadata = d.pop("metadata", UNSET)
        metadata: IntegrationInfoMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = IntegrationInfoMetadata.from_dict(_metadata)




        integration_info = cls(
            connections=connections,
            id=id,
            methods=methods,
            name=name,
            metadata=metadata,
        )

        return integration_info

