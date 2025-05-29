# Context Files

YAML files containing reusable context for LLM interactions. These files can be referenced via their raw GitHub URLs.

## Structure

- `technical/` - Technical specifications and documentation
- `domain/` - Domain-specific knowledge
- `reference/` - Reference materials

## Usage

1. Navigate to any .yaml file
2. Click "Raw" to get the plain text version
3. Copy the URL or content into your LLM chat interface

## Format

All context files use this simple YAML structure:

```yaml
title: "Context Title"
description: "What this context is for"
content:
  key_points:
    - Point 1
    - Point 2
  references:
    - Reference 1
    - Reference 2
``` 