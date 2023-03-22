import re
import WorkFunctions

class Transaction:
    counts = []
    operations = []
    transaction_file_name = "/Transaction.py"

    def __init__(self):
        transaction_file = open(self.transaction_file_name)
        lines = transaction_file.readlines()
        for line in lines:
            if re.fullmatch(r'\d.\d.\d \d+ \d+'):
                self.counts.append(line)
            elif re.fullmatch(r'\d.\d.\d \d+ \d+ \d+ .*'):
                self.operations.append(line)
        transaction_file.close()

    def add_count(self, date, count, summa):
        transaction_file = open(self.transaction_file_name, 'a')
        new_count = date + " " + count + " " + summa
        transaction_file.write(new_count)
        self.counts.append(new_count)
        transaction_file.close()

    def add_operation(self, date, count_out, count_in, summa, comment):
        transaction_file = open(self.transaction_file_name, 'a')
        new_operation = date + " " + count_out + " " + count_in + " " + summa + " " + comment
        transaction_file.write(new_operation)
        self.operations.append(new_operation)
        transaction_file.close()

    def get_transaction_per_date(self, date):
        return list(filter(lambda x: x.fullmatch(date + '.*'), self.counts + self.operations))

    def get_transaction_with_word(self, word):
        return list(filter(lambda x: x.fullmatch(r'.*' + word + '.*'), self.operations))

    def get_history_for_count(self, count, start_date, end_date):
        result = []
        # Сначала получаем все операции по счету за все время, затем оставляем только с подходящей датой
        result += list(filter(lambda x: x.fullmatch(r'\d.\d.\d ' + count + ' \d+'), self.counts))
        result += list(filter(lambda x: x.fullmatch(r'\d.\d.\d ' + count + ' \d+ \d+ .*'), self.operations))
        result += list(filter(lambda x: x.fullmatch(r'\d.\d.\d \d+ ' + count + ' \d+ .*'), self.operations))
        result = list(filter(lambda x:  WorkFunctions.compare_date(x.split()[0], start_date) and
                             WorkFunctions.compare_date(end_date, x.split()[0]), result))
        return result
