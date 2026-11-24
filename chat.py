import requests

HOST = "http://localhost:11434"

r = requests.post(f"{HOST}/api/chat", json={
    "model": "SillyBot",
    "messages": [{"role": "user", "content": "I feel a bit grumpy today. What can I do?"}],
    "stream": False,
}, timeout=300)
r.raise_for_status()
print(r.json()["message"]["content"])