import json
import os
import pytz
from datetime import datetime, timedelta


def _process_data_file(file_path: str) -> tuple[datetime | None, float | None, float | None]:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        unix_time = data.get("timestamp")
        payload = data.get("payload", {})
        temperature = payload.get("temperature")
        humidity = payload.get("humidity")

        if unix_time is not None and temperature is not None and humidity is not None:
            timestamp = datetime.fromtimestamp(unix_time / 1000, pytz.timezone('Asia/Singapore'))
            jakarta_timestamp = timestamp.astimezone(pytz.timezone('Asia/Jakarta'))
            return jakarta_timestamp, temperature, humidity
        else:
            print(f"Data missing in file: {file_path}")
            return None, None, None

    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None, None, None


def _collect_data(time_filter) -> tuple[list[datetime], list[float], list[float]]:
    times = []
    temperatures = []
    humidities = []

    for root, _, files in os.walk("data"):
        for filename in files:
            if filename.endswith(".json"):
                file_path = os.path.join(root, filename)
                timestamp, temperature, humidity = _process_data_file(file_path)

                if timestamp and temperature and humidity:
                    if time_filter(timestamp):
                        times.append(timestamp)
                        temperatures.append(temperature)
                        humidities.append(humidity)

    sorted_temp_data = sorted(zip(times, temperatures))
    sorted_humid_data = sorted(zip(times, humidities))

    sorted_times, sorted_temperatures = zip(*sorted_temp_data)
    _, sorted_humidities = zip(*sorted_humid_data)

    return sorted_times, sorted_temperatures, sorted_humidities


def realtime_data() -> tuple[list[datetime], list[float], list[float]]:
    time_threshold = datetime.now(pytz.timezone('Asia/Jakarta')) - timedelta(hours=12)
    return _collect_data(lambda t: t >= time_threshold)


def data_from_yesterday() -> tuple[list[datetime], list[float], list[float]]:
    today = datetime.now(pytz.timezone('Asia/Jakarta'))
    start = (today - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    end = (today - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=999999)
    return _collect_data(lambda t: start <= t <= end)