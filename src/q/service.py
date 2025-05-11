import subprocess
import re

def build_prompt(code_text, inplace=False):
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
        Do not write any comments, explanations, or any extra text outside the docstrings.

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

def call_q_cli(prompt):
    try:
        result = subprocess.run(
            ["q"],
            input=prompt,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"Q CLI returned an error:\n{result.stderr}")

        return clean_q_output(result.stdout)

    except FileNotFoundError:
        raise FileNotFoundError("Q CLI is not installed. Please install Q CLI first.")

    except Exception as e:
        raise RuntimeError(f"Something went wrong while calling Q CLI: {e}")

def clean_q_output(output, inplace=False):
    output = re.sub(r"^.*(code:|Documentation:)\n", "", output, flags=re.DOTALL)
    output = re.sub(r'```.*?```', lambda m: f'{{{{CODE_BLOCK_{hash(m.group(0))}}}}}', output, flags=re.DOTALL)
    output = re.sub(r'\x1b\[[0-9;]*m', '', output)
    output = re.sub(r'(To learn more about MCP safety.*|/help.*|ctrl.*|━━━━━━━━━━━━━━━━.*)', '', output)
    output = re.sub(r'\{\{CODE_BLOCK_(.*?)\}\}', lambda m: m.group(1), output)
    
    if inplace:
        output = clean_language_output(output)
    
    return output.strip()

def clean_language_output(output):
    """Removes the language identifier line (e.g., python) from the generated documentation."""
    output_lines = output.splitlines()
    if output_lines:
        output_lines.pop(0)
    return "\n".join(output_lines)
