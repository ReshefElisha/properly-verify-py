class Check(object):
    def __init__(self, propertiestoverify):
        self.properties = propertiestoverify
        self.missing = []
        self.failed = False

    def fail(self, prop):
        self.missing.append(prop)
        self.failed = True
        return self

    def require(self, prop):
        try:
            if prop in self.properties and self.properties[prop] is not None:
                return self
            else:
                return self.fail(prop)
        except TypeError:
            return self.fail(prop)

    def optional(self, prop, fallback=None):
        if prop not in self.properties or self.properties[prop] is None:
            if fallback is not None:
                self.properties[prop] = fallback
            else:
                self.missing.append(prop)
        return self

    def validate(self):
        if self.failed:
            errtxt = 'The property check failed. The following required properties were missing: '
            errtxt += repr(self.missing)[1:-1]
            raise AttributeError(errtxt)
        return self.properties

    def close(self):
        return self.properties
