# Magenta Piano Duet API

Magenta developed [a cool website](https://experiments.withgoogle.com/ai/ai-duet/view/) to play piano with an AI in your browser. To make it easier to interact with this technology programatically I made a simple REST API.

![](https://lh3.googleusercontent.com/SK7iorys5N1DNR82MQVyJomG4l2c88f20yyD_7sttUZEgqF0-dFmahNqN1MUJ5eeoyD3QTsBVMmpQA6C-ISVt64glzsPBNLWyw=s850)

## How do I use it?

You need to provide general details like tempo and length of the prediction to the AI, also the previous notes you want the machine to continue (if any).

### The input data looks should like like this

```python
{'pitches': [60, 60, 61, 62], 'start_times': [0, 1, 2, 3], 'durations': [1, 1, 1, 2], 'tempo': 120, 'length': 10}
```

### The predicted value you get as output will looks like this

```python
{'pitches': [60, 60, 61, 62, 64, 60, 60, 62], 'start_times': [0.0, 1.0, 2.0, 3.0, 6.0, 7.0, 8.0, 9.0], 'durations': [1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0]}
```

### Usage examples

#### Using CURL

```bash
curl --header "Content-Type: application/json" --request POST --data '{"pitches": [60, 60, 61, 62], "start_times": [0, 1, 2, 3], "durations": [1, 1, 1, 2], "tempo": 120, "length": 10}' https://ai-duet-ilfqxfroaq-uc.a.run.app/predict
```

#### Using Python

```bash
python client.py
```

# How do I run the server locally?

## 1. Install requirements

```bash
python -m pip install -r requirements.txt
```

## 2. Run server

```bash
python server.py
```
