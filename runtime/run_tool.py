import json
import subprocess
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(ROOT, "registry", "tools.json")

with open(REGISTRY_PATH) as f:
    registry = json.load(f)

tool = registry["tools"][0]

tool_path = os.path.join(ROOT, tool["path"], tool["entryPoint"])

print(f"Running tool: {tool['name']}")

subprocess.run(["python3", tool_path])
