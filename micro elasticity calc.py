q_start = float(input("start q: "))
p_start = float(input("start p: "))

q_end = float(input("end q: "))
p_end = float(input(     "end p: "))


def price (a,b,y,z):
    avg_q = ((b-a))/((b+a)/2)
    
    avg_p = ((z-y))/((z+y)/2)
    final = avg_q/avg_p
    print("change in q: ", avg_q)
    print("change in p: ", avg_p)
    if abs(final) > 1:
        print("it's elastic")
    elif abs(final) == 1:
        print("it is unit elastic")
    else:
        print("inelastic")
    print(abs(final))

price(q_start,q_end,p_start,p_end)