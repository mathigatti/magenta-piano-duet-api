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

import os

import magenta
from magenta import music as mm
from magenta.models.melody_rnn import melody_rnn_model
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from magenta.protobuf import generator_pb2
from midiutil import MIDIFile

BUNDLE_NAME = 'attention_rnn'
config = magenta.models.melody_rnn.melody_rnn_model.default_configs[BUNDLE_NAME]
bundle_file = sequence_generator_bundle.read_bundle_file(os.path.abspath('model/' + BUNDLE_NAME+'.mag'))
steps_per_quarter = 4

generator = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
      model=melody_rnn_model.MelodyRnnModel(config),
      details=config.details,
      steps_per_quarter=steps_per_quarter,
      bundle=bundle_file)

def _steps_to_seconds(steps, qpm):
    return steps * 60.0 / qpm / steps_per_quarter


def make_midi(pitches, start_times, durations, tempo, midi_path):
    track    = 0
    channel  = 0
    time     = 0
    volume   = 100
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)

    for pitch, start_time, duration in zip(pitches,start_times,durations):
        MyMIDI.addNote(track, channel, pitch, start_time, duration, volume)

    with open(midi_path, "wb") as output_file:
        MyMIDI.writeFile(output_file)

def make_notes_sequence(pitches, start_times, durations, tempo):
    TEMP_MIDI = "temp.mid"
    make_midi(pitches, start_times, durations, tempo, TEMP_MIDI)
    return mm.midi_file_to_sequence_proto(TEMP_MIDI)

def note2dict(note):
    return {"pitch": note.pitch, "velocity": note.velocity, "start_time": note.start_time, "end_time": note.end_time}

def generate_midi(pitches, start_times, durations, tempo, total_seconds):
    primer_sequence = make_notes_sequence(pitches, start_times, durations, tempo)

    generator_options = generator_pb2.GeneratorOptions()
    # Set the start time to begin on the next step after the last note ends.
    last_end_time = (max(n.end_time for n in primer_sequence.notes)
                     if primer_sequence.notes else 0)

    qpm = tempo/2 # I'm not sure about this
    generator_options.generate_sections.add(
        start_time=last_end_time + _steps_to_seconds(1, qpm),
        end_time=_steps_to_seconds(total_seconds, qpm))

    # generate the output sequence
    generated_sequence = generator.generate(primer_sequence, generator_options)
    return [note2dict(note) for note in generated_sequence.notes]