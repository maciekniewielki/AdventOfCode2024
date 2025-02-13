from Common import *
from itertools import zip_longest


def compact_blocks(blocks):
    compacted = blocks[:]
    upper = len(blocks) - 1
    lower = 0
    while True:
        while compacted[lower] is not None or lower == upper:
            lower += 1
        while compacted[upper] is None or lower == upper:
            upper -= 1
        if lower >= upper:
            break
        compacted[lower], compacted[upper] = compacted[upper], compacted[lower]
    return compacted


def calc_checksum(blocks):
    return sum(
        block_id * chunk_id
        for block_id, chunk_id in enumerate(blocks)
        if chunk_id is not None
    )


def solve1(blocks):
    compacted = compact_blocks(blocks)
    return calc_checksum(compacted)


def solve2(chunks):
    pass


# IO
a = input_as_string("input.txt")
blocks = []
# Chunks waiting for part 2
# chunks = []
for file_id, space in enumerate(zip_longest(a[::2], a[1::2])):
    file_space, free_space = space
    # chunks.append((chunk_id, int(file_space)))
    blocks += [file_id] * int(file_space)
    if free_space:
        blocks += [None] * int(free_space)
        # chunks.append((None, int(free_space)))

# 1st
print(solve1(blocks))


# 2nd
# print(solve2(chunks))
