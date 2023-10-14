'''
class StarCookie:
    def __init__(self):
        print("The cookie is ready...")
        
star_cookie1 = StarCookie()
star_cookie1.weight = 15
star_cookie1.color = "Brown"
star_cookie1.shape = "Oval"

star_cookie2 = StarCookie()
star_cookie2.weight = 19
star_cookie2.color = "Black"
star_cookie2.shape = "Circular"

print(star_cookie1.weight)
print(star_cookie1.color)
print(star_cookie1.shape)

print("#################################")
print(star_cookie2.weight)
print(star_cookie2.color)
print(star_cookie2.shape)'''

########################################################
'''HOW CAN WE SET THE ATTRIBUTE INSIDE THE INITIALIZER'''
########################################################
'''
By using this method we can initialize the attributes 
    def __init__(self,color):
        self.color = color
'''
class StarCookie:
    def __init__(self,color):
        self.color = color
        
star_cookie1 = StarCookie("Brown")
star_cookie1.weight = 15
#star_cookie1.color = "Brown"
star_cookie1.shape = "Oval"
'''
star_cookie2 = StarCookie()
star_cookie2.weight = 19
star_cookie2.color = "Black"
star_cookie2.shape = "Circular"
'''
print(star_cookie1.weight)
print(star_cookie1.color)
print(star_cookie1.shape)
'''
print("#################################")
print(star_cookie2.weight)
print(star_cookie2.color)
print(star_cookie2.shape)'''

print("WE CAN ADD AS MANY AS ATTRIBUTE WE NEEDED ")

class Mercenary:
    def __init__(self,armorcolor,weight,weapon):
        self.armorcolor = armorcolor
        self.weight = weight
        self.weapon = weapon
mercenary1 = Mercenary("Red",30,"Sword")
print(mercenary1.armorcolor)
print(mercenary1.weapon)
print(mercenary1.weight)

print(mercenary1.__dict__)