"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""

if __name__ == '__main__':
    pass


# Задание 1
# prompt user for console input
password = input('Enter password to test how good it is: ')

# Basic check of password complexity
checks_passed_count = 0
if len(password) < 8:
    print("Your password is very weak. It is shorter than 8 symbols.")
    is_short = True
else:
    checks_passed_count += 1


# I know that isdigit is slower than regex
# (and maybe isalpha too),
# but here we value readability over performance
if not any(char.isdigit() for char in password):
    print("Your password should contain digits")
    has_no_digits = True
else:
    checks_passed_count += 1

if not any(char.isalpha() for char in password):
    print("Your password should contain alphabetical symbols")
    has_no_alpha = True
else:
    checks_passed_count += 1

print("Checks passed: %s" % checks_passed_count)
# function wrapper for dictionary with verdicts
# depending on number of checks passed


def password_weakness(n):
    verdict = {
        0: "Your password is very very weak",
        1: "Your password is very weak",
        2: "Your password is weak",
        3: "Your password is decent",
    }
    return verdict.get(n, "Wait, what?! How'd you get there?")


print(password_weakness(checks_passed_count))

# For regex solution, use smth like this:

# _digits = re.compile('\d')
# def contains_digits(d):
#     return bool(_digits.search(d))
