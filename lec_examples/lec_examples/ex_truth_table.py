print("  A       I       Y       C")
for A in True, False:
    for I in True, False:
        for Y in True, False:
            C = (not A) and (I or (not Y))
            print(str(A) + "\t" + str(I) + "\t" + str(Y) + "\t" + str(C))
      
