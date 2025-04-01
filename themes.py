class ThemeManager:
    """Класс для управления темами оформления интерфейса."""
    
    def __init__(self):
        self.theme = "light"

    def set_theme(self, theme):
        """Установка темы оформления.

        Args:
            theme (str): Название темы для установки.

        Returns:
            str: Сообщение о новой установленной теме.
        """
        self.theme = theme
        return f"Theme set to {theme}"

    def get_theme(self):
        """Получение текущей установленной темы.

        Returns:
            str: Информация о текущей теме.
        """
        return f"Current theme: {self.theme}"