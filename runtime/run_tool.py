import json
import subprocess

with open("../registry/tools.json") as f:
    registry = json.load(f)

tool = registry["tools"][0]
path = f"../{tool['path']}/{tool['entryPoint']}"

print("Running:", tool["name"])
subprocess.run(["python", path])
