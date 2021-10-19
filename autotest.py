{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Функция, которая обращает все строки в числа и подставляет значение по умолчанию, если встречает пропуск.  \n",
    "def digitize_values(collection, default=0):  \n",
    "    no_missed = [value if value else default for value in collection]   \n",
    "    return [float(value) for value in no_missed]  \n",
    "  \n",
    "# Мы передаём на вход произвольные параметры и смотрим, что функция корректно работает с ними   \n",
    "# Проверим, что функция корректно обращает список строк в список чисел  \n",
    "def test_digitize_convert_to_float():  \n",
    "    assert digitize_values([\"10\", \"50\"])  == [10, 50]  \n",
    "    assert digitize_values([\"70.2\", \"33.4\"]) == [70.2, 33.4]  \n",
    "      \n",
    "# Хорошей практикой считается покрывать разные аспекты функции в разных тестах  \n",
    "# Здесь мы проверим, что функция закрывает пропуски   \n",
    "def test_digitize_restore_missed():  \n",
    "    assert digitize_values([\"\"], 10) == [10]  \n",
    "    assert digitize_values([\"20\", None], 50) == [20, 50]  \n",
    "      \n",
    "# Ещё стоит проверять, что наша функция корректно работает на граничных значениях  \n",
    "# Например, на пустых данных  \n",
    "def test_digitize_empty():  \n",
    "    assert digitize_values([]) == []  "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
