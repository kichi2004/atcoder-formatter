class FormattingFailedError(Exception):
    def __init__(self, status: int, error: str):
        self.status = status
        self.error = error

    status: int
    error: str
