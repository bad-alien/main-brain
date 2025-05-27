# Main Brain - Prompt Builder System

A flexible and modular system for building and managing AI prompts for various purposes including tutoring, code review, research, and technical communication. The system is designed to generate consistent, well-structured prompts while maintaining context and reusability.

## Features

- **Modular Prompt Types**: Support for various interaction types (tutoring, coding, research, etc.)
- **Course Integration**: Seamless integration with course materials and learning objectives
- **Template System**: YAML-based templates with field validation
- **Clipboard Support**: Automatically copies generated prompts to clipboard
- **Interactive CLI**: User-friendly command-line interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bad-alien/main-brain.git
cd main-brain
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Building Prompts

The main script `prompt_builder.py` supports several commands:

1. **List available prompt types**:
```bash
python prompt_builder.py list
```

2. **Build a prompt** (with interactive field input):
```bash
python prompt_builder.py build <type> <template>

# Example for tutoring:
python prompt_builder.py build tutoring walkthrough
```

3. **Create a new template**:
```bash
python prompt_builder.py build <type> <name>
```

### Available Templates

#### Tutoring
- `walkthrough.yaml`: Interactive Socratic dialogue template
- `math_tutor.yaml`: Mathematics-focused tutoring
- `checkanswer.yaml`: Solution verification and feedback

#### Research
- `breakdown.yaml`: Research topic analysis
- `quicksum.yaml`: Quick research summaries

#### Coding
- `code_review.yaml`: Code review and feedback
- `python_review.yaml`: Python-specific code review

## Directory Structure

```
.
├── prompt_builder.py     # Main CLI script
├── prompts/             # Prompt templates
│   ├── tutoring/
│   ├── coding/
│   ├── research/
│   └── communication/
├── data/
│   ├── classes/         # Course configurations
│   └── config/          # System configuration
└── requirements.txt     # Python dependencies
```

## Template Structure

Templates are YAML files with the following structure:

```yaml
name: "template_name"
description: "Template purpose and usage"

fields:
  - name: "field_name"
    required: true/false

template: |
  Your template content here with
  {field_name} placeholders
```

## Course Integration

Course information is stored in `data/classes/` as YAML files:
- Course details
- Learning objectives
- Textbook information
- Subject-specific configurations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details
