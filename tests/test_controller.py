from resumemanagement.controller import Controller

items = [
    {
        "text": "section 1",
        "selected": True,
        "items": [
            {"text": "item 1", "selected": True},
            {"text": "item 2", "selected": False},
            {"text": "item 3", "selected": True},
        ],
    },
    {
        "text": "section 2",
        "selected": False,
        "items": [
            {"text": "item 4", "selected": False},
            {"text": "item 5", "selected": False},
            {"text": "item 6", "selected": False},
        ],
    },
    {
        "text": "section 3",
        "selected": True,
        "items": [
            {"text": "item 7", "selected": True},
            {"text": "item 8", "selected": False},
            {"text": "item 9", "selected": False},
        ],
    },
]


def test_get_sections():
    controller: Controller = Controller(items)
    sections = controller.get_sections()
    assert sections == items


def test_get_items():
    controller: Controller = Controller(items)
    gotten_items = controller.get_items("section 1")
    assert gotten_items == [
        {"text": "item 1", "selected": True},
        {"text": "item 2", "selected": False},
        {"text": "item 3", "selected": True},
    ]


def test_toggle_section_item_status():
    controller: Controller = Controller(items)
    controller.toggle_section_item_status("section 1", "item 2")
    gotten_items = controller.get_items("section 1")
    assert gotten_items == [
        {"text": "item 1", "selected": True},
        {"text": "item 2", "selected": True},
        {"text": "item 3", "selected": True},
    ]


def test_toggle_section_item_status_2():
    controller: Controller = Controller(items)
    controller.toggle_section_item_status("section 3", "item 7")
    gotten_items = controller.get_items("section 3")
    assert gotten_items == [
        {"text": "item 7", "selected": False},
        {"text": "item 8", "selected": False},
        {"text": "item 9", "selected": False},
    ]
    sections = controller.get_sections()
    assert not sections[2]["selected"]
