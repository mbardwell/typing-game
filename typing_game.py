import sys
import time

import click

USR_ESC = b'\x03'
SPACE = b'\x20'
LINE = "The quick brown fox jumps over the lazy dog"

def show_line_to_type(line: str):
    print(line)

def valid_char(c: bytes):
    """only supports a-z, A-Z, space"""
    return True if c >= b'A' and c <= b'Z' or c >= b'a' and c <= b'z' or c == SPACE else False

def print_char_and_flush(c: bytes):
    if valid_char(c):
        print(c.decode(encoding="utf-8"), end='')
        sys.stdout.flush()

def read_from_input(ignore) -> bytes:
    return str.encode(click.getchar())

def interpret_character(c: bytes, expected: bytes) -> bool:
    if c == USR_ESC:
        exit(0)
    if valid_char(c) and expected == c.decode(encoding="utf-8"):
        print_char_and_flush(c)
        return True
    return False

def play(line: str, input_cb) -> float:
    """Play and return Letters Per Second (LPS)"""
    show_line_to_type(line)
    count = 0
    while count < len(line):
        count += 1 if interpret_character(input_cb(count), line[count]) else 0
        if count == 1:
            ts = time.time()

    t_run = time.time() - ts
    n_words = sum([c == " " for c in line]) + 1
    print(f"\nCompleted {n_words} words in {t_run:.2f}s. {n_words * 60 /  t_run:.2f} WPM. {len(line) / t_run:.2f} LPS")
    return len(line) / t_run
   
if __name__ == "__main__":
    play(LINE, read_from_input)