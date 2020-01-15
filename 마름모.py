for z in range(1,12,2):
    print(' ' * (10 - z // 2) + '*' * (z))
    if 11 == z:
         for z in range(9, 0, -2):
             print(' ' * (10 - z // 2) + '*' * (z))
