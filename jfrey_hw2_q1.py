def divisible_truefalse():
    numerator = float(raw_input("Input numerator: "))
    denominator = float(raw_input("Input denominator: "))

    if (float(numerator) / float(denominator)) == int(float(numerator) / float(denominator)):
        return True
    else:
        return False


