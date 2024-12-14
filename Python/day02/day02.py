from Common import *


def is_good_report(report, tolerate_single=False):
    variants = [report]
    if tolerate_single:
        variants = generate_all_variants(report)

    return any([are_good_diffs(calculate_diffs(variant)) for variant in variants])


def generate_all_variants(report):
    variants = []
    for i in range(len(report)):
        variants += [report[:i] + report[i + 1 :]]

    return variants


def calculate_diffs(report):
    return set(y - x for x, y in zip(report[:-1], report[1:]))


def are_good_diffs(diffs):
    good1 = {1, 2, 3}
    good2 = {-1, -2, -3}
    return diffs.issubset(good1) or diffs.issubset(good2)


def solve1(data):
    return sum(is_good_report(report) for report in data)


def solve2(data):
    return sum(is_good_report(report, tolerate_single=True) for report in data)


# IO
a = input_as_lists_of_ints("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
