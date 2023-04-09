# Задача:
В текстовом файле содержится набор строк с информацией о движении денежных
средств между счетами (транзакции). Строки должны быть в одном из двух форматов:
- Дата Счёт Сумма (открытие счета);
- Дата Счёт1 Счёт2 Сумма Примечание (перевод денег со счета1 на счет2).

По данным из файла формируется список счетов с информацией о движении денежных средств
по каждому. При чтении данных из файла некорректные данные или транзакции приводящие к
некорректным действиям игнорируются (перевод с неоткрытого счета, перевод суммы, превышающей количество денег на счете), при этом формируется файл со списком некорректных строк и
пояснениями.

В главном окне отображается список счетов с итоговым количеством денежных средств на каждом. Главное меню должно содержать пункты для следующих действий:
- добавление новых транзакций;
- список транзакций, совершенных в заданную дату;
- список транзакций, примечание в которых содержит заданное слово;
- дополнительно: вывод истории операций по данному счету за выбранный период;
- дополнительно: вывод пар счетов, по которым наибольшее количество взаимных переводов
(первые пять пар).
