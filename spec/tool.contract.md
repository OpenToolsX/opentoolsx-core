# OpenToolsX Tool Contract v1

A tool in OpenToolsX must follow this structure:

## Required fields (tool.json)
- id
- name
- version
- path
- entryPoint
- runtime

## Execution rule
A tool is executed by:
registry → resolving tool → runtime executing entryPoint

## Runtime support (v1)
- python only

## Entry point rule
entryPoint must be a valid executable file inside the tool folder
