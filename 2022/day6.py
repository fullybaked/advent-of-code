import os
import sys

from aocd import lines

example = ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]


def parse_message(enc_message: str, window_size: int):
    unique = set()

    for i in range(len(enc_message) - (window_size + 1)):
        unique.clear()

        for j in range(i, i + window_size):
            unique.add(enc_message[j])

        if len(unique) == window_size:
            return i + window_size


def part_1(data):
    packet_start = parse_message(data[0], 4)
    print(f"Packet starts at character [{packet_start}]")


def part_2(data):
    message_start = parse_message(data[0], 14)
    print(f"Message starts at character [{message_start}]")


if __name__ == "__main__":
    part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    debug = bool(os.environ.get("DEBUG", False))
    data = example if debug else lines

    locals()[f"part_{part}"](data)
