# Main Brain

A collection of AI prompts and tools for different use cases, from CLI-based prompt building to standalone prompts for web-based LLM interfaces.

## Components

### 1. Prompt Builder (CLI/IDE Usage)
- Located in `prompt_builder.py`
- Builds customized prompts using templates and context
- Integrates with your development environment
- Supports various prompt types (tutoring, coding, research)

### 2. Standalone Prompts (Web LLM Usage)
- Located in `prompts/collection/`
- Ready-to-use prompts for web-based LLM interfaces (ChatGPT, Claude, etc.)
- No processing required - just copy and paste
- Includes context templates in `contexts/` for enhanced interactions

## Quick Start

1. For CLI/IDE Usage:
```bash
# Clone and setup
git clone https://github.com/bad-alien/main-brain.git
cd main-brain
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Run prompt builder
python prompt_builder.py build <type> <template>
```

2. For Web LLM Usage:
- Browse `prompts/collection/` for standalone prompts
- Browse `contexts/` for additional context templates
- Copy desired prompt/context and paste into your preferred LLM interface

## License

MIT License - See LICENSE file for details
