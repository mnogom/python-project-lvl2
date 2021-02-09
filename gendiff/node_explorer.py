"""Module has predicates to explore nodes."""


def is_leaf(node):
    """Predicate to check if node is leaf."""

    return not is_branch(node)


def is_branch(node):
    """Predicate to check if node is branch."""

    return isinstance(node, dict)


def has_key(key, node):
    """Predicate to check if node have selected key."""

    return key in node.keys()


def have_child(node):
    """Predicate to check if node have child."""

    return isinstance(node, dict)
