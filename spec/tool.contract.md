# OpenToolsX Tool Contract v1

## Definition
A tool is a self-contained executable defined by tool.json.

## Required fields
- id
- name
- version
- path
- entryPoint
- runtime

## Execution rule
registry → resolves tool → runtime executes entryPoint

## Supported runtime (v1)
- python only

## Rule
If a tool is not in registry, it is not part of the system
