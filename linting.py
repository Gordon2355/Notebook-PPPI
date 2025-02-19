class Linter:
    def __init__(self, language):
        self.language = language

    def lint(self, code):
        """
        Имитация линтинга кода.
        """
        return f"Linted {self.language} code: {code}"

    def set_language(self, language):
        """
        Установка языка для линтинга.
        """
        self.language = language
        return f"Linting language set to {language}"