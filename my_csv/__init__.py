class Csv:
    def __init__(self, filename):
        self.f = open(filename)

    def read(self, delimiter=','):
        line = self.f.readline()
        if not line:
            return None
        raw_row = line.rstrip()
        return raw_row.split(delimiter)

    def __del__(self):
        self.f.close()
