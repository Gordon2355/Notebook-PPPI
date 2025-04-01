class SyntaxHighlighter:
    """Класс для обработки подсветки синтаксиса для различных языков программирования.

    Args:
        language (str): Язык программирования, для которого выполняется подсветка синтаксиса.
    """
    def __init__(self, language):
        self.language = language

    def highlight(self, code):
        """Имитирует подсветку синтаксиса для переданного кода.

        Args:
            code (str): Фрагмент кода для подсветки.

        Returns:
            str: Строка с подсвеченным кодом и префиксом языка.
        """
        return f"Highlighted {self.language} code: {code}"

    def set_language(self, language):
        """Устанавливает язык для подсветки синтаксиса.

        Args:
            language (str): Новый язык для подсветки.

        Returns:
            str: Сообщение, подтверждающее установку нового языка.
        """
        self.language = language
        return f"Language set to {language}"