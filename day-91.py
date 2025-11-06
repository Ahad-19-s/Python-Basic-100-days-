from functools import lru_cache
import time

# Cache up to 3 previous results
@lru_cache(maxsize=3)
def expensive_computation(x):
    print(f"Computing {x}...")
    time.sleep(2)  # Simulate long computation
    return x * x

# First call → computes and caches
print(expensive_computation(5))  # Computing 5... then prints 25

# Second call with same argument → returns cached result instantly
print(expensive_computation(5))  # No "Computing..." print, instantly returns 25

# New argument → computes again
print(expensive_computation(6))  # Computing 6... then prints 36
