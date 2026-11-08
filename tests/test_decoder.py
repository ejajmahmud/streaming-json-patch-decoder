"""Unit tests for streaming-json-patch-decoder."""
import unittest
from streaming_json_patch_decoder.decoder import StreamingJSONPatchDecoder


class TestStreamingJSONPatchDecoder(unittest.TestCase):
    def test_complete_json_parse(self):
        d = StreamingJSONPatchDecoder()
        res = d.feed_chunk('{"name": "test", "val": 42}')
        self.assertEqual(res, {"name": "test", "val": 42})

    def test_partial_json_auto_repair(self):
        d = StreamingJSONPatchDecoder()
        res = d.feed_chunk('{"key": "value')
        self.assertEqual(res, {"key": "value"})

    def test_partial_nested_repair(self):
        d = StreamingJSONPatchDecoder()
        res = d.feed_chunk('{"meta": {"id": 12')
        self.assertEqual(res, {"meta": {"id": 12}})
