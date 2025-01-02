from typing import Dict, List
import json
import os

class PerformanceStorage:
    def __init__(self):
        self._data = []
        self._file_path = "performance_data.json"

    def store(self, metrics: Dict):
        """Store performance metrics"""
        self._data.append(metrics)
        self._save_to_file()

    def get_all(self) -> List[Dict]:
        """Get all stored performance data"""
        return self._data

    def get_by_function(self, function_name: str) -> List[Dict]:
        """Get performance data for a specific function"""
        return [d for d in self._data if d['function_name'] == function_name]

    def clear(self):
        """Clear all stored data"""
        self._data = []
        if os.path.exists(self._file_path):
            os.remove(self._file_path)

    def _save_to_file(self):
        """Save data to file"""
        with open(self._file_path, 'w') as f:
            json.dump(self._data, f, indent=2)

    def load_from_file(self):
        """Load data from file"""
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as f:
                self._data = json.load(f)
