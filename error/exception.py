class CustomError(Exception):
    def __init__(self, code, message):
        super().__init__(code, message)
        self.code = code
        self.message = message


ErrorApplicationNotInit = CustomError(
    100001,
    "application not init",
)

ErrorConfigEnvNotFind = CustomError(
    100002,
    "config env not find",
)

ErrorLaunchModuleNotAllow = CustomError(
    100003,
    "launch module not allow",
)

ErrorLaunchClassNotFind = CustomError(
    100004,
    "launch class not find",
)

ErrorLaunchClassNotConform = CustomError(
    100005,
    "launch class not conform",
)

ErrorLaunchFunctionNotFind = CustomError(
    100006,
    "launch function not find",
)
