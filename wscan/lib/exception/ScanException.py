

# ===================== Top Level Exception ======================
class ScanException(Exception):
    pass


# ==================== Network Exception =========================
class NetworkException(ScanException):
    pass


class TimeOutError(NetworkException):
    pass


class UnknownNetworkError(NetworkException):
    pass


class SessionError(NetworkException):
    pass


# ===================== Connect Exception ========================
class ConnectError(ScanException):
    pass


class ResetError(ConnectError):
    pass


# ===================== Many kinds of Error ========================
class FetchResError(ScanException):
    pass


class ParameterTypeError(ScanException):
    pass
