class VersionControl:
    def __init__(self, repo):
        self.repo = repo

    def commit(self, message):
        """
        Имитация коммита в систему контроля версий.
        """
        return f"Committed to {self.repo} with message: {message}"

    def pull(self):
        """
        Имитация получения изменений из репозитория.
        """
        return f"Pulled latest changes from {self.repo}"

    def push(self):
        """
        Имитация отправки изменений в репозиторий.
        """
        return f"Pushed changes to {self.repo}"