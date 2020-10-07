import requests
import json

endpoint = "http://localhost:8080"

def compute_next_notes(midi_data, duration=4):
  headers = {
    'Content-Type': 'application/json',
  }

  print(midi_data)

  response = requests.post(f'{endpoint}/predict', headers=headers, data=json.dumps(midi_data))
  return response.json()


midi_data = {
  "pitches": [60,60,61,62],
  "start_times": [0,1,2,3],
  "durations": [1,1,1,2],
  "tempo": 120,
  "total_seconds": 100
}
next_notes = compute_next_notes(midi_data)
print(next_notes)