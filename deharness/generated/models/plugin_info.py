from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.plugin_features import PluginFeatures
  from ..models.plugin_source_type_0 import PluginSourceType0
  from ..models.plugin_source_type_1 import PluginSourceType1
  from ..models.plugin_source_type_2 import PluginSourceType2
  from ..models.plugin_source_type_3 import PluginSourceType3
  from ..models.plugin_state_type_0 import PluginStateType0
  from ..models.plugin_state_type_1 import PluginStateType1





T = TypeVar("T", bound="PluginInfo")



@_attrs_define
class PluginInfo:
    """ 
        Attributes:
            features (PluginFeatures):
            source (PluginSourceType0 | PluginSourceType1 | PluginSourceType2 | PluginSourceType3):
            state (PluginStateType0 | PluginStateType1):
            id (str | Unset):
     """

    features: PluginFeatures
    source: PluginSourceType0 | PluginSourceType1 | PluginSourceType2 | PluginSourceType3
    state: PluginStateType0 | PluginStateType1
    id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.plugin_features import PluginFeatures # noqa: PLC0415
        from ..models.plugin_source_type_0 import PluginSourceType0 # noqa: PLC0415
        from ..models.plugin_source_type_1 import PluginSourceType1 # noqa: PLC0415
        from ..models.plugin_source_type_2 import PluginSourceType2 # noqa: PLC0415
        from ..models.plugin_source_type_3 import PluginSourceType3 # noqa: PLC0415
        from ..models.plugin_state_type_0 import PluginStateType0 # noqa: PLC0415
        from ..models.plugin_state_type_1 import PluginStateType1 # noqa: PLC0415
        features = self.features.to_dict()

        source: dict[str, Any]
        if isinstance(self.source, PluginSourceType0):
            source = self.source.to_dict()
        elif isinstance(self.source, PluginSourceType1):
            source = self.source.to_dict()
        elif isinstance(self.source, PluginSourceType2):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()


        state: dict[str, Any]
        if isinstance(self.state, PluginStateType0):
            state = self.state.to_dict()
        else:
            state = self.state.to_dict()


        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "features": features,
            "source": source,
            "state": state,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_features import PluginFeatures # noqa: PLC0415
        from ..models.plugin_source_type_0 import PluginSourceType0 # noqa: PLC0415
        from ..models.plugin_source_type_1 import PluginSourceType1 # noqa: PLC0415
        from ..models.plugin_source_type_2 import PluginSourceType2 # noqa: PLC0415
        from ..models.plugin_source_type_3 import PluginSourceType3 # noqa: PLC0415
        from ..models.plugin_state_type_0 import PluginStateType0 # noqa: PLC0415
        from ..models.plugin_state_type_1 import PluginStateType1 # noqa: PLC0415
        d = dict(src_dict)
        features = PluginFeatures.from_dict(d.pop("features"))




        def _parse_source(data: object) -> PluginSourceType0 | PluginSourceType1 | PluginSourceType2 | PluginSourceType3:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_source_type_0 = PluginSourceType0.from_dict(data)



                return componentsschemas_plugin_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_source_type_1 = PluginSourceType1.from_dict(data)



                return componentsschemas_plugin_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_source_type_2 = PluginSourceType2.from_dict(data)



                return componentsschemas_plugin_source_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_source_type_3 = PluginSourceType3.from_dict(data)



            return componentsschemas_plugin_source_type_3

        source = _parse_source(d.pop("source"))


        def _parse_state(data: object) -> PluginStateType0 | PluginStateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_plugin_state_type_0 = PluginStateType0.from_dict(data)



                return componentsschemas_plugin_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_plugin_state_type_1 = PluginStateType1.from_dict(data)



            return componentsschemas_plugin_state_type_1

        state = _parse_state(d.pop("state"))


        id = d.pop("id", UNSET)

        plugin_info = cls(
            features=features,
            source=source,
            state=state,
            id=id,
        )

        return plugin_info

