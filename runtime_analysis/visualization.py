import matplotlib.pyplot as plt
from typing import List, Dict

class PerformanceVisualizer:
    def __init__(self, storage):
        self.storage = storage

    def plot_execution_time(self, function_name: str):
        """Plot execution time for a specific function"""
        data = self.storage.get_by_function(function_name)
        if not data:
            print(f"No data found for function: {function_name}")
            return

        times = [d['execution_time'] for d in data]
        plt.figure(figsize=(10, 6))
        plt.plot(times, marker='o')
        plt.title(f"Execution Time for {function_name}")
        plt.xlabel("Execution Count")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        plt.show()

    def plot_resource_usage(self, function_name: str):
        """Plot resource usage for a specific function"""
        data = self.storage.get_by_function(function_name)
        if not data:
            print(f"No data found for function: {function_name}")
            return

        cpu_usage = [d['end_metrics']['cpu']['percent'] for d in data]
        memory_usage = [d['end_metrics']['memory']['percent'] for d in data]

        plt.figure(figsize=(10, 6))
        plt.plot(cpu_usage, label='CPU Usage (%)', marker='o')
        plt.plot(memory_usage, label='Memory Usage (%)', marker='s')
        plt.title(f"Resource Usage for {function_name}")
        plt.xlabel("Execution Count")
        plt.ylabel("Usage (%)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_io_network(self, function_name: str):
        """Plot IO and Network usage for a specific function"""
        data = self.storage.get_by_function(function_name)
        if not data:
            print(f"No data found for function: {function_name}")
            return

        read_bytes = [d['end_metrics']['io']['read_bytes'] for d in data]
        write_bytes = [d['end_metrics']['io']['write_bytes'] for d in data]
        bytes_sent = [d['end_metrics']['network']['bytes_sent'] for d in data]
        bytes_recv = [d['end_metrics']['network']['bytes_recv'] for d in data]

        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.plot(read_bytes, label='Read Bytes', marker='o')
        plt.plot(write_bytes, label='Write Bytes', marker='s')
        plt.title(f"IO Usage for {function_name}")
        plt.xlabel("Execution Count")
        plt.ylabel("Bytes")
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(bytes_sent, label='Bytes Sent', marker='o')
        plt.plot(bytes_recv, label='Bytes Received', marker='s')
        plt.title(f"Network Usage for {function_name}")
        plt.xlabel("Execution Count")
        plt.ylabel("Bytes")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()
