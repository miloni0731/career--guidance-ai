import json
import os
from typing import Any, Dict, Union

def load_json(file_path: str) -> Union[Dict[str, Any], list]:
    ...

    """Load data from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save data to a JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_config(config_name: str) -> Dict[str, Any]:
    """Load configuration from the configs directory."""
    config_path = os.path.join('configs', f'{config_name}.json')
    return load_json(config_path)

def save_test_case(test_case: Dict[str, Any], test_name: str) -> None:
    """Save a test case to the data directory."""
    test_path = os.path.join('data', 'test_inputs.json')
    if os.path.exists(test_path):
        test_cases = load_json(test_path)
    else:
        test_cases = {}
    
    test_cases[test_name] = test_case
    save_json(test_cases, test_path) 