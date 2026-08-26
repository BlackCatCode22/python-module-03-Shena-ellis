#
# # < ----    ---->
#
# num = 0
# tot = 0.0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         break
#     fval = float(sval)  # This will convert the input to a float
#     print(fval)
#     num = num + 1 # counter pattern
#     tot = tot + fval
#
# print('ALL DONE')
# print(tot, num, tot/num)


# < ---- TRY AND EXCEPT ---- >
# To prevent the program from breaking if somebody enters any string other than 'done' in the input



num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)      # This will convert the input to a float
    except:
        print('INVALID INPUT')
        continue
        # print(fval)
    num = num + 1 # counter pattern
    tot = tot + fval

# print('ALL DONE')
print(tot, num, tot/num)