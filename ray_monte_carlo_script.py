import ray
import random

@ray.remote
def monte_carlo_pi(n: int) -> float:
  """Estimate pi via the Monte Carlo method."""
  in_circ_cnt = 0
  for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x * x + y * y) < 1:
      in_circ_cnt += 1

  return 4 * in_circ_cnt / n


if __name__ == "__main__":
  import argparse
  import time
  from math import pi

  parser = argparse.ArgumentParser()
  parser.add_argument("--points", type=int, default=10_000_000)
  parser.add_argument("--jobs", type=int, default=10)
  args = parser.parse_args()

  start = time.time()
  pi_refs = [monte_carlo_pi.remote(args.points) for _ in range(args.jobs)]
  pi_estimates = ray.get(pi_refs)

  print(f"Elapsed time {time.time() - start :.1f} sec")
  best_est = sum(pi_estimates) / args.jobs
  print(pi_estimates)
  print(f"Mean estimate: {best_est}, diff from builtin: {abs(best_est - pi)}")
  print(f"Estimated from {args.points * args.jobs} random points")
