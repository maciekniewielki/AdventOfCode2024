# Some IO functions taken from Keirua (https://blog.keiruaprod.fr/2021/11/23/getting-ready-for-adventofcode-in-python.html)


def input_as_string(filename):
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_lines(filename):
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_2d_grid(filename):
    """Return a list of lists of input characters"""
    return [list(s) for s in input_as_lines(filename)]


def input_as_ints(filename):
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip("\n"))
    return list(map(line_as_int, lines))


def input_as_lists_of_ints(filename):
    """Return a list where each line in the input file is an element of the list, converted into an integer list"""
    lines = input_as_lines(filename)
    return [list(map(int, (line.split()))) for line in lines]


def input_as_columns(filename):
    """Return a list where each column in the input file is a element of the list"""
    lines_split = [l.split() for l in input_as_lines(filename)]
    return transpose(lines_split)


def input_as_column_ints(filename):
    """Return a list where each column in the input file is a element of the list, converted into an integer"""
    columns = input_as_columns(filename)
    return [list(map(int, col)) for col in columns]


def input_as_one_line_ints(filename):
    """Return a list where it splits the file by comma and converts each entry into an integer"""
    entries = input_as_string(filename).split(",")
    return list(map(int, entries))


def input_as_chunks(filename):
    """Return a list where each chunk of lines in the input file is an element of the list"""
    lines = input_as_lines(filename)
    chunks = []
    curr_chunk = []
    for line in lines:
        if line:
            curr_chunk.append(line)
        else:
            if curr_chunk:
                chunks.append(curr_chunk)
            curr_chunk = []
    # append last chunk
    chunks.append(curr_chunk)
    return chunks


def input_as_chunked_ints(filename):
    """Return a list where each chunk of lines in the input file is a separate list of integers"""
    chunks = input_as_chunks(filename)
    return [list(map(int, c)) for c in chunks]


def flatten(l):
    """Return a flattened list"""
    return [item for sublist in l for item in sublist]


def transpose(l):
    """Return a transposed list of lists"""
    return [list(x) for x in zip(*l)]
