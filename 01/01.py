

class Day1():

    def __init__(self,
                 input_path: str="input/input.txt"):
        self.input_path: str = input_path

    def read_input(self) -> list[str]:
        with open(self.input_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def input_to_array(self, rows) -> list[int]:
        """
        Converte righe tipo 'R11', 'L47' in interi:
        - 'R' → numero positivo
        - 'L' → numero negativo
        Il valore è la parte dopo il primo carattere.
        """
        numeri = []
        for r in rows:
            direzione = r[0]
            valore = int(r[1:])
            if direzione == "L":
                numeri.append(-valore)
            elif direzione == "R":
                numeri.append(valore)
            else:
                raise ValueError(f"Direzione sconosciuta: {direzione}")
        return numeri

    def passages_at_zero(self,
                         values: list[int]):
        passages_at_zero: int = 0
        running_sum: int = 0

        for value in values:
            running_sum += value
            if running_sum % 100 == 50:
                passages_at_zero += 1

        return passages_at_zero

    def solve(self):
        input: list[str] = self.read_input()
        numeri: list[int] = self.input_to_array(input)
        passages_at_zero: int = self.passages_at_zero(numeri)
        return passages_at_zero

def main():

    day1 = Day1()
    day1_result = day1.solve()
    print("Part 1:", day1_result)


if __name__ == "__main__":
    main()