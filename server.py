# 
# Copyright 2016 Google Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

from predict import generate_midi

from flask import request
import json

from flask import Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    midi_data = json.loads(request.data)
    #duration = float(request.args.get('duration'))
    print(midi_data)
    pitches = midi_data["pitches"]
    start_times = midi_data["start_times"]
    durations = midi_data["durations"]
    tempo = midi_data["tempo"]
    total_seconds = midi_data["total_seconds"]
    ret_midi = generate_midi(pitches, start_times, durations, tempo, total_seconds)
    return json.dumps(ret_midi)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
