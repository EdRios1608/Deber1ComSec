# initial encrypted text
flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"

# A-Z
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# a-z
az = "abcdefghijklmnopqrstuvwxyz"

# string to store result
flag_answer = ""

# iterate through encrypted flag
for x in flag:
    # if the character is in AZ
    if x in AZ:
        # go 13 characters further from the current character
        flag_answer += AZ[(AZ.index(x)+13)%len(AZ)]
        # if the character is in az
    elif x in az:
        # go 13 characters further from the current character
        flag_answer += az[(az.index(x)+13)%len(az)]
    else:
        # else add the character
        flag_answer += x

# print string
print(flag_answer)