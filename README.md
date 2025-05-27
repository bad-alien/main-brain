# Prompt Builder System

A flexible and modular system for building and managing prompts for various purposes including tutoring, code review, debate, research, and technical communication.

## Features

- Configurable prompt types with required and optional fields
- Template-based prompt generation
- Context management for reusable prompt components
- Validation system for templates and fields
- CLI interface for easy interaction

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### List Available Prompt Types
```bash
python data/scripts/prompt_builder.py list
```

### Build a Prompt
```bash
python data/scripts/prompt_builder.py build tutoring math_tutor --fields fields.yaml --context context.yaml
```

### Create a New Template
```bash
python data/scripts/prompt_builder.py create tutoring calculus_tutor
```

## Directory Structure

```
.
├── data/
│   ├── config/
│   │   └── prompt_types.yaml
│   └── scripts/
│       └── prompt_system/
│           ├── core.py
│           ├── context.py
│           ├── utils.py
│           └── validators.py
├── prompts/
│   ├── tutoring/
│   ├── coding/
│   ├── debate/
│   ├── research/
│   └── communication/
└── contexts/
```

## Configuration

Prompt types are defined in `data/config/prompt_types.yaml`. Each type specifies:
- Description
- Required fields
- Optional fields

## Templates

Templates are YAML files that define:
- The prompt template text with field placeholders
- Template-specific configuration
- Optional conditional sections

## Context Management

Contexts allow reusing common prompt components across templates:
- Store in the `contexts/` directory
- Reference in templates or during prompt building
- Support for nested context references

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License
