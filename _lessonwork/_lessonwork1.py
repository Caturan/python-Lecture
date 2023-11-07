# Convert a float number to binary. 

class BinaryRepresentation():
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("Number must be float")
        if isinstance(number, bool):
            raise TypeError("Number must not be boolean type")
        self.num = num 
        self.result = self.__str__()

    def __str__(self):
        integer_part = int(self.number)
        decimal_part = self.number - integer_part
        self.result = binary_rep_res(integer_part, decimal_part)
        return self.result
    
def binary_rep_res(integer_part, decimal_part):
    return f"{calculate_binary_rep_for_int_part(integer_part)}.{calculate_binary_conversion_for_dec_part(decimal_part)}"

def calculate_binary_rep_for_int_part(int_part):
    result = ""
    if int_part == 0:
        result += str(int_part)
        return result 
    else: 
        while int_part > 0:
            remainder = int_part % 2 
            result += str(remainder)
            int_part = int_part // 2
        return result[::-1]

def calculate_binary_conversion_for_dec_part(decimal_part):
    result = ""
    while decimal_part != 0:
        decimal_part = float(decimal_part) * 2
        if decimal_part >= 1:
            result += '1'
            decimal_part -= 1
        else: 
            result += '0'
        if len(result) >= 10:
            break
    return result



def main():
    main()

if __name__ == "__main__":
    x = binary_rep_res(375, 814)
    print(x)
    y = list(x)
    # print(y)
    # print(y.index('.'))
    z = y.index('.')
    # print(z)
    # print(y[0])
    # print(y[0:z])
    k = y[0]
    # print(type(k))

    sign = " "
   
    i = (y[0:z] ,": is integer part")
    m = (y[z+1:-1], ": is float part")
    if k == '1':
       sign = "Positive sign"
    else:
       sign = "Negative sign"

    # print(sign)

    print(i, ": is integer part of binary conversion ", 
    m, ": is mantassi part of conversion ",
    sign, ": is sign of the binary number")

    #print(dir(list))
