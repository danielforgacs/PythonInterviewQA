# 01 ==========================================================================
class Attr:
# UPDATE HERE:
    pass
# ^^^

class K:
    attr = Attr()

k = K()

try:
    assert isinstance(k.attr, int)
except AssertionError as err:
    print(err)
    pass



# 02 ==========================================================================
try:
    assert 1 or 2 == None
except Exception as error:
    print(error)
    pass



# 03 ==========================================================================
try:
    assert 1 and 2 == None
except Exception as error:
    print(error)
    pass


