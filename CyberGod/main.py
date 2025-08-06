
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


class MainScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 20

        self.capital_input = MDTextField(
            hint_text="Enter your capital (Toman)",
            helper_text="Example: 150000000",
            helper_text_mode="on_focus",
            input_filter="int"
        )
        self.add_widget(self.capital_input)

        self.income_input = MDTextField(
            hint_text="Enter your monthly income (Toman)",
            helper_text="Example: 58000000",
            helper_text_mode="on_focus",
            input_filter="int"
        )
        self.add_widget(self.income_input)

        self.result_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary"
        )
        self.add_widget(self.result_label)

        calc_button = MDRaisedButton(
            text="Calculate",
            pos_hint={"center_x": 0.5},
            on_release=self.calculate
        )
        self.add_widget(calc_button)

    def calculate(self, instance):
        try:
            capital = float(self.capital_input.text)
            monthly_income = float(self.income_input.text)

            profit_per_100k = (monthly_income / capital) * 100_000
            monthly_profit_percent = (monthly_income / capital) * 100

            self.result_label.text = (
                f"Profit per 100,000 Toman: {profit_per_100k:,.0f} Toman\n"
                f"Monthly profit percentage: {monthly_profit_percent:.2f}%"
            )
        except:
            self.result_label.text = "Please enter valid numbers."


class CyberGodApp(MDApp):
    def build(self):
        self.title = "CyberGod"
        return MainScreen()


if __name__ == "__main__":
    CyberGodApp().run()
