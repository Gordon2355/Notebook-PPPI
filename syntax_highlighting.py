class SyntaxHighlighter:
    def __init__(self, language):
        self.language = language

    def highlight(self, code):
        """
        Имитация подсветки синтаксиса.
        """
        return f"Highlighted {self.language} code: {code}"

    def set_language(self, language):
        """
        И снова установка языка для подсвептки
        Установка языка для подсветки.
        """
        self.language = language
        return f"Language set to {language}"