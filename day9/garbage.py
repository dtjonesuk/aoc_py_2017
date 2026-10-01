from dataclasses import dataclass, field


@dataclass
class Group:
   score:int = 0
   parent: Group | None = None
   groups:list[Group] = field(default_factory=list)
   characters:str = ""

def parse_groups(s:str):
    i = 0
    root = Group(0)
    current_group = root
    in_garbage = False

    while i < len(s):
        ch = s[i]
        i += 1
        if in_garbage:
            if ch == '!':
                # ignore next char
                i += 1
                continue
            elif ch == '>':
                in_garbage = False
            else:
                current_group.characters += ch
            continue
        if ch == '<':
            in_garbage = True
            continue

        # Not in garbage
        if ch == '{':
            # begin group
            new_group = Group(current_group.score + 1, current_group)
            current_group.groups.append(new_group)
            current_group = new_group
        elif ch == '}':
            # end group
            current_group = current_group.parent
            assert(current_group is not None)

    return root
