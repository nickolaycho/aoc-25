import time

def get_input(input_path: str) -> list[str]:
    with open(input_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

class Node():
    def __init__(self,
        name: str,
        output: list[str]):
        self.name = name
        self.output = output
        self.parents: list[str] = []

class NodeMap():
    def __init__(self,):
        self.nodes: list[Node] = []

    def get_node(self, node_name: str) -> Node:
        for node in self.nodes:
            if node.name == node_name:
                return node
        raise AttributeError(f"Node {node_name} not found")

    def append(self, node: Node):
        self.nodes.append(node)

    def get_nodes(self) -> list[Node]:
        return self.nodes

class Network():
    def __init__(self,
         input_file: list[str],):
        self.input_file = input_file
        self.nodes: NodeMap = NodeMap()
        for line in self.input_file:
            value = line.split(":")[0].strip()
            output = line.split(":")[1].strip().split(" ")
            self.nodes.append(Node(value, output))
        self.nodes.append(Node(name="out", output= []))
        self.nodes.get_node("out").parents = []
        for node1 in self.nodes.get_nodes():
            for node2 in self.nodes.get_nodes():
                if node2.name == node1.name:
                    continue
                if node1.name in node2.output:
                    node1.parents.append(node2.name)

        self.calls = 0
        self.last_log = time.time()

    def paths_to_you(self,
             from_node: Node,
             path: list[str] = None,
             all_paths: list[list[str]] = None) -> list[list[str]]:
        if path is None:
            path = ["out"]
        if all_paths is None:
            all_paths = []

        self.calls += 1
        now = time.time()
        if now - self.last_log >= 1:
            print(f"{self.calls:,} chiamate...")
            self.last_log = now

        # evita cicli
        if from_node.name in path[:-1]:
            return all_paths

        if from_node.name=="you":
            all_paths.append(path)
            return all_paths

        else:
            current_node_parents: list[str] = (
                self.nodes.get_node(from_node.name).parents
            )
            if not current_node_parents:
                return all_paths
            for input in current_node_parents:
                updated_path = path + [(self.nodes.get_node(input).name)]
                self.paths_to_you(
                    from_node=self.nodes.get_node(input),
                    path=updated_path,
                    all_paths=all_paths
                )

            return all_paths

    def num_paths_to_you(self) -> int:
        return len(
            self.paths_to_you(
                from_node=self.nodes.get_node("out")
            )
        )