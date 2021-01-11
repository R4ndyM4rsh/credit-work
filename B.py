from A import A


class B(A):
    def one(self):
        if type(self.number) == int or type(self.number) == float:
            result = self.number * 1
        else:
            result = "error"
        return result

    def two(self):
        if type(self.number) == int or type(self.number) == float:
            result = self.number * 2
        else:
            result = "error"
        return result

    def three(self):
        if type(self.number) == int or type(self.number) == float:
            result = self.number * 3
        else:
            result = "error"
        return result