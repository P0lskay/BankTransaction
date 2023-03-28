import re
import WorkFunctions


class Transaction:
    counts = []
    operations = []
    transaction_file_name = "BankOperations.txt"

    def __init__(self):
        transaction_file = open(self.transaction_file_name)
        lines = transaction_file.readlines()
        for line in lines:
            if re.fullmatch(r'\d+.\d+.\d+ \d+ \d+ \d+.*', line.rstrip('\n')):
                self.operations.append(line)
            elif re.fullmatch(r'\d+.\d+.\d+ \d+ \d+.*', line.rstrip('\n')):
                self.counts.append(line)
        transaction_file.close()

    def add_count(self, date, count, summa):
        transaction_file = open(self.transaction_file_name, 'a')
        new_count = date + " " + count + " " + summa + "\n"
        transaction_file.write(new_count)
        self.counts.append(new_count)
        transaction_file.close()

    def add_operation(self, date, count_out, count_in, summa, comment):
        transaction_file = open(self.transaction_file_name, 'a')
        new_operation = date + " " + count_out + " " + count_in + " " + summa + " " + comment + "\n"
        transaction_file.write(new_operation)
        self.operations.append(new_operation)
        transaction_file.close()

    def get_transaction_per_date(self, date):
        return list(filter(lambda x: re.fullmatch(date + '.*\n', x), self.counts + self.operations))

    def get_transaction_with_word(self, word):
        return list(filter(lambda x: re.fullmatch(r'.*' + word + '.*\n', x), self.operations))

    def get_history_for_count(self, count, start_date, end_date):
        result = []
        # Сначала получаем все операции по счету за все время, затем оставляем только с подходящей датой
        result += list(filter(lambda x: re.fullmatch(r'\d+.\d+.\d+ ' + count + ' \d+\n', x), self.counts))
        result += list(filter(lambda x: re.fullmatch(r'\d+.\d+.\d+ ' + count + ' \d+ \d+ .*\n', x), self.operations))
        result += list(filter(lambda x: re.fullmatch(r'\d+.\d+.\d+ \d+ ' + count + ' \d+ .*\n', x), self.operations))
        result = list(filter(lambda x: WorkFunctions.compare_date(x.split()[0], start_date) and
                                       WorkFunctions.compare_date(end_date, x.split()[0]), result))
        return result

    def get_balance_for_all(self):
        result = {}
        for count in self.counts:
            num_count = count.split()[1]
            sum_count = int(count.split()[2])
            for operation in self.operations:
                if operation.split()[1] == num_count:
                    sum_count -= int(operation.split()[3])
                if operation.split()[2] == num_count:
                    sum_count += int(operation.split()[3])
            result[num_count] = sum_count

        return result
