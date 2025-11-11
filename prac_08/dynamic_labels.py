"""
CP1404 - Practical
Dynamic labels program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that displays a list of names as dynamically created Labels."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Connor", "Lindsay", "jd111696"]

    def build(self):
        """Build the GUI from kv file and create labels."""
        self.title = "Dynamic Labels Example"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels from list of names and add them to layout."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        """Clear all Labels."""
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
