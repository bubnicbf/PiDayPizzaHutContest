for a in ['1','3','7','9']:
    for b in ['2','4','6','8']:
        for c in ['1','3','7','9']:
            for d in ['2','4','6','8']:
                for f in ['2','4','6','8']:
                    for g in ['1','3','7','9']:
                        for h in ['2','4','6','8']:
                            for i in ['1','3','7','9']:
                                if a!=c and a!=g and a!=i and c!=g and c!=i and g!=i and b!=d and b!=f and b!=h and d!=f and d!=h and f!=h:
                                	number2 = int(a+b)
                                	number3 = int(a+b+c)
                                	number4 = int(a+b+c+d)
                                	number6 = int(a+b+c+d+'5'+f)
                                	number7 = int(a+b+c+d+'5'+f+g)
                                	number8 = int(a+b+c+d+'5'+f+g+h)
                                	number9 = int(a+b+c+d+'5'+f+g+h+i)
                                	if number2%2==0 and number3%3==0 and number4%4==0 and number6%6==0 and number7%7==0 and number8%8==0 and number9%9==0:
                                		print number9
                                		#381654729
