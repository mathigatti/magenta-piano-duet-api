import requests
import json

endpoint = "https://ai-duet-ilfqxfroaq-uc.a.run.app"

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

def midi2note(note):
    midi2note_dict = {int(Scale.default.get_midi_note(pitch)): pitch for pitch in range(-100,100)} # I'm going to hell for this
    if note in midi2note_dict:
        return midi2note_dict[note]
    else:
        return midi2note_dict[note-1] + 0.5

def foxdot_values(pitches, durs, length=4):
    print(pitches)
    pitches = [int(Scale.default.get_midi_note(pitch)) for pitch in list(pitches)]
    print(pitches)
    durs = list(durs)
    start_times = [sum(durs[:i]) for i in range(len(durs))]
    data = compute_next_notes(pitches, durs, start_times, int(Clock.bpm), length)
    pitches = [midi2note(int(pitch)) for pitch in data["pitches"]]
    durs = [start_2 - start_1 for start_1, start_2 in zip(data["start_times"][:-1],data["start_times"][1:])]
    sus = data["durations"]
    print(pitches,durs,sus)
    return pitches, durs, sus

# Initial values
n = 4
pitches = PWalk()[:n]
durs = PSum(n,4)
sus = durs

# Or maybe starting empty
pitches = []
durs = []
sus = []

# New values
Clock.bpm = 40
Scale.default = Scale.minor

pitches, dur, sus = foxdot_values(pitches[-16:],durs[-16:], length=64)

d1 >> ambi(pitches,dur=dur,sus=sus)

d2 >> piano(d1.pitch,dur=4,oct=4) + (0,2,4)
