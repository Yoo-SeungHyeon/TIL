# 아래에 코드를 작성하시오.
class MovieTheater():

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name
    
mt1 = MovieTheater('메가박스',300)
mt2 = MovieTheater('CGV', 200)

print(mt1)
print(mt2)