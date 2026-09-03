from __future__ import annotations

from typing import TypeAlias

from ..content_text import ContentText, ContentTextDict
from ..content_transcription import ContentTranscription, ContentTranscriptionDict

Content: TypeAlias = ContentText | ContentTranscription
"""The content of the Communication using type field for discrimination."""

ContentDict: TypeAlias = ContentTextDict | ContentTranscriptionDict
