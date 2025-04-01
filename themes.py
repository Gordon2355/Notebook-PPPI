class ThemeManager:
    """Класс для управления темами оформления пользовательского интерфейса.

    Attributes:
        theme (str): Текущая тема, по умолчанию 'light'.
    """
    def __init__(self):
        self.theme = "light"

    def set_theme(self, theme):
        """Устанавливает тему оформления для приложения.

        Args:
            theme (str): Название темы для применения (например, 'light', 'dark').

        Returns:
            str: Сообщение, подтверждающее установку новой темы.
        """
        self.theme = theme
        return f"Theme set to {theme}"

    def get_theme(self):
        """Получает текущую тему оформления.

        Returns:
            str: Строка, указывающая текущую тему.
        """
        return f"Current theme: {self.theme}"