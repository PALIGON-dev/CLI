import json
import re
import sys

class Config:
    def __init__(self, json_data):
        self.json_data = json_data
        self.constants = {}

    def _process_dict(self, data, indent=0):
        if not isinstance(data, dict):
            raise ValueError("el is not wright")

    def translate(self):
        return self._process_dict(self.json_data)

        result = []
        for key, value in data.items():
            if not re.match(r'^[_a-zA-Z]+$', key):
                raise ValueError(f"Invalid key : {key}")

            if isinstance(value, (int, float, str)):
                result.append(f"{' ' * indent}{key} = {self._process_value(value)}")
            elif isinstance(value, dict):
                result.append(f"{' ' * indent}{key} = {{")
                result.append(self._process_dict(value, indent + 2))
                result.append(f"{' ' * indent}}}")
            else:
                raise ValueError(f"Unsupported type {key}: {type(value)}")
        return "\n".join(result)

    def _process_value(self, value):
        if isinstance(value, str):
            if re.match(r'^\$\(.*\)$', value):
                constant_name = value[2:-1]
                if constant_name not in self.constants:
                    raise ValueError(f"Unrecognised : {constant_name}")
                return str(self.constants[constant_name])
            return f'"{value}"'
        return str(value)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except Exception as e:
        print(f"Json is not opened: {e}")
        sys.exit(1)

    try:
        translator = Config(json_data)
        result = translator.translate()
        print(result)
    except Exception as e:
        print(f"Translation is wrong: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()