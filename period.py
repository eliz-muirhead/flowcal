class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = (end - start).days
