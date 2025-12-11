def read_values(filename: str) -> list[float]:
    values = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    values.append(float(line))
                except ValueError:
                    raise ValueError(f"Invalid number in file: '{line}'")
    return values

def amount_of_values(values: list[float]) -> int:
    return len(values)

def sum_of_values(values: list[float]) -> float:
    return sum(values)

def average_of_values(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0
