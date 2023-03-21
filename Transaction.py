import re


class Transaction:
    counts = []
    operations = []

    def __init__(self):
        transaction_file = open("/Transaction.py")
        lines = transaction_file.readlines()
        for line in lines:
            if re.fullmatch("\d.\d.\d \d+ \d+"):
                self.counts.append(line)
            elif re.fullmatch("\d.\d.\d \d+ \d+ \d+ .*"):
                self.operations.append(line)
        transaction_file.close()


