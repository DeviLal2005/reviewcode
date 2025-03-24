import subprocess
import openai

openai.api_key = "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"

def analyze_code(code):
    """Execute and analyze Python code for errors and AI-based fixes."""
    errors, output = "", ""

    try:
        result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)
        output = result.stdout
        if result.stderr:
            errors = result.stderr
    except Exception as e:
        errors = str(e)

    # AI-Based Fix Suggestion
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI code fixer."},
            {"role": "user", "content": f"Fix this code and improve it:\n{code}"}
        ]
    )
    fixed_code = response["choices"][0]["message"]["content"]

    return output, errors, fixed_code
import openai

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Fix this code: print(Hello)"}]
)

print(response["choices"][0]["message"]["content"])
