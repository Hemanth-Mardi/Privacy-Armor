
from client import EnvClient

client = EnvClient()

obs = client.reset()
print("Initial:", obs)

done = False
total_reward = 0

pii_candidates = ["john@gmail.com", "9876543210"]

for pii in pii_candidates:
    res = client.step({
        "action_type": "redact",
        "target_text": pii
    })
    total_reward += res["reward"]

res = client.step({"action_type": "submit"})
total_reward += res["reward"]

print("Final:", res)
print("Total Reward:", total_reward)
