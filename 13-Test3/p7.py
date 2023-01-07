class C:
    @staticmethod
    def m1(n):
        return ''.join([c for c in str(n) if int(c) % 2 == 0])
    
    @staticmethod
    def m2(n):
        prev_digit = None
        for c in str(n):
            if prev_digit is not None and prev_digit > int(c):
                return False
            prev_digit = int(c)
        return True
    
    @staticmethod
    def m3(n):
        digits = sorted([c for c in str(n)])
        digits_str = ''.join(digits)
        missing_digits = set('0123456789') - set(digits_str)
        missing_digits_str = ''.join(sorted(list(missing_digits)))
        return missing_digits_str

print(C.m1(4231564))  
print(C.m1(79381))    
print(C.m2(125579))   
print(C.m2(4557879))  
print(C.m3(23557))  # Output: "014689"
print(C.m3(12340))  # Output: "56789"
