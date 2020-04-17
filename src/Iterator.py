class Iterator(object):
    def __init__(self, element):
        self.element = element
        self.position = 0

    def set_first(self):
        self.position = 0

    def next(self):
        self.position += 1

    def is_done(self):
        if self.position < len(self.element):
            return True
        else:
            return False

    def get_current_item(self):
        return self.element[self.position]
