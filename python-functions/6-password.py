def validate_password(password):
    if len(password) < 8:
        return False
    else:
        upperC =0
        lowerc=0
        digit=0
        for x in password:
            if x.isnumeric():
                digit +=1
            elif x.isalpha():
                if x == x.upper():
                    upperC +=1
                else:
                    lowerc +=1
            elif x.isspace():
                return False
            else:
                return False
    if digit > 0 and lowerc > 0 and upperC > 0:
            return True
    else:
            return False