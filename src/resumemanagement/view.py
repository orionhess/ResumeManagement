from resumemanagement.controller import Controller


class View:
    def __init__(self, controller: Controller) -> None:
        self.__controller: Controller = controller
        pass

    def validate_items(self, items: list[dict]) -> bool:
        for item in items:
            if not ("text" in item.keys() and "selected" in item.keys()):
                return False
        return True

    def print_sections(self) -> None:
        """Print the options for sections of the resume"""
        for i, section in enumerate(self.__controller.get_sections(), start=1):
            selected = " "
            if section["selected"]:
                selected = "x"

            print(f"[{selected}] {i}) {section['text']}")

    def print_items(self, section: str):
        """Print the items within a given section"""
        for i, item in enumerate(self.__controller.get_items(section), start=1):
            selected = " "
            if item["selected"]:
                selected = "x"

            print(f"[{selected}] {i}) {item['text']}")

    def get_section(self) -> str:
        """Select a section, returning a boolean for status"""
        self.print_sections()
        section_index = -1
        while True:
            try:
                section_index = int(input("Which section to select? 0 to exit"))
                break
            except ValueError:
                print("That is not a valid selection")

        if section_index == 0:
            return ""

        sections = self.__controller.get_sections()
        if len(sections) < section_index - 1:
            return ""
        section = sections[section_index - 1]

        return section["text"]

    def select_item(self, section: str) -> bool:
        """Select an item within a section, returning a boolean for status"""
        self.print_items(section)
        section_index = -1
        while True:
            try:
                section_index = int(input("Which item to select? 0 to exit -> "))
                break
            except ValueError:
                print("That is not a valid selection")

        if section_index == 0:
            return False

        items = self.__controller.get_items(section)
        if len(items) < section_index - 1:
            return False
        item = items[section_index - 1]

        self.__controller.toggle_section_item_status(section, item)
        return True

    def print_active(self) -> None:
        for section in self.__controller.get_sections_active():
            print(f"{section['text']}")
            for item in self.__controller.get_items_active(section["text"]):
                print(f"  {item['text']}")

    def add_section(self) -> None:
        section_name = input("What is the name of the new section? -> ")
        self.__controller.add_section(section_name)

    def remove_section(self) -> None:
        self.print_sections()
        section_index = -1
        while True:
            try:
                section_index = int(input("Which section to remove? 0 to exit -> "))
                break
            except ValueError:
                print("That is not a valid selection")

        if section_index == 0:
            return

        sections = self.__controller.get_sections()
        if len(sections) < section_index - 1:
            return
        section = sections[section_index - 1]

        self.__controller.remove_section(section["text"])

    def add_item(self, section: str) -> None:
        item_name = input("What is the text in this item? -> ")
        self.__controller.add_item(section, item_name)

    def remove_item(self, section: str) -> None:
        self.print_items(section)
        item_index = -1
        while True:
            try:
                item_index = int(input("Which item to remove? 0 to exit"))
                break
            except ValueError:
                print("That is not a valid item")

        if item_index == 0:
            return

        items = self.__controller.get_items(section)
        if len(items) < item_index - 1:
            return
        item = items[item_index - 1]

        self.__controller.remove_item(section, item["text"])

