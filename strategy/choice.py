# --*-- encoding: utf -8 --*--

class choiceBase(object):
    def __int__(self):
        self._map = {}

    def getNextStep(self,dct_data):
        tmp = dct_data['form']
        tmp['a'] = str(int(tmp['a']) + 1)
        return tmp