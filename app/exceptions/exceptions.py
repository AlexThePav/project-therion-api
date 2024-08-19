class TherionException(Exception):
    def __init__(
            self,
            message: str = "Service is unavailable",
            name: str = "Therion"
    ):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class ServiceError(TherionException):
    """
    failures in external services or APIs,
    like a database or a third-party service
    """
    pass
