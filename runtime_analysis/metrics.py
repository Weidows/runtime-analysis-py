import psutil
import time

def collect_system_metrics():
    """Collect system performance metrics"""
    cpu_percent = psutil.cpu_percent(interval=0.1)
    memory_info = psutil.virtual_memory()
    io_counters = psutil.disk_io_counters()
    net_io_counters = psutil.net_io_counters()

    return {
        'timestamp': time.time(),
        'cpu': {
            'percent': cpu_percent,
            'count': psutil.cpu_count(logical=False),
            'logical_count': psutil.cpu_count(logical=True)
        },
        'memory': {
            'total': memory_info.total,
            'available': memory_info.available,
            'percent': memory_info.percent,
            'used': memory_info.used,
            'free': memory_info.free
        },
        'io': {
            'read_count': io_counters.read_count,
            'write_count': io_counters.write_count,
            'read_bytes': io_counters.read_bytes,
            'write_bytes': io_counters.write_bytes
        },
        'network': {
            'bytes_sent': net_io_counters.bytes_sent,
            'bytes_recv': net_io_counters.bytes_recv,
            'packets_sent': net_io_counters.packets_sent,
            'packets_recv': net_io_counters.packets_recv
        }
    }
