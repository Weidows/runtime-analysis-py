import time
import pytest
from runtime_analysis.decorator import analyze, PerformanceAnalyzer
from runtime_analysis.storage import PerformanceStorage
from runtime_analysis.visualization import PerformanceVisualizer

storage = PerformanceStorage()
analyzer = PerformanceAnalyzer(storage)

@analyzer
def example_function(duration: float):
    """Example function for testing"""
    time.sleep(duration)
    return duration

def test_decorator_basic():
    """Test basic decorator functionality"""
    storage.clear()

    # Execute function
    result = example_function(0.1)

    # Verify result
    assert result == 0.1

    # Verify data collection
    data = storage.get_all()
    assert len(data) == 1
    assert data[0]['function_name'] == 'example_function'
    assert isinstance(data[0]['execution_time'], float)

def test_visualization():
    """Test visualization functionality"""
    storage = PerformanceStorage()
    storage.clear()

    # Execute function multiple times
    for _ in range(5):
        example_function(0.05)

    # Test visualization
    visualizer = PerformanceVisualizer(storage)
    visualizer.plot_execution_time('example_function')
    visualizer.plot_resource_usage('example_function')
    visualizer.plot_io_network('example_function')

if __name__ == "__main__":
    pytest.main()
