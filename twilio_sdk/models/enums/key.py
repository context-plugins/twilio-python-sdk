from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Key(str, Enum):
    """The language key/identifier (typically uppercase)"""

    ALL = "ALL"
    AFRIKAANS = "AFRIKAANS"
    ARABIC = "ARABIC"
    BENGALI = "BENGALI"
    CHINESE = "CHINESE"
    CROATIAN = "CROATIAN"
    CZECH = "CZECH"
    DANISH = "DANISH"
    DUTCH = "DUTCH"
    ENGLISH = "ENGLISH"
    ESTONIAN = "ESTONIAN"
    FINNISH = "FINNISH"
    FRENCH = "FRENCH"
    GERMAN = "GERMAN"
    GREEK = "GREEK"
    HEBREW = "HEBREW"
    HINDI = "HINDI"
    HUNGARIAN = "HUNGARIAN"
    ITALIAN = "ITALIAN"
    JAPANESE = "JAPANESE"
    KOREAN = "KOREAN"
    LATVIAN = "LATVIAN"
    LITHUANIAN = "LITHUANIAN"
    MALAY = "MALAY"
    MALAYSIAN = "MALAYSIAN"
    NORWEGIAN = "NORWEGIAN"
    POLISH = "POLISH"
    PORTUGUESE = "PORTUGUESE"
    RUSSIAN = "RUSSIAN"
    SLOVAK = "SLOVAK"
    SLOVENE = "SLOVENE"
    SPANISH = "SPANISH"
    SOUTHERN_NDEBELE = "SOUTHERN_NDEBELE"
    SOUTHERN_SOTHO = "SOUTHERN_SOTHO"
    SWATI = "SWATI"
    SWEDISH = "SWEDISH"
    TAMIL = "TAMIL"
    TSWANA = "TSWANA"
    TSONGA = "TSONGA"
    VENDA = "VENDA"
    XHOSA = "XHOSA"
    ZULU = "ZULU"

    __str__ = str.__str__


KeyOrStr: TypeAlias = Annotated[Key | str, open_enum_validator(Key)]
