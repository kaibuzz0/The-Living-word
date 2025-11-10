
def reduce_to_single_digit(number):
    """Reduce a number to a single digit unless it's a master number (11, 22, 33)."""
    while number > 9 and number not in {11, 22, 33}:
        number = sum(int(digit) for digit in str(number))
    return number
def extract_digits(input_str):
    """Extract all digits from a string."""
    return [int(char) for char in input_str if char.isdigit()]
def numerology_value(char):
    """Calculate numerology value of a character based on position in alphabet."""
    numerology_mapping = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    return numerology_mapping[char.upper()]
def calculate_name_values(name):
    """Calculate values needed for numerology from a name."""
    letter_values = [numerology_value(char) for char in name if char.isalpha()]
    return letter_values, reduce_to_single_digit(sum(letter_values))
def interpret_birth_time(time_of_birth):
    """Interpret birth time and return challenge numbers, outward persona, and hidden spiritual key."""
    digits = extract_digits(time_of_birth)
    if digits:
        challenge_number = reduce_to_single_digit(sum(digits))
        outward_persona = reduce_to_single_digit(digits[0]) if digits else None
        hidden_spiritual_key = reduce_to_single_digit(sum(digits[-2:])) if len(digits) > 1 else None
        return challenge_number, outward_persona, hidden_spiritual_key
    return None, None, None
def calculate_life_path(birthdate):
    digits = [int(char) for char in birthdate if char.isdigit()]
    return reduce_to_single_digit(sum(digits))
def calculate_soul_urge(name):
    vowels = "AEIOU"
    total = sum(numerology_value(char) for char in name if char.upper() in vowels)
    return reduce_to_single_digit(total)
def calculate_personality_number(name):
    vowels = "AEIOU"
    total = sum(numerology_value(char) for char in name if char.isalpha() and char.upper() not in vowels)
    return reduce_to_single_digit(total)
def calculate_birthday_number(birthdate):
    day = int(birthdate.split('/')[1])
    return reduce_to_single_digit(day)
def calculate_maturity_number(life_path, expression):
    return reduce_to_single_digit(life_path + expression)
def calculate_pinnacle_numbers(life_path, birth_day):
    return [reduce_to_single_digit(life_path + birth_day)] * 4
def calculate_personal_year(life_path, current_year):
    return reduce_to_single_digit(life_path + current_year)
def calculate_personal_month(personal_year, current_month):
    return reduce_to_single_digit(personal_year + current_month)
def calculate_personal_day(personal_month, current_day):
    return reduce_to_single_digit(personal_month + current_day)
def calculate_karmic_debt_numbers(expression_number):
    return [reduce_to_single_digit(expression_number + n) for n in [13, 14, 16, 19]]
def calculate_hidden_passion(name):
    return reduce_to_single_digit(sum(numerology_value(char) for char in name if char.lower() in 'aeiou'))
def calculate_subconscious_self(name):
    consonant_values = sum(numerology_value(char) for char in name if char.isalpha() and char.lower() not in 'aeiou')
    return reduce_to_single_digit(consonant_values)
def calculate_balance_number(vowel_values, consonant_values):
    return reduce_to_single_digit(sum(vowel_values) + sum(consonant_values))
def calculate_cornerstone(name):
    return numerology_value(name[0])
def calculate_capstone(name):
    return numerology_value(name[-1])
def calculate_first_vowel(name):
    for char in name:
        if char.lower() in 'aeiou':
            return numerology_value(char)
    return None
def calculate_birthday_secret_keys(day, month, year):
    day_sum = reduce_to_single_digit(day)
    month_sum = reduce_to_single_digit(month)
    year_sum = reduce_to_single_digit(sum([int(digit) for digit in str(year)]))
    return day_sum, month_sum, year_sum
def calculate_all_numerology(full_name, birthdate, time_of_birth, current_year, current_month, current_day):
    """Consolidate all numerology calculations into a single dictionary."""
    life_path_number = reduce_to_single_digit(sum(extract_digits(birthdate)))
    expression_number = calculate_name_values(full_name)[1]
    soul_urge_number = calculate_name_values(''.join(char for char in full_name.upper() if char in 'AEIOU'))[1]
    personality_number = calculate_name_values(''.join(char for char in full_name.upper() if char not in 'AEIOU'))[1]
    birthday_number = reduce_to_single_digit(int(birthdate.split('/')[1]))
    maturity_number = reduce_to_single_digit(life_path_number + expression_number)
    
    challenge_numbers = calculate_challenge_numbers(birthdate)
    pinnacle_numbers = [
        reduce_to_single_digit(sum(map(int, birthdate.split('/')[0:2]))),
        reduce_to_single_digit(sum(map(int, birthdate.split('/')[::2]))),
        reduce_to_single_digit(sum(map(int, birthdate.split('/')[1:]))),
        reduce_to_single_digit(sum(challenge_numbers[::2]))
    ]

    personal_year_number = reduce_to_single_digit(sum(extract_digits(birthdate[:5])) + sum(extract_digits(str(current_year))))
    personal_month_number = reduce_to_single_digit(personal_year_number + current_month)
    personal_day_number = reduce_to_single_digit(personal_month_number + current_day)

    birth_time_interpretation = interpret_birth_time(time_of_birth)
    birthdate_keys = calculate_birthdate_sums(*map(int, birthdate.split('/')))
    name_secret_keys = determine_name_secret_keys(full_name)

    # Calculate new numerology numbers
    karmic_debts = calculate_karmic_debt_numbers(full_name)
    karmic_lessons = calculate_karmic_lessons(full_name)
    hidden_passion = hidden_passion_number(full_name)
    subconscious_self = subconscious_self_number(full_name)
    balance = balance_number(full_name)
    cornerstone_value = cornerstone(full_name.split()[0])
    capstone_value = capstone(full_name.split()[0])
    first_vowel_value = first_vowel(full_name.split()[0])

    return {
        "Life Path Number": life_path_number,
        "Expression Number": expression_number,
        "Soul Urge Number": soul_urge_number,
        "Personality Number": personality_number,
        "Birthday Number": birthday_number,
        "Maturity Number": maturity_number,
        "Challenge Numbers": challenge_numbers,
        "Pinnacle Numbers": pinnacle_numbers,
        "Personal Year Number": personal_year_number,
        "Personal Month Number": personal_month_number,
        "Personal Day Number": personal_day_number,
        "Birth Time Interpretation": birth_time_interpretation,
        "Birthday Secret Keys": birthdate_keys,
        "Name Secret Keys": name_secret_keys,
        "Karmic Debt Numbers": karmic_debts,
        "Karmic Lessons": karmic_lessons,
        "Hidden Passion Number": hidden_passion,
        "Subconscious Self Number": subconscious_self,
        "Balance Number": balance,
        "Cornerstone": cornerstone_value,
        "Capstone": capstone_value,
        "First Vowel": first_vowel_value
    }
