from resumemanagement.controller import Controller
import json

def save_to_json(data, filename):
    """Saves list of dictionaries to a JSON file"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving file: {e}")
        
def load_from_json(filename):
    """Loads list of dictionaries from a JSON file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None