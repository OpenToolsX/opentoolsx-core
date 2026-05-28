# OpenToolsX Tool Contract v1

## What is a Tool?
A tool is a self-contained executable unit defined by a tool.json file.

## Required structure
Each tool MUST contain:
- id
- name
- version
- path
- entryPoint
- runtime

## Execution rule
A tool is executed ONLY through:
registry → resolve tool → runtime executes entryPoint

## Supported runtime (v1)
- python only

## Registry rule
If a tool is not listed in registry/tools.json, it does not exist in the system

## EntryPoint rule
entryPoint MUST be a valid executable file inside the tool folder
