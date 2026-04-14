from resumemanagement.controller import Controller
from resumemanagement.view import View

items = [
    {"text": "something", "selected": True},
    {"text": "something else", "selected": False},
    {"text": "who knows", "selected": True},
]


def initialize_controller_object():
    controller: Controller = Controller()
    assert controller is not None


def initialize_view_object():
    controller: Controller = Controller()
    view: View = View(controller)
    assert view is not None


def test_validate_items():
    controller = Controller()
    view = View(controller)
    assert view.validate_items(items)


def test_printing_sections():
    controller = Controller()
    view = View(controller)
    view.print_sections()


def test_print_items():
    controller = Controller()
    view = View(controller)
    view.print_items(controller.get_sections()[0]["text"])
