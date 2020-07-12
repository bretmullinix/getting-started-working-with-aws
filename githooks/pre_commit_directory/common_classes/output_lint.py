#!/usr/bin/python3
class OutputLint:
    def __init__(self, results, errors):
        self.results = results
        self.errors = errors

    def __str__(self):
        return "Results = \n\t" + str(self.results) + "\nErrors = \n\t" + str(self.errors)
