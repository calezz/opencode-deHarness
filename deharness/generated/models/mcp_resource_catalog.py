from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_resource import McpResource
  from ..models.mcp_resource_template import McpResourceTemplate





T = TypeVar("T", bound="McpResourceCatalog")



@_attrs_define
class McpResourceCatalog:
    """ 
        Attributes:
            resources (list[McpResource]):
            templates (list[McpResourceTemplate]):
     """

    resources: list[McpResource]
    templates: list[McpResourceTemplate]





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_resource import McpResource # noqa: PLC0415
        from ..models.mcp_resource_template import McpResourceTemplate # noqa: PLC0415
        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)



        templates = []
        for templates_item_data in self.templates:
            templates_item = templates_item_data.to_dict()
            templates.append(templates_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "resources": resources,
            "templates": templates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_resource import McpResource # noqa: PLC0415
        from ..models.mcp_resource_template import McpResourceTemplate # noqa: PLC0415
        d = dict(src_dict)
        resources = []
        _resources = d.pop("resources")
        for resources_item_data in (_resources):
            resources_item = McpResource.from_dict(resources_item_data)



            resources.append(resources_item)


        templates = []
        _templates = d.pop("templates")
        for templates_item_data in (_templates):
            templates_item = McpResourceTemplate.from_dict(templates_item_data)



            templates.append(templates_item)


        mcp_resource_catalog = cls(
            resources=resources,
            templates=templates,
        )

        return mcp_resource_catalog

