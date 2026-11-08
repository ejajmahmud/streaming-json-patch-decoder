"""Core Streaming JSON Patch Decoder implementation."""
import json
import re
from typing import Dict, Any, Optional


class StreamingJSONPatchDecoder:
    def __init__(self):
        self.raw_stream = ""

    def feed_chunk(self, chunk: str) -> Dict[str, Any]:
        self.raw_stream += chunk
        return self.get_partial_json()

    def get_partial_json(self) -> Dict[str, Any]:
        text = self.raw_stream.strip()
        if not text:
            return {}

        # If it parses cleanly directly, return it
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Attempt recovery by balancing quotes and braces
        repaired = text

        # Balance unclosed string quote
        if repaired.count('"') % 2 == 1:
            repaired += '"'

        # Balance brackets and braces
        open_braces = repaired.count('{') - repaired.count('}')
        open_brackets = repaired.count('[') - repaired.count(']')

        # Remove trailing comma before closing if present
        repaired = re.sub(r',\s*$', '', repaired)

        if open_brackets > 0:
            repaired += ']' * open_brackets
        if open_braces > 0:
            repaired += '}' * open_braces

        try:
            return json.loads(repaired)
        except Exception:
            return {}
