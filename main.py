import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import time

timestamps = []
cpu_usage = []
memory_usage = []

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)


def update_graph():
    ax1.clear()
    ax2.clear()

    ax1.plot(timestamps, memory_usage, label="Memory Usage")
    ax1.set_ylabel("Memory Usage")
    ax1.legend()

    for i in range(len(cpu_usage[0])):
        ax2.plot(timestamps, [cpu[i] for cpu in cpu_usage], label="CPU %s" % i)
    ax2.set_ylabel("CPU Usage")

    plt.xlabel("Time")
    plt.legend()
    plt.pause(0.1)


def timer(start_time):
    end_time = datetime.now()
    duration = end_time - start_time
    mins, secs = divmod(duration.total_seconds(), 60)

    format_duration = f"{int(mins)}:{int(secs)}"

    return format_duration


def main() -> None:
    start_time = datetime.now()
    while True:
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        memory_percent = psutil.virtual_memory().percent

        timestamps.append(timer(start_time))
        cpu_usage.append(cpu_percent)
        memory_usage.append(memory_percent)

        update_graph()


if __name__ == "__main__":
    main()
