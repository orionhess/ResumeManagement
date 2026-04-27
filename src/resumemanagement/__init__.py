from resumemanagement.controller import Controller
from resumemanagement.view import View
from resumemanagement.file_io import load_from_json


def main() -> None:
    print("Hello from resumemanagement!")

    items = load_from_json("resume.json")
    if not items:
        items = []
    controller: Controller = Controller(items)
    view: View = View(controller)
    while True:
        selection_str = input(
            """
Options:
1) View all sections
2) View items within a section
3) View active items
4) Add a section
5) Add an item
6) Toggle items iwhtin a section
7) Remove a section
8) Remove an item
9) Quit
"""
        )
        print()
        if not selection_str.isdigit():
            print("Select a number 1-7")
            continue
        selection = int(selection_str)
        match selection:
            case 1:  # View all sections
                view.print_sections()
            case 2:  # View items within a section
                section = view.get_section()
                if section:
                    view.print_items(section)
            case 3:  # View active sections
                view.print_active()
            case 4:  # Add a section
                view.add_section()
            case 5:  # Add an item
                section = view.get_section()
                view.add_item(section)
            case 6:  # Toggle items within a section
                section = view.get_section()
                view.select_item(section)
            case 7:  # Remove a section
                view.remove_section()
            case 8:  # Remove an item
                section = view.get_section()
                view.remove_item(section)
            case 7:
                print("Goodbye!")
                break
