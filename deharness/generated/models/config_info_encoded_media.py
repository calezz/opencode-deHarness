from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded_media_image import ConfigInfoEncodedMediaImage





T = TypeVar("T", bound="ConfigInfoEncodedMedia")



@_attrs_define
class ConfigInfoEncodedMedia:
    """ 
        Attributes:
            image (ConfigInfoEncodedMediaImage | Unset):
     """

    image: ConfigInfoEncodedMediaImage | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded_media_image import ConfigInfoEncodedMediaImage # noqa: PLC0415
        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded_media_image import ConfigInfoEncodedMediaImage # noqa: PLC0415
        d = dict(src_dict)
        _image = d.pop("image", UNSET)
        image: ConfigInfoEncodedMediaImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = ConfigInfoEncodedMediaImage.from_dict(_image)




        config_info_encoded_media = cls(
            image=image,
        )

        return config_info_encoded_media

