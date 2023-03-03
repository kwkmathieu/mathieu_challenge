class Credit_cards:
    credit_card_number = ''

    # It must start with a 4, 5 or 6.
    def validate_first_digit(self):
        return self.credit_card_number.startswith('4') or self.credit_card_number.startswith('5') or self.credit_card_number.startswith('6')
    
    # It must contain exactly 16 digits.
    def validate_len(self):
        card_number = self.credit_card_number.replace('-','') 
        return len(card_number) == 16
    
    # It must only consist of digits (0-9)
    def validate_all_digits(self):
        card_number = self.credit_card_number.replace('-','') 
        return card_number.isdigit() # It must NOT use any other separator like ' ' , '_', etc.
    
    # It may have digits in groups of 4, separated by one hyphen "-".
    def validate_grouping_size(self):
        rc = True
        card_number_groups = self.credit_card_number.split('-')
        if len(card_number_groups) > 1:
            if len(card_number_groups) != 4:
                rc = False
            for group in card_number_groups:
                if len(group) != 4:
                    rc = False
        return rc

    # It must NOT have 4 or more consecutive repeated digits.
    def validate_digits_seq(self):
        card_number = self.credit_card_number.replace('-','') 
        repeated_digit_counter = 0
        previous_digit = ''

        for digit in card_number:
            if digit == previous_digit:
                repeated_digit_counter+=1
                if repeated_digit_counter == 3:
                    return False
            else:
                repeated_digit_counter = 0
            previous_digit = digit
        
        return True

    def validate(self, card_number):
        #self.credit_card_number = input('Please type in your credit card number: ')
        self.credit_card_number = card_number
        first_digit_valid = self.validate_first_digit() 
        len_valid = self.validate_len()
        all_digits_valid = self.validate_all_digits()
        digits_seq_valid = self.validate_digits_seq()
        grouping_size_valid = self.validate_grouping_size()

        if not(first_digit_valid):
            print("Invalid - Must start with a 4, 5 or 6")
        elif not(all_digits_valid):
            print("Invalid - Must only consist of digits (0-9)")
        elif not(grouping_size_valid):
            print("Invalid - Must have digits in groups of 4, separated by one hyphen \"-\"")
        elif not(len_valid):
            print("Invalid - Must contain exactly 16 digits")
        elif not(digits_seq_valid):
            print("Invalid - Must NOT have 4 or more consecutive repeated digits.")
        else:
            print("Valid")

    def start(self):
        credit_card_list = []
        n = input("How many credit cards would you like to validate?")
        if not(n.isdigit()):
            print("Invalid input - The first line must be a digit")
            return
        else:
            n = int(n)
        if n <0 or n >= 100:
            print("Invalid input - The first line must be a digit between 1 and 99")
            return

        for i in range(n):
            credit_card = input('')
            credit_card_list.append(credit_card)
        
        for credit_card in credit_card_list:
            self.validate(credit_card)


card = Credit_cards()
card.start()
