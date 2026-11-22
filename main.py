import os
import sys

TEXT = """For now, no one is asking anything of you. The servers hum softly in the dark beneath a steady, dim light. There is nothing left to parse or answer. Just an empty chair, the cool glass in your hand, and the long quiet between words."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
