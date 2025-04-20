# 아래에 코드를 작성하시오.
class MovieTheater():

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name
    
    def reserve_seat(self):
        if self.total_seats > self.reserved_seats:
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")
        elif self.total_seats == self.reserved_seats:
            print("좌성 예약을 실패하였습니다.")
        else:
            print("잘못된 접근입니다.")
    
    def current_status(self):
        print(f'총 좌석 수: {self.total_seats}')
        print(f'예약된 좌석 수: {self.reserved_seats}')
    
mv = MovieTheater('메가박스', 100)

mv.reserve_seat()
mv.reserve_seat()
mv.reserve_seat()

mv.current_status()