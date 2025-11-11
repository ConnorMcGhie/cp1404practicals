"""
CP1404 - Practical
Miles to km converter
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """App that converts miles to km"""
    output_km = StringProperty()

    def build(self):
        """Build app from kv layout"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Handle conversion of miles to km"""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle the up/down button presses"""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Update output label to display converted result"""
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
