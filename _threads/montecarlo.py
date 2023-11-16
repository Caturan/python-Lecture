import random

def next_pi() -> float:
    total = 0
    inner = 0
    while True:
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            inner += 1
        total += 1
        yield((inner / total) * 4)

def main() -> None:
    random.seed(7)
    pi = next_pi()
    for i in range(10000):
        print(f"i={i:3d} pi={next(pi):.6f}")

if __name__ == "__main__":
    main()