import time
import functools
from .metrics import collect_system_metrics
from .storage import PerformanceStorage

class PerformanceAnalyzer:
    def __init__(self, storage=None):
        self.storage = storage or PerformanceStorage()

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Start timing
            start_time = time.perf_counter()

            # Collect system metrics before execution
            start_metrics = collect_system_metrics()

            # Execute the function
            result = func(*args, **kwargs)

            # Collect system metrics after execution
            end_metrics = collect_system_metrics()
            end_time = time.perf_counter()

            # Calculate execution time
            execution_time = end_time - start_time

            # Store performance data
            self.storage.store({
                'function_name': func.__name__,
                'execution_time': execution_time,
                'start_metrics': start_metrics,
                'end_metrics': end_metrics,
                'args': args,
                'kwargs': kwargs
            })

            return result
        return wrapper

# Create a global instance for easy usage
analyze = PerformanceAnalyzer()
