import json
import re
import sys

class Config:
    def __init__(self, json_data):
        self.json_data = json_data
        self.constants = {}

    def translate(self):
        return self._process_dict(self.json_data)

    def _process_value(self, value):
        if isinstance(value, str):
            if re.match(r'^\$\(.*\)$', value):
                constant_name = value[2:-1]
                if constant_name not in self.constants:
                    raise ValueError(f"Undefined constant: {constant_name}")
                return str(self.constants[constant_name])
            return f'"{value}"'
        return str(value)


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]