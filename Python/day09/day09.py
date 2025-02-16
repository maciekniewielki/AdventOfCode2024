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


def compact_chunks(chunks):
    highest_id = max(filter(lambda c: c[0] is not None, chunks), key=lambda c: c[0])[0]
    for id in range(highest_id, 0, -1):
        try_insert_chunk(chunks, id)
    return chunks


def try_insert_chunk(chunks, chunk_id):
    upper = None
    for i in range(len(chunks) - 1, 0, -1):
        if chunks[i][0] == chunk_id:
            upper = i

    for lower in range(upper):
        if chunks[lower][0] is None and chunks[lower][1] == chunks[upper][1]:
            # File is just the right size, just swap places
            chunks[lower], chunks[upper] = chunks[upper], chunks[lower]
            break
        elif chunks[lower][0] is None and chunks[lower][1] > chunks[upper][1]:
            # File is smaller than free space
            free_space_left = chunks[lower][1] - chunks[upper][1]
            # Insert whole file into the free space and free space into file
            chunks[lower], chunks[upper] = chunks[upper], (None, chunks[upper][1])
            # Add leftover free space after the file
            chunks.insert(lower + 1, (None, free_space_left))
            break


def calc_checksum(blocks):
    return sum(
        block_id * chunk_id
        for block_id, chunk_id in enumerate(blocks)
        if chunk_id is not None
    )


def blockify(chunks):
    blocks = []
    for chunk in chunks:
        blocks += [chunk[0]] * chunk[1]
    return blocks


def solve1(chunks):
    blocks = blockify(chunks)
    compacted_blocks = compact_blocks(blocks)
    return calc_checksum(compacted_blocks)


def solve2(chunks):
    compacted_chunks = compact_chunks(chunks)
    compacted_blocks = blockify(compacted_chunks)
    return calc_checksum(compacted_blocks)


# IO
a = input_as_string("input.txt")


chunks = []
for file_id, space in enumerate(zip_longest(a[::2], a[1::2])):
    file_space, free_space = space
    chunks.append((file_id, int(file_space)))
    if free_space:
        chunks.append((None, int(free_space)))

# 1st
print(solve1(chunks))


# 2nd
print(solve2(chunks))
