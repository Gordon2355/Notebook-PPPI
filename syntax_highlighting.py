
class SyntaxHighlighter:
    """Класс для подсветки синтаксиса кода различных языков программирования.

    Args:
        language (str): Язык программирования для подсветки.
    """
    
    def __init__(self, language):
        self.language = language

    def highlight(self, code):
        """Имитация подсветки синтаксиса для указанного кода.

        Args:
            code (str): Код для подсветки.

        Returns:
            str: Подсвеченный код с указанием языка.
        """
        return f"Highlighted {self.language} code: {code}"

    def set_language(self, language):
        """Установка языка для подсветки синтаксиса.

        Args:
            language (str): Новый язык программирования.

        Returns:
            str: Сообщение о новом установленном языке.
        """
        self.language = language
        return f"Language set to {language}"