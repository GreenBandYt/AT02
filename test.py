
import pytest
from main import count_vowels

def test_only_vowels():
    """
    Проверяем, что функция правильно считает гласные
    в строке, содержащей только гласные.
    """
    assert count_vowels("aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ") == 30

def test_no_vowels():
    """
    Проверяем, что функция возвращает 0 для строки,
    не содержащей гласных.
    """
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_case():
    """
    Проверяем, что функция правильно считает гласные
    в строке с прописными и строчными буквами.
    """
    assert count_vowels("Hello, World!") == 3

def test_empty_string():
    """
    Проверяем, что функция возвращает 0 для пустой строки.
    """
    assert count_vowels("") == 0

def test_numeric_and_special_characters():
    """
    Проверяем, что функция игнорирует числа и специальные символы.
    """
    assert count_vowels("1234567890!@#$%^&*()") == 0

# Весёлые тесты!

def test_russian_tongue_twister():
    """
    Проверяем, как функция справляется с известной скороговоркой.
    """
    tongue_twister = "Карл у Клары украл кораллы, а Клара у Карла украла кларнет."
    assert count_vowels(tongue_twister) == 20  # Считаем гласные!

def test_mixed_language_fun():
    """
    Смешанный текст из русского и английского с числами.
    """
    mixed_text = "Привет, World! У меня 3 кота и 2 собаки. A you?"
    assert count_vowels(mixed_text) == 15  # Гласные на обоих языках.

def test_long_vowel_repeat():
    """
    Проверяем строку, где только повторяются гласные.
    """
    repeat_vowels = "ааааааееееооооооууууу"
    assert count_vowels(repeat_vowels) == len(repeat_vowels)  # Все буквы - гласные.

def test_dinosaur_joke():
    """
    Шутка про динозавров.
    """
    dinosaur_text = "Что говорит динозавр? Raaaawwrrrr!"
    assert count_vowels(dinosaur_text) == 11  # Гласные из "Raaaawwrrrr".

def test_nonsense_string():
    """
    Проверяем, что функция справляется с бессмысленной строкой.
    """
    nonsense = "Шпгртнмп! Вртгрштз."
    assert count_vowels(nonsense) == 0  # Гласных нет, результат 0.
