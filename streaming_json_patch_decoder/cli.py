"""CLI for streaming-json-patch-decoder."""
import sys
import argparse
from .decoder import StreamingJSONPatchDecoder


def main():
    parser = argparse.ArgumentParser(description="Streaming JSON Patch Decoder CLI")
    parser.add_argument("--demo", action="store_true", help="Run streaming JSON patch decoding demo")
    args = parser.parse_args()

    if args.demo:
        decoder = StreamingJSONPatchDecoder()
        chunks = ['{"tool": "run_test", ', '"arguments": {"suite": "auth", ', '"timeout": 30}']
        for i, c in enumerate(chunks, 1):
            partial = decoder.feed_chunk(c)
            print(f"[+] Chunk {i} partial decode: {partial}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
