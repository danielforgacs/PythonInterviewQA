import sys



# 01 ==========================================================================
class Attr:
    # UPDATE HERE:
    pass
    # ^^^

class Klass:
    attr = Attr()

instance = Klass()

try:
    assert isinstance(instance.attr, int)

except Exception as error:
    print('[ERROR] line: {}, type: {}, msg: {}'.format(
        sys.exc_info()[2].tb_lineno, type(error), error))



# 02 ==========================================================================
try:
    assert (1 or 2) == None

except Exception as error:
    print('[ERROR] line: {}, type: {}, msg: {}'.format(
        sys.exc_info()[2].tb_lineno, type(error), error))



# 03 ==========================================================================
try:
    assert 1 and 2 == None

except Exception as error:
    print('[ERROR] line: {}, type: {}, msg: {}'.format(
        sys.exc_info()[2].tb_lineno, type(error), error))


