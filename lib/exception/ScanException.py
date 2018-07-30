# import aiohttp


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


# ===================== Connect Exception ========================
class ConnectError(ScanException):
    pass


class DNSError(ConnectError):
    pass


class ResetError(ConnectError):
    pass


# ===================== All kinds of Error ========================
class FetchResError(ScanException):
    pass


class FormatError(ScanException):
    pass
