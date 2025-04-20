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

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats
    
    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            print("VIP 좌석 예약이 완료되었습니다.")
        elif self.vip_seats == 0:
            print("예약 가능한 VIP 좌석이 없습니다.")
        else:
            print("잘못된 접근입니다.")
    
    def reserve_seat(self):
        if self.vip_seats > 0:
            self.reserve_vip_seat()
        elif self.vip_seats == 0:
            super().reserve_seat()

mv = VIPMovieTheater('CGV',100,3)

mv.reserve_vip_seat()
mv.reserve_vip_seat()

mv.reserve_seat()
mv.reserve_seat()

mv.reserve_vip_seat()