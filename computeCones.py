import math

print("This program calculates the surface area and volume of a cone.")
r = float(input("Enter the radius of the cone (in feet): "))
h = float(input("Enter the height of the cone (in feet): "))
print("The numbers you entered have been rounded to 2 decimal digits.\nRadius = "
      +str(round(r,2))+ " feet & Height = " +str(round(h,2))+ " feet.")

def cone_surface_area(r, h):
    sa1 = math.pi * (pow(r,2)) 
    sa2 = (pow(r,2) + pow(h,2) )
    sa3 = (math.pi * r) * math.sqrt(sa2)
    final = sa1 + sa3
    print("The surface area of the cone is " +str(round(final,2))+ " feet.")

def cone_volume(r,h):
    v1 = ( math.pi * (pow(r,2)) * h)
    final = v1 / 3
    print("The volume of the cone is " +str(round(final,2))+ " feet.")

cone_surface_area(r,h)
cone_volume(r,h)

