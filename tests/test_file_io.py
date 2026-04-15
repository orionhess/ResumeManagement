from resumemanagement.controller import Controller
from resumemanagement.file_io import save_to_json, load_from_json
import os
import json

def test_save_and_load_round_trip(tmp_path):
    data = [
        {"text": "A", "selected": True},
        {"text": "B", "selected": False}
    ]
    file_path = tmp_path / "test.json"
    save_to_json(data, file_path)
    loaded = load_from_json(file_path)
    assert loaded == data


def test_save_creates_file(tmp_path):
    data = [{"text": "Hello", "selected": True}]
    file_path = tmp_path / "output.json"
    save_to_json(data, file_path)
    assert os.path.exists(file_path)


def test_load_valid_file(tmp_path):
    data = [{"text": "Test", "selected": False}]
    file_path = tmp_path / "input.json"
    # manually write file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    loaded = load_from_json(file_path)
    assert loaded == data


def test_load_nonexistent_file():
    result = load_from_json("nonexistent_file.json")
    assert result is None


def test_empty_list(tmp_path):
    data = []
    file_path = tmp_path / "empty.json"
    save_to_json(data, file_path)
    loaded = load_from_json(file_path)
    assert loaded == []