# Password class and obj str
class Password:
    _pString: object

    def __init__(self, pString: object):
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
