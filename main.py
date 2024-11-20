def count_vowels(string):

    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    count = sum(1 for char in string if char in vowels)
    return count