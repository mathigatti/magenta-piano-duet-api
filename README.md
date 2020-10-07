# piano-api
Piano composer API

## Install requirements

```bash
python -m pip install -r requirements.txt
```

## Run server

```bash
python server.py
```

## Run client example

```bash
python client.py
```

### The input data looks like this

```javascript
{'pitches': [60, 60, 61, 62], 'start_times': [0, 1, 2, 3], 'durations': [1, 1, 1, 2], 'tempo': 120, 'total_seconds': 100}
```

### The predicted value you get as output looks like this

```python
b"[{'pitch': 60, 'velocity': 100, 'start_time': 0.0, 'end_time': 0.5}, {'pitch': 60, 'velocity': 100, 'start_time': 0.5, 'end_time': 1.0}, {'pitch': 61, 'velocity': 100, 'start_time': 1.0, 'end_time': 1.5}, {'pitch': 62, 'velocity': 100, 'start_time': 1.5, 'end_time': 2.5}, {'pitch': 64, 'velocity': 100, 'start_time': 3.5, 'end_time': 4.0}, {'pitch': 65, 'velocity': 100, 'start_time': 4.0, 'end_time': 4.5}, {'pitch': 60, 'velocity': 100, 'start_time': 4.5, 'end_time': 5.5}, {'pitch': 59, 'velocity': 100, 'start_time': 5.5, 'end_time': 5.75}, {'pitch': 57, 'velocity': 100, 'start_time': 5.75, 'end_time': 6.0}, {'pitch': 55, 'velocity': 100, 'start_time': 6.0, 'end_time': 7.0}, {'pitch': 65, 'velocity': 100, 'start_time': 8.0, 'end_time': 8.5}, {'pitch': 60, 'velocity': 100, 'start_time': 8.5, 'end_time': 9.5}, {'pitch': 67, 'velocity': 100, 'start_time': 9.5, 'end_time': 10.0}, {'pitch': 60, 'velocity': 100, 'start_time': 10.0, 'end_time': 10.5}, {'pitch': 68, 'velocity': 100, 'start_time': 11.0, 'end_time': 11.25}, {'pitch': 68, 'velocity': 100, 'start_time': 11.25, 'end_time': 11.5}, {'pitch': 68, 'velocity': 100, 'start_time': 11.5, 'end_time': 11.75}, {'pitch': 69, 'velocity': 100, 'start_time': 11.75, 'end_time': 12.0}, {'pitch': 71, 'velocity': 100, 'start_time': 12.0, 'end_time': 14.0}, {'pitch': 67, 'velocity': 100, 'start_time': 15.0, 'end_time': 15.5}, {'pitch': 69, 'velocity': 100, 'start_time': 15.5, 'end_time': 16.0}, {'pitch': 69, 'velocity': 100, 'start_time': 16.0, 'end_time': 16.5}, {'pitch': 67, 'velocity': 100, 'start_time': 16.5, 'end_time': 16.75}, {'pitch': 68, 'velocity': 100, 'start_time': 16.75, 'end_time': 17.0}, {'pitch': 67, 'velocity': 100, 'start_time': 17.0, 'end_time': 18.25}, {'pitch': 71, 'velocity': 100, 'start_time': 19.0, 'end_time': 19.25}, {'pitch': 67, 'velocity': 100, 'start_time': 19.25, 'end_time': 19.5}, {'pitch': 64, 'velocity': 100, 'start_time': 19.5, 'end_time': 19.75}, {'pitch': 65, 'velocity': 100, 'start_time': 19.75, 'end_time': 20.0}, {'pitch': 67, 'velocity': 100, 'start_time': 20.0, 'end_time': 20.5}, {'pitch': 67, 'velocity': 100, 'start_time': 20.5, 'end_time': 21.0}, {'pitch': 64, 'velocity': 100, 'start_time': 21.0, 'end_time': 21.25}, {'pitch': 67, 'velocity': 100, 'start_time': 21.25, 'end_time': 21.5}, {'pitch': 67, 'velocity': 100, 'start_time': 21.5, 'end_time': 22.5}, {'pitch': 69, 'velocity': 100, 'start_time': 23.0, 'end_time': 23.5}, {'pitch': 68, 'velocity': 100, 'start_time': 23.5, 'end_time': 24.0}, {'pitch': 68, 'velocity': 100, 'start_time': 24.0, 'end_time': 24.25}, {'pitch': 68, 'velocity': 100, 'start_time': 24.25, 'end_time': 24.5}, {'pitch': 68, 'velocity': 100, 'start_time': 24.5, 'end_time': 24.75}, {'pitch': 68, 'velocity': 100, 'start_time': 24.75, 'end_time': 25.0}]"
```
