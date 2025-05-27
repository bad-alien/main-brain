#!/usr/bin/env python3
# type: ignore
import argparse
import os
import sys
import yaml
import subprocess
from typing import Dict, Any, Optional
# Add the data/scripts directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data", "scripts"))
from prompt_system.core import PromptBuilder
from prompt_system.utils import ensure_directory

def load_yaml_file(path: str) -> Dict[str, Any]:
    """Load data from a YAML file."""
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_course_files() -> list[str]:
    """Get list of available course files."""
    classes_dir = "data/classes"
    return [f for f in os.listdir(classes_dir) if f.endswith('.yaml')]

def select_course() -> Optional[Dict[str, Any]]:
    """Interactive course selection."""
    courses = get_course_files()
    if not courses:
        print("No course files found in data/classes/")
        return None
    
    print("\nAvailable courses:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course[:-5]}")  # Remove .yaml extension
    
    while True:
        try:
            choice = int(input("\nSelect a course (number): ")) - 1
            if 0 <= choice < len(courses):
                course_path = os.path.join("data/classes", courses[choice])
                return load_yaml_file(course_path)
        except ValueError:
            pass
        print("Invalid selection. Please try again.")

def get_field_value(field_name: str, required: bool, fields: Dict[str, Any]) -> Any:
    """Get field value from existing fields or user input."""
    if field_name in fields:
        return fields[field_name]
    
    prompt = f"Enter {field_name}"
    if required:
        prompt += " (required)"
    prompt += ": "
    
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print(f"Error: {field_name} is required.")

def parse_args():
    parser = argparse.ArgumentParser(description="Prompt Builder CLI")
    parser.add_argument(
        "--config",
        default="data/config/prompt_types.yaml",
        help="Path to prompt types configuration file"
    )
    parser.add_argument(
        "--templates-dir",
        default="prompts",
        help="Directory containing prompt templates"
    )
    parser.add_argument(
        "--contexts-dir",
        default="contexts",
        help="Directory containing context files"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List available prompt types")
    
    # Build command
    build_parser = subparsers.add_parser("build", help="Build a prompt from a template")
    build_parser.add_argument("type", help="Type of prompt to build")
    build_parser.add_argument("template", help="Name of the template to use")
    build_parser.add_argument("--output", help="Output file (default: stdout)")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new template")
    create_parser.add_argument("type", help="Type of prompt to create")
    create_parser.add_argument("name", help="Name for the new template")
    
    return parser.parse_args()

def copy_to_clipboard(text: str) -> None:
    """Copy text to system clipboard using pbcopy."""
    try:
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(text.encode('utf-8'))
        print("\nPrompt has been copied to clipboard!")
    except Exception as e:
        print(f"\nFailed to copy to clipboard: {str(e)}")

def main():
    args = parse_args()
    
    # Ensure directories exist
    ensure_directory(os.path.dirname(args.config))
    ensure_directory(args.templates_dir)
    ensure_directory(args.contexts_dir)
    
    # Initialize prompt builder
    builder = PromptBuilder(args.config)
    
    if args.command == "list":
        # List available prompt types
        types = builder.list_available_types()
        print("\nAvailable prompt types:")
        for prompt_type in types:
            config = builder.get_prompt_type(prompt_type)
            print(f"\n{prompt_type}:")
            print(f"  Description: {config['description']}")
            print("  Required fields:")
            for field in config['required_fields']:
                print(f"    - {field}")
            if 'optional_fields' in config:
                print("  Optional fields:")
                for field in config['optional_fields']:
                    print(f"    - {field}")
                    
    elif args.command == "build":
        # Load template
        template_path = os.path.join(args.templates_dir, args.type, f"{args.template}.yaml")
        template_data = load_yaml_file(template_path)
        
        # Get course data if available
        course_data = select_course()
        
        # Initialize fields with course data
        fields = {}
        if course_data:
            # Map specific fields from course data
            field_mapping = {
                'name': 'course',
                'subject': 'subject',
                'level': 'level',
                'course_description': 'course_description',
                'textbook': 'textbook',
                'learning_objectives': 'learning_objectives'
            }
            for course_field, template_field in field_mapping.items():
                if course_field in course_data:
                    fields[template_field] = course_data[course_field]
        
        # Get any missing required fields
        for field in template_data['fields']:
            field_name = field['name']
            if field_name not in fields:
                fields[field_name] = get_field_value(
                    field_name,
                    field.get('required', False),
                    fields
                )
        
        # Build the prompt
        prompt = builder.build_prompt(
            args.type,
            template_path,
            fields
        )
        
        # Output the result
        if args.output:
            with open(args.output, 'w') as f:
                f.write(prompt)
        else:
            print("\nGenerated Prompt:\n")
            print(prompt)
            
        # Copy to clipboard
        copy_to_clipboard(prompt)
            
    elif args.command == "create":
        # Create a new template
        template_dir = os.path.join(args.templates_dir, args.type)
        ensure_directory(template_dir)
        
        template_path = os.path.join(template_dir, f"{args.name}.yaml")
        if os.path.exists(template_path):
            print(f"Error: Template {args.name} already exists for type {args.type}")
            sys.exit(1)
            
        # Get the prompt type configuration
        prompt_config = builder.get_prompt_type(args.type)
        
        # Create a basic template structure
        template = {
            "template": "# Add your template here\n",
            "config": {
                "description": f"Template for {args.type}"
            }
        }
        
        with open(template_path, 'w') as f:
            yaml.dump(template, f, default_flow_style=False)
            
        print(f"Created new template: {template_path}")
        print("Edit the file to add your template content and configuration.")
        
    else:
        print("Error: No command specified")
        sys.exit(1)

if __name__ == "__main__":
    main() 