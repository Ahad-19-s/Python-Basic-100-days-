import argparse

parser = argparse.ArgumentParser(description="Greeting Utility")
parser.add_argument("name", help="Enter your name")
parser.add_argument("-t", "--times", type=int, default=1, help="How many times to greet")

args = parser.parse_args()

for i in range(args.times):
    print(f"Hello, {args.name}!")
