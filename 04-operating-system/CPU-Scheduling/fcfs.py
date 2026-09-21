def fcfs(processes):
    current_time = 0
    results = []

    for process in processes:
        name = process["name"]
        burst_time = process["burst_time"]

        waiting_time = current_time
        turnaround_time = waiting_time + burst_time

        results.append({
            "name": name,
            "waiting_time": waiting_time,
            "turnaround_time": turnaround_time
        })

        current_time += burst_time

    return results


if __name__ == "__main__":
    processes = [
        {"name": "P1", "burst_time": 5},
        {"name": "P2", "burst_time": 3},
        {"name": "P3", "burst_time": 2}
    ]

    results = fcfs(processes)

    for result in results:
        print(result)