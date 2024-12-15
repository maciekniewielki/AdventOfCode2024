from Common import *


def get_fixed_update_value(update, lookup):
    # Create copies of data structures
    current_update = update[:]
    current_lookup = get_relevant_rules(update, lookup)

    # While our update is broken
    while get_update_value(current_update, current_lookup) == 0:
        # Get only numbers that don't have a preceding rule
        no_rule_nums = [
            num
            for num in current_update
            if (num not in current_lookup) or not len(current_lookup[num])
        ]
        rule_nums = [num for num in current_update if num not in no_rule_nums]
        # Update the lookup, removing the no rule numbers from other rules as they will be satisfied
        # Once the no rule number go first
        current_lookup = {
            k: set(v) - set(no_rule_nums) for k, v in current_lookup.items()
        }
        current_update = no_rule_nums + rule_nums

    return get_update_value(current_update, current_lookup)


def get_relevant_rules(update, lookup):
    return {k: set(v) & set(update) for k, v in lookup.items() if k in update}


def get_update_value(update, lookup):
    if update_matches_rules(update, lookup):
        return update[len(update) // 2]
    return 0


def update_matches_rules(update, lookup):
    seen = set()
    for num in update:
        if num in lookup:
            # Get the number that should have appeared before, filtered by what is actually in the update
            nums_before_current = lookup[num] & set(update)
            if not nums_before_current.issubset(seen):
                return False
        seen.add(num)
    return True


def solve1(updates, lookup):
    return sum(get_update_value(update, lookup) for update in updates)


def solve2(updates, lookup):
    return sum(
        get_fixed_update_value(update, lookup)
        for update in updates
        if get_update_value(update, lookup) == 0
    )


# IO
def create_lookup(rules):
    lookup = {}
    for rule in rules:
        if rule[1] not in lookup:
            lookup[rule[1]] = {rule[0]}
        else:
            lookup[rule[1]].add(rule[0])
    return lookup


chunks = input_as_chunks("input.txt")
rules = [(int(x), int(y)) for x, y in map(lambda s: s.split("|"), chunks[0])]
updates = [[int(x) for x in rule] for rule in map(lambda s: s.split(","), chunks[1])]
lookup = create_lookup(rules)


# 1st
print(solve1(updates, lookup))


# 2nd
print(solve2(updates, lookup))
