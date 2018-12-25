

class Utility(object):
    @staticmethod
    def int_try_parse(value):
        try:
            return int(value)
        except ValueError:
            return 0
