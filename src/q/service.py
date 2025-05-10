import subprocess
import re

def build_prompt(code_text):
    print("📝 Building the prompt for documentation generation...")
    prompt = f"""
You are a technical writer.

Generate a concise and clear documentation summary for the following code. Include a class explanation, constructor details, a section for properties (if applicable), and method descriptions. 
For each method, provide an example usage. Do not write code comments or docstrings. Just explain the structure and logic in plain English.

Code:
{code_text}

Documentation:
"""
    return prompt.strip()

def clean_q_output(output):
    print("🔧 Cleaning up the Q CLI output...")
    output = re.sub(r'```.*?```', lambda m: f'{{{{CODE_BLOCK_{hash(m.group(0))}}}}}', output, flags=re.DOTALL)
    output = re.sub(r'\x1b\[[0-9;]*m', '', output)
    output = re.sub(r'(To learn more about MCP safety.*|/help.*|ctrl.*|━━━━━━━━━━━━━━━━.*)', '', output)
    output = re.sub(r'\{\{CODE_BLOCK_(.*?)\}\}', lambda m: m.group(1), output)
    return output.strip()

def call_q_cli(prompt):
    print("🚀 Quack is thinking... Calling the Q CLI to generate documentation...")
    try:
        result = subprocess.run(
            ["q"],
            input=prompt,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print("❌ Error: Q CLI returned an error.")
            print(result.stderr)
            return "Error generating documentation."

        return clean_q_output(result.stdout)

    except FileNotFoundError:
        print("❌ Error: Q CLI is not installed. Please install Q CLI first.")
        return "Error: Q CLI is not installed."

    except Exception as e:
        print(f"❌ Exception: Something went wrong while calling Q CLI: {e}")
        return "Error generating documentation."
