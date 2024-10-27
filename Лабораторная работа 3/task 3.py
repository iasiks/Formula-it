# TODO  Напишите функцию count_letters
def count_letters(text):
    count_letters_dict = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in count_letters_dict:
                count_letters_dict[letter] = 1
            elif letter in count_letters_dict:
                count_letters_dict[letter] += 1
    return count_letters_dict
# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):
    calc_frequency_dict = {}
    for letter, count in letters_dict.items():
        calc_frequency_dict[letter] = count / sum(letters_dict.values())
    return calc_frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_in_poem = count_letters(main_str)
frequency_letters = calculate_frequency(letters_in_poem)
for letter_poem, frequency_poem in frequency_letters.items():
    print(f'{letter_poem}: {frequency_poem:.2f}')
