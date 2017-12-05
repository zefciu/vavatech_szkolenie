class DefaultDict(dict):
    def __init__(self, *args, default=None, **kwargs):
        super(DefaultDict, self).__init__(*args, **kwargs)
        self.default = default

    def __getitem__(self, key):
        try:
            return super(DefaultDict, self).__getitem__(key)
        except KeyError:
            return self.default
