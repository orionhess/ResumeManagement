from resumemanagement.file_io import save_to_json
from typing import Any


class Controller:
    def __init__(self, items: list, filename: str = "") -> None:
        self.__items = items
        self.__filename = filename

    def write_changes(self) -> None:
        """Write the items list to the given filename"""
        # Write nothing if empty filename
        if self.__filename == "":
            return
        save_to_json(self.__items, self.__filename)

    def get_sections(self) -> list[dict[str, Any]]:
        """Get every section"""
        return self.__items

    def get_items(self, section: str) -> list[dict[str, Any]]:
        """Get every item in a given section"""
        # Find reference to the correct section
        chosen_section = {}
        for section_iter in self.__items:
            if section_iter["text"] == section:
                chosen_section = section_iter
                break
        else:
            return []

        return chosen_section["items"]

    def toggle_section_item_status(self, section, item) -> bool | None:
        """Toggle the active status of an item within a section, returning bool for status or None on failure"""
        # Find reference to the correct section
        chosen_section = {}
        for section_iter in self.__items:
            if section_iter["text"] == section:
                chosen_section = section_iter
                break
        else:
            return None

        # Find reference to the correct item
        chosen_item = {}
        for item_iter in chosen_section["items"]:
            if item_iter["text"] == item:
                chosen_item = item_iter
                break
        else:
            return None

        # Toggle status of the item, and the environment if needed
        old_status = chosen_item["selected"]
        chosen_item["selected"] = not old_status
        # If we turned the item on, the section should be on
        if not old_status:
            chosen_section["selected"] = True
        # If we turned the item off, the section should be off if every other item is also off
        else:
            # If one of the items is on, break and fall through
            # Otherwise, trigger the else and turn the section off
            for item_iter in chosen_section["items"]:
                if item_iter["selected"]:
                    break
            else:
                chosen_section["selected"] = False

        return not old_status

    def get_sections_active(self) -> list[dict[str, Any]]:
        sections = []

        for section in self.__items:
            if section["selected"]:
                sections.append(section)

        return sections

    def get_items_active(self, section: str) -> list[dict[str, Any]]:
        # Find reference to the correct section
        chosen_section = {}
        for section_iter in self.__items:
            if section_iter["text"] == section:
                chosen_section = section_iter
                break
        else:
            return []

        items = []
        for item in chosen_section["items"]:
            if item["selected"]:
                items.append(item)

        return items

    def add_section(self, section_text: str) -> dict[str, Any]:
        """Add a section to the resume, returning the section"""
        section = {"text": section_text, "selected": False, "items": []}
        self.__items.append(section)
        return section

    def remove_section(self, section: str) -> None:
        """Remove a section from the resume"""
        # Find reference to the correct section
        for i, section_iter in enumerate(self.__items):
            if section_iter["text"] == section:
                section_index = i
                break
        else:
            return

        self.__items.pop(section_index)

    def add_item(self, section: str, item_text: str) -> dict[str, Any] | None:
        """
        Add an item to a section, returning the item or None if the section
        does not exist
        """
        # Find reference to the correct section
        chosen_section = {}
        for section_iter in self.__items:
            if section_iter["text"] == section:
                chosen_section = section_iter
                break
        else:
            return None

        item = {"text": item_text, "selected": False}
        chosen_section["items"].append(item)
        return item

    def remove_item(self, section: str, item: str) -> None:
        """Remove an item from a section"""
        # Find reference to the correct section
        chosen_section = {}
        for section_iter in self.__items:
            if section_iter["text"] == section:
                chosen_section = section_iter
                break
        else:
            return None

        for i, item_iter in enumerate(chosen_section["items"]):
            if item_iter["text"] == item:
                item_index = i
                break
        else:
            return None

        chosen_section["items"].pop(item_index)
