print('please note, this code is case sensitive and all inputs should be in small caps')
agn='yes'
while agn=='yes':
    choice=input('which shape would you like to calculate the area for(trapezium,square,cylinder or triangle):')
    if choice=='trapezium':
        print('alright lets do this for all the trapeziums in the world')
        a=eval(input('please enter the length of the top of the trapezium:'))
        b=eval(input('please enter the length of the bottom of the trapezium:'))
        c=eval(input('please enter the height of the trapezium:'))
        d=a+b
        e=c*d
        f=e/2
        print('the area of your trapezium is:',f)
        print('thats all for the trapezium')
        agn=input('would you like to calculate another area?(yes/no):')
    elif choice=='square':
        print('the worlds square are about to be fit into round holes')
        g=eval(input('enter the length of the squares side:'))
        h=g**2
        print('the area of your square is:',h)
        print('thats all for the square')
        agn=input('would you like to calculate another area?(yes/no):')
    elif choice=='cylinder':
        print('we are about to give all those cylinders a run for their money')
        from math import pi
        i=eval(input('enter the height of your prefered cylinder:'))
        j=eval(input('enter the radius of the cylinder:'))
        k=j**2
        l=pi*k*i
        print('the area of your chosen cylinder is:',l)
        print('thats all for the cylinder')
        agn=input('would you like to calculate another area?(yes/no):')
    elif choice=='triangle':
        print('now we are going into a world of triangles, hope you are ready for it')
        m=eval(input('enter the height of our preferred triangle:'))
        n=eval(input('enter the length of the base of the triangle:'))
        o=(m*n)/2
        print('the area of your triangle is:',o)
        print('thats all for the triangle')
        agn=input('would you like to calculate another area?(yes/no):')
print('thank you for your time and goodbye ;)')









