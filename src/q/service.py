import subprocess
import re

def build_prompt(code_text, inplace=False):
    print("📝 Building the prompt for documentation generation...")

    if inplace:
        prompt = build_prompt_for_docstring(code_text)
    else:
        prompt = build_prompt_for_documentation(code_text)
    return prompt.strip()

def build_prompt_for_docstring(code_text):
    return f"""
        You are a documentation generator AI.

        Your task is to insert docstrings into the code below. For each function, method, or class, add an appropriate docstring.
        Do not change any other part of the code. Maintain indentation and original structure.
        Do not write any comments, explanations, or any extra text outside of the docstrings.

        Code:
        {code_text}

        The modified code with docstrings should be returned as the **only** output, nothing else:
        code:
        """

def build_prompt_for_documentation(code_text):
    return f"""
        You are a technical writer.

        Your task is to generate a clear and concise documentation summary for the following code. 
        Include a class explanation, constructor details, a section for properties (if applicable), and method descriptions. 
        For each method, provide an example usage in a ```python code block``` format. 
        Do not write any comments or explanations outside the documentation.

        Code:
        {code_text}

        Documentation should be returned as the **only** output, nothing else:
        code:
        """

def clean_q_output(output):
    print("🔧 Cleaning up the Q CLI output...")
    output = re.sub(r"^.*(code:|Documentation:)\n", "", output, flags=re.DOTALL)
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
