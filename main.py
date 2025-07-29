from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.icon = "c1.png"
        self.operators = ["/", "*", "-", "+"]
        self.last_was_operator = False

        main_layout = BoxLayout(orientation="vertical")

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55,
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=32,
                    background_color=(.3, .3, .3, 1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",
            font_size=32,
            background_color=(.2, .6, .2, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
            self.last_was_operator = False
        else:
            if current and self.last_was_operator and button_text in self.operators:
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.solution.text += button_text
                self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                self.solution.text = str(eval(text))
            except Exception:
                self.solution.text = "Error"


if __name__ == "__main__":
    MainApp().run()
