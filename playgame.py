import math
# hediin dotor sanasaniig asuuna
# garah songoltiig hiih hurtel dawtaj ajillana
#  1.zuw hariult
#  2.ih too sanasan
#  3.baga too sanasan
#  4.garah
#  buruu songolt hiivel dahin asuuna
ans = '2'
while ans not in '4':
    n = int(input("Ta hediin dotor too sanasan be? : "))
    
    print("Bi tanii sanasan toog hamgiin ihdee {} oroldlogo hiigeed olj chadna".format(int(math.log(n,2)) + 1))
    low_n,high_n = 1,n
    i = 1
    print("Oroldlogo {} : Tanii sanasan too {} mun uu?".format(i ,((low_n+high_n)//2)))
    
    ans = input("1.Zuw hariult\n2.ih too sanasan\n3. Baga too sanasan \n4.Garah\n")

    while ans not in '14':
        if ans not in '1234':
            ans = input("1.Zuw hariult\n2.ih too sanasan\n3. Baga too sanasan \n4.Garah\n")
            continue
        i += 1
        if ans == '2':
            low_n = (low_n+high_n)//2
            
        elif ans == '3':
            high_n = (low_n+high_n)//2
             
        
        print("Oroldlogo {} : Tanii sanasan too {} mun uu?".format(i,((low_n + high_n) // 2 )))
        ans = input("1.Zuw hariult\n2.ih too sanasan\n3. Baga too sanasan \n4.Garah\n")
        if ans == '1':
            ans = input("Ta togloomoos garah bol (4) towchiig darna uu\nUrgeljluuleh bol yamarch hamaagui towch darna uu\n")
    
            
    


    
    
    
    
