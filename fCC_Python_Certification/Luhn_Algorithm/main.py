

def verify_card_number(card_number: str) -> str:
    
    def clean_str(string:str) -> str:
        return string.replace('-','').replace(' ','')

    def double_digit(digit: int) -> int:
        doubled = digit * 2
        if doubled > 9:
            doubled = doubled // 10 + doubled % 10
        return doubled
    
    card_numbers = list(clean_str(card_number))
    check_digit = int(card_numbers[-1])
    sum_digits = check_digit
    try:
        calc_numbers = list(map(int, card_numbers[:-1]))[::-1]
        for i, number in enumerate(calc_numbers):
            if i % 2 == 0:
                sum_digits += double_digit(number)
            else:
                sum_digits += number
        if sum_digits % 10 == 0:
            return 'VALID!'
        else:
            return 'INVALID!'
    except ValueError:
        return 'Card number contains invalid digits!'
    


print(verify_card_number('453914889'))
