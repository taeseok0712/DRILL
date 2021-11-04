class Star:
    type = 'Star'
    x = 100

    @staticmethod
    def change():
        x = 200
        print('x is ', x)

print('x IS ', Star.x) # OK
Star.change() # OK
print('x IS ', Star.x)
star = Star() # OK
print('x IS ', star.x) # OK
star.change() # Error

# 생성자 없는 클래스는 싱글톤이라 생각하면 편하다?
