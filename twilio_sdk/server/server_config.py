from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UrlTemplate


class DefaultConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://api.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class DefaultConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default1Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://messaging.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default1ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default2Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://content.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default2ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default3Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://verify.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default3ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default4Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://lookups.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default4ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default5Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://numbers.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default5ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default6Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://video.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default6ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default7Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://conversations.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default7ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default8Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://taskrouter.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default8ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default9Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://trusthub.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default9ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default10Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://proxy.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default10ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default11Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://studio.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default11ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default12Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://sync.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default12ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default13Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://flex-api.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default13ConfigDict(TypedDict):
    base_url: NotRequired[str]


class Default14Config(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    base_url: str = "https://insights.twilio.com"

    def resolve(self, path: str) -> UrlTemplate:
        return UrlTemplate(base_url=self.base_url, path=path)


class Default14ConfigDict(TypedDict):
    base_url: NotRequired[str]


class ServerConfig(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    default: DefaultConfig = Field(default_factory=DefaultConfig)
    default1: Default1Config = Field(default_factory=Default1Config)
    default2: Default2Config = Field(default_factory=Default2Config)
    default3: Default3Config = Field(default_factory=Default3Config)
    default4: Default4Config = Field(default_factory=Default4Config)
    default5: Default5Config = Field(default_factory=Default5Config)
    default6: Default6Config = Field(default_factory=Default6Config)
    default7: Default7Config = Field(default_factory=Default7Config)
    default8: Default8Config = Field(default_factory=Default8Config)
    default9: Default9Config = Field(default_factory=Default9Config)
    default10: Default10Config = Field(default_factory=Default10Config)
    default11: Default11Config = Field(default_factory=Default11Config)
    default12: Default12Config = Field(default_factory=Default12Config)
    default13: Default13Config = Field(default_factory=Default13Config)
    default14: Default14Config = Field(default_factory=Default14Config)

    @classmethod
    def coerce(cls, value: ServerConfigOrDict | None) -> ServerConfig:
        if isinstance(value, cls):
            return value
        return cls.model_validate(value if value is not None else {})


class ServerConfigDict(TypedDict):
    default: NotRequired[DefaultConfigDict]
    default1: NotRequired[Default1ConfigDict]
    default2: NotRequired[Default2ConfigDict]
    default3: NotRequired[Default3ConfigDict]
    default4: NotRequired[Default4ConfigDict]
    default5: NotRequired[Default5ConfigDict]
    default6: NotRequired[Default6ConfigDict]
    default7: NotRequired[Default7ConfigDict]
    default8: NotRequired[Default8ConfigDict]
    default9: NotRequired[Default9ConfigDict]
    default10: NotRequired[Default10ConfigDict]
    default11: NotRequired[Default11ConfigDict]
    default12: NotRequired[Default12ConfigDict]
    default13: NotRequired[Default13ConfigDict]
    default14: NotRequired[Default14ConfigDict]


ServerConfigOrDict: TypeAlias = ServerConfig | ServerConfigDict
