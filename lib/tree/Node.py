from itertools import chain


class Node():
    full_path = None


    def __init__(self, name="/", parent=None):
        self.parent = parent
        self.children = Children()
        self.name = name
        self.access = False
        self.status = 404
        self.depth = None


    def get_name(self):
        return self.name


    def get_status(self):
        return self.status


    def get_depth(self):
        if self.depth is None:
            p = self.parent
            depth = 0
            try:
                while p is not None:
                    p = p.parent

                    depth += 1
            except Exception:
                pass
            finally:
                self.depth = depth
        return self.depth


    def is_access(self):
        return self.access


    def set_access(self, flag=True):
        self.access = flag


    def set_parent(self, _parent=None):
        self.parent = _parent


    def add_child(self, _child=None):
        if isinstance(_child, Node) and _child.name == "":
            return None

        if isinstance(_child, str):
            if _child == "":
                return None
            check_child = self.has_child(_child)
            if check_child is not None:
                return check_child
            _child = Node(_child, parent=self)
        self.children[_child.name] = _child

        return _child


    def set_status(self, status):
        self.status = status


    def get_full_path(self):
        if self.full_path is None:
            full_path = self.name
            p = self.parent
            try:
                while 1:
                    full_path = p.name + "/" + full_path
                    p = p.parent
            except Exception:
                if full_path[:2] == "//":
                    self.full_path = full_path[1:]
                else:
                    self.full_path = full_path

        return self.full_path


    def has_child(self, name):
        if name in self.children.keys():
            return self.children[name]
        return None


    def is_root(self):
        return True if self.parent is None else False


    def is_leaf(self):
        return (not self.children) is True


    def __eq__(self, other):
        return self.name == other.name


    def __hash__(self):
        return hash(self.name)


    def __iter__(self):
        # Pre-order travel
        yield self
        for v in chain(*map(iter, self.children.values())):
            yield v


    def __str__(self):
        return self.name


class Children(dict):

    def get(self, name):
        return self[name]


    def add(self, object):
        if isinstance(object, Node):
            self[object.name] = object


    def __iter__(self):
        for node in self.values():
            yield node


if __name__ == "__main__":
    pass