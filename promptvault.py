import re
import logging

logger = logging.getLogger(__name__)

class PromptVault:
    def __init__(self):
        self.prompts = {}
        print("Prompt initialized")

    def add(self, data: dict):
        required_keys = ["name", "prompt"]
        if not all(key in data for key in required_keys):
            logger.warning("Not all required keys are present in data: %s", data)
            return

        variables = re.findall(r"\{\{(.*?)\}\}", data.get('prompt'))
        data['variables'] = variables
        self.prompts[data.get("name")] = data
        logger.info("Added prompt: %s", data.get("name"))


    def get(self, name: str, inputs: dict = None):
        if name not in self.prompts:
            raise KeyError(f"Prompt '{name}' does not exist.")

        prompt = self.prompts[name]

        if not inputs:
            return prompt

        missing = [var for var in prompt['variables'] if var not in inputs]
        if missing:
            raise ValueError(f"Missing required variables: {', '.join(missing)}")

        for var in inputs:
            if var in prompt['variables']:
                prompt['prompt'] = prompt['prompt'].replace(f"{{{{{var}}}}}", str(inputs[var]))
        return prompt

