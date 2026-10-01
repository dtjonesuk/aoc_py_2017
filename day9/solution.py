import os
from lib.input import Input
from garbage import Group, parse_groups

input_path = os.path.join(str(os.path.dirname(__file__)), "input.txt")


# Root "group" is a placeholder that contains the real groups, so we count only the child groups
def get_group_count(grp: Group) -> int:
    child_groups = sum(_group_count_recursive(child) for child in grp.groups)
    return child_groups


def _group_count_recursive(grp: Group):
    child_groups = sum(_group_count_recursive(child) for child in grp.groups)
    return 1 + child_groups


def get_total_score(grp: Group) -> int:
    child_scores = sum(get_total_score(child) for child in grp.groups)
    return grp.score + child_scores


def get_character_count(grp: Group) -> int:
    child_groups = sum(get_character_count(child) for child in grp.groups)
    return len(grp.characters) + child_groups


def part1(groups):
    total = get_total_score(groups)
    return total


def part2(groups):
    total = get_character_count(groups)
    return total


if __name__ == "__main__":
    data = Input(input_path).read_lines()[0]
    groups = parse_groups(data)
    print("Part 1: ", part1(groups))
    print("Part 2: ", part2(groups))
