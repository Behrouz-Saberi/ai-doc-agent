import os
import sys
from anthropic import Anthropic

class AIDocAgent:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            print("[Warning] ANTHROPIC_API_KEY environment variable not found. Running in dry-run mode.")
            self.client = None
        else:
            self.client = Anthropic(api_key=self.api_key)

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def optimize_documentation(self, content):
        """Uses Anthropic Claude to optimize and format the markdown content."""
        if not self.client:
            return content + "\n\n<!-- [Dry-Run] Optimized by AI Doc Agent -->"

        system_prompt = (
            "You are an expert technical writer and AI assistant. "
            "Your task is to optimize the provided documentation for clarity, technical accuracy, "
            "and proper Markdown structure, while keeping code blocks completely intact."
        )

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                system=system_prompt,
                messages=[{"role": "user", "content": content}]
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error communicating with Claude API: {e}")
            sys.exit(1)

if __name__ == "__main__":
    print("Initializing AI Doc Agent...")
    agent = AIDocAgent()
    # Placeholder for test execution
