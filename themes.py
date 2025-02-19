class ThemeManager:
    def __init__(self):
        self.theme = "light"

    def set_theme(self, theme):
        """
        Установка темы оформления.
        """
        self.theme = theme
        return f"Theme set to {theme}"

    def get_theme(self):
        """
        Получение текущей темы.
        """
        return f"Current theme: {self.theme}"