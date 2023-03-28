import io
import os

import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.label import Label


class FileConverterApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_file = None
        self.selected_converter = None

    def select_file(self, selection):
        print(selection)
        print(selection[0])
        self.selected_file = selection[0]

    def convert_file(self):
        if self.selected_file and self.selected_converter:
            filename, file_ext = os.path.splitext(self.selected_file)
            new_filename = f"{filename}_converted.{self.selected_converter}"

            if self.selected_converter == "csv":
                # reads json and outputs csv
                df_json = pd.read_json(
                    self.selected_file, orient="records", lines=False
                )
                df_json.to_csv(new_filename, index=False)

            elif self.selected_converter == "json":
                # reads csv and outputs json
                df_csv = pd.read_csv(self.selected_file)
                df_csv.to_json(
                    new_filename,
                    orient="records",
                    lines=False,
                    date_format="iso",
                )

            os.rename(
                new_filename, f"{os.path.expanduser('~')}/Downloads/{new_filename}"
            )
            self.selected_file = None
            self.selected_converter = None

    def build(self):
        # Creates window application with different elements
        root = BoxLayout(orientation="vertical", padding=10)

        filechooser = FileChooserIconView(filters=["*.csv", "*.json"])
        filechooser.bind(selection=self.select_file)

        convert_label = Label(text="Convert to:")
        csv_button = Button(
            text="CSV", on_press=lambda _: setattr(self, "selected_converter", "csv")
        )
        json_button = Button(
            text="JSON", on_press=lambda _: setattr(self, "selected_converter", "json")
        )
        convert_button = Button(text="Convert", on_press=lambda _: self.convert_file())

        button_layout = BoxLayout(orientation="horizontal")
        button_layout.add_widget(csv_button)
        button_layout.add_widget(json_button)

        root.add_widget(filechooser)
        root.add_widget(convert_label)
        root.add_widget(button_layout)
        root.add_widget(convert_button)

        return root


if __name__ == "__main__":
    FileConverterApp().run()
