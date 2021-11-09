# Password class and object string
class Password:
    def __init__(self, pString = ""):
        self._pString = pString

    @property
    def pString(self):
        return self._pString

    @pString.setter
    def pString(self, pString: object):
        self._pString = pString

    @pString.deleter
    def pString(self):
        del self._pString

    @classmethod
    def MakePassword( cls, control_state ) -> str:
        pString = "PASSWORD PLACEHOLDER"
        return cls(pString)
