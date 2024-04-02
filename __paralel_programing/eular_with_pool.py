import multiprocessing
import random
import math

def monte_carlo_estimate(iterations):
    count_inside_circle = 0

    for _ in range(iterations):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            count_inside_circle += 1

    return count_inside_circle

def estimate_euler_number(num_processes, total_iterations):
    iterations_per_process = total_iterations // num_processes

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(monte_carlo_estimate, [iterations_per_process] * num_processes)

    total_inside_circle = sum(results)
    total_iterations = num_processes * iterations_per_process

    estimated_ratio = total_inside_circle / total_iterations
    estimated_euler = estimated_ratio * 4  # The ratio in a quarter circle

    return estimated_euler

if __name__ == "__main__":
    num_processes = 4
    total_iterations = 1000000

    estimated_euler = estimate_euler_number(num_processes, total_iterations)

    print(f"Estimated Euler's number (e): {estimated_euler}")
