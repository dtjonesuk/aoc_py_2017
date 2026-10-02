from pyparsing import *

SOURCENODE = pyparsing_common.integer.set_results_name('source')
DESTNODE = pyparsing_common.integer
NODELIST = DelimitedList(DESTNODE).set_results_name('destinations')
LINE = SOURCENODE + Suppress('<->') + NODELIST


class Nodes:
    """Initial Nodes directly from the puzzle input"""

    def __init__(self, data):
        source_dest = lambda l: (l.source, list(l.destinations))
        self.nodes = dict(source_dest(LINE.parse_string(line)) for line in data)

    """Returns a set containing all members of a group"""

    def get_group(self, root: int):
        visited = set()

        # Keep a list of nodes to_visit (starting with root).
        # We keep track of all the nodes we visit in the visited set.
        # As we visit a node, we add the connected nodes to our to_visit list,
        #   excluding any nodes that we have already visited (to prevent cycles).

        to_visit = [root]
        while len(to_visit) > 0:
            node = to_visit.pop(0)
            visited.add(node)
            to_visit.extend(n for n in self.nodes[node] if n not in visited)
        return visited

    """Returns a list of all the groups"""

    def find_all_groups(self):
        visited = set()
        groups = list()

        # Iterate through all the possible nodes:
        #   Obtain the group membership for the current node,
        #   then mark all the nodes in that group as visited.

        for node in self.nodes.keys():
            if node not in visited:
                group = self.get_group(node)
                groups.append(group)
                visited.update(n for n in group)
        return groups
