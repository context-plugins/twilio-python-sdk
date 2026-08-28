from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MessagingV2PresignedUrlRequest(SdkBaseModel):
    image_content_md5: str = Field(alias="imageContentMd5")
    """Base64-encoded MD5 hash of the image"""

    image_content_type: str = Field(alias="imageContentType")
    """MIME type of the image (e.g., image/png, image/jpeg)"""

    image_kind: str = Field(alias="imageKind")
    """Type of image (logo, hero, etc.)"""

    image_name: str = Field(alias="imageName")
    """Name of the image file"""

    image_size_bytes: int = Field(alias="imageSizeBytes")
    """Size of the image in bytes"""

    image_height: Optional[int] = Field(default=UNSET, alias="imageHeight")
    """Height of the image in pixels"""

    image_width: Optional[int] = Field(default=UNSET, alias="imageWidth")
    """Width of the image in pixels"""


class MessagingV2PresignedUrlRequestDict(TypedDict):
    image_content_md5: str
    image_content_type: str
    image_kind: str
    image_name: str
    image_size_bytes: int
    image_height: NotRequired[int]
    image_width: NotRequired[int]
