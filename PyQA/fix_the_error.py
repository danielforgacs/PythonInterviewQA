# Update here:
class Attr:
    pass

# to make this work:
class K:
    attr = Attr()

k = K()

assert isinstance(k.attr, int)
