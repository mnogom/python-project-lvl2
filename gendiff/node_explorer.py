"""Module have predicates to explore nodes."""


def is_leaf(node):
    """Predicate to check if node is child."""

    return not is_branch(node)


def is_branch(node):
    """Predicate to check if node is parent."""

    return isinstance(node, dict)


def have_key(key, node):
    """Predicate to check if node have selected key."""

    return key in node.keys()
