from __future__ import annotations

from typing import TypeAlias

from ..content_text1 import ContentText1, ContentText1Dict
from ..content_transcription1 import ContentTranscription1, ContentTranscription1Dict

Content2: TypeAlias = ContentText1 | ContentTranscription1
"""The content of the Communication."""

Content2Dict: TypeAlias = ContentText1Dict | ContentTranscription1Dict
