cmp_count = 0


class Node:
    def __init__(self):
        self.edges = []
        self.leaf = -1
        self.link = 0
        self.parent = -1
        self.char = ''


def search(text, pattern):
    global cmp_count
    cmp_count = 0
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return (0, cmp_count)
    if text_size == 0 or pattern_size > text_size:
        return (-1, cmp_count)
    a = AhoKorasick()
    a.add_pattern(pattern=pattern)
    a.set_links()
    e = a.search(text)[0][1]
    return (e, cmp_count)


class AhoKorasick:

    def __init__(self):
        node = Node()
        self.nodes = [node]
        self.patterns = []

    def add_pattern(self, pattern):
        v = 0
        if len(pattern) == 0:
            return
        for i in range(len(pattern)):
            next_step = -1
            for x in self.nodes[v].edges:
                if pattern[i] == self.nodes[x].char:
                    next_step = x
                    break
            if next_step == -1:
                new_node = Node()
                new_node.parent = v
                new_node.char = pattern[i]

                self.nodes.append(new_node)
                next_step = len(self.nodes) - 1
                self.nodes[v].edges.append(next_step)

            v = next_step
        self.patterns.append(pattern)
        self.nodes[v].leaf = len(self.patterns) - 1

    def set_links(self):
        queue = [0]
        while len(queue) != 0:
            node_id = queue[0]
            queue.pop(0)
            for x in self.nodes[node_id].edges:
                if self.nodes[x].parent != 0:
                    node = self.nodes[x]
                    parent_link = self.nodes[node.parent].link
                    for y in self.nodes[parent_link].edges:
                        if node.char == self.nodes[y].char:
                            self.nodes[x].link = y
                            break
                    if self.nodes[x].link == 0:
                        if self.nodes[x].char == self.nodes[parent_link].char:
                            self.nodes[x].link = parent_link
                        else:
                            for y in self.nodes[0].edges:
                                if self.nodes[x].char == self.nodes[y].char:
                                    self.nodes[x].link = y

                queue.append(x)

    def search(self, text):
        global cmp_count
        text_size = len(text)
        if text_size == 0:
            return -1
        ans = []
        v = 0
        i = 0
        while True:
            if self.nodes[v].leaf != -1:
                ans.append((self.patterns[self.nodes[v].leaf], i - len(self.patterns[self.nodes[v].leaf])))

            if self.nodes[self.nodes[v].link].leaf != -1:
                ans.append((self.patterns[self.nodes[self.nodes[v].link].leaf],
                         i - len(self.patterns[self.nodes[self.nodes[v].link].leaf])))

            if i == text_size:
                break

            next_step = -1
            for x in self.nodes[v].edges:
                cmp_count += 1
                if text[i] == self.nodes[x].char:
                    next_step = x
                    break

            if next_step == -1:
                if v == 0:
                    i += 1
                v = self.nodes[v].link
            else:
                v = next_step
                i += 1
        return ans
