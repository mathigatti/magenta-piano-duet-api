import requests
import json

production_endpoint = "https://ai-duet-ilfqxfroaq-uc.a.run.app"
local_endpoint = "http://localhost:8080"
endpoint = production_endpoint

def compute_next_notes(pitches, durs, start_times, tempo, length=4):
    headers = {
        'Content-Type': 'application/json',
    }
    midi_data = {
      "pitches": pitches,
      "start_times": start_times,
      "durations": durs,
      "tempo": tempo,
      "length": length
    }
    response = requests.post(f'{endpoint}/predict', headers=headers, data=json.dumps(midi_data))
    return response.json()

pitches = [60,60,61,62]
start_times = [0,1,2,3]
durations = [1,1,1,2]
tempo = 120
length = 10

next_notes = compute_next_notes(pitches, durs, start_times, tempo, length)
print(next_notes)
