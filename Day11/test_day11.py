from day11 import *

class TestDay11:
    def setup_method(self, method):
        input_file = """
        aaa: you hhh
        you: bbb ccc
        bbb: ddd eee
        ccc: ddd eee fff
        ddd: ggg
        eee: out
        fff: out
        ggg: out
        hhh: ccc fff iii
        iii: out
        """.splitlines()
        self.input = [line.strip() for line in input_file if line.strip()]
        self.test_network = Network(input_file=self.input)

    def test_paths_to_you(self):
        num_paths: int = self.test_network.num_paths_to_you()
        assert num_paths == 5

