from resumemanagement.controller import Controller
from resumemanagement.view import View


def main() -> None:
    print("Hello from resumemanagement!")

    controller: Controller = Controller()
    view: View = View(controller)
    view.print_active()
