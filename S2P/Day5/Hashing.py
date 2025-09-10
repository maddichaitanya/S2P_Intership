# def freq(s):
#     freq = [0] * 256  # ASCII size   
#     for ch in s:
#         freq[ord(ch)] += 1
#         if freq[ord(ch)] == 1:
#             print(ch, ":", s.count(ch))

# s = "programming23ADF"
# freq(s)





def sol(s):
    Has = [0] * 256  # ASCII size   
    for ch in s:
        Has[ord(ch)] += 1   

    for ch in s:
        if Has[ord(ch)] != 0:  
            print(ch, ":", Has[ord(ch)])
             

s = "programming23ADF/@"
sol(s)







# for i in range(256):
#     print(i, ":", repr(chr(i)))




# we are creating an array that can store counts for all ASCII characters:

# 0–31 → Control characters (non-printable, like newline, tab)

# 32–47 → Symbols (space ! " # $ % & ' ( ) * + , - . /)

# 48–57 → Digits (0–9)

# 58–64 → Symbols (: ; < = > ? @)

# 65–90 → Uppercase letters (A–Z)

# 91–96 → Symbols (`[ \ ] ^ _ ``)

# 97–122 → Lowercase letters (a–z)

# 123–126 → Symbols ({ | } ~)

# 127–255 → Extended ASCII (depends on system/encoding) (varies by encoding, includes symbols like é, ñ, ü, etc.)