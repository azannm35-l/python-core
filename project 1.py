class ticketbooker:
    def __init__(self,total_seat):
        self.total_seat=total_seat
        self.booked_seat=0
    def book_seat(self):
        if self.booked_seat < self.total_seat:
         self.booked_seat+=1 
         print("your seat is booked")
        else:
           print("insuficient seat avalible")
    def show_avalible_seats(self):
       avalible= self.total_seat -self.booked_seat
       print("avalible seats are ",avalible)

booking=ticketbooker(90)
booking.book_seat()
booking.book_seat()
booking.show_avalible_seats()
booking.book_seat()
booking.show_avalible_seats()



#added comment just to check the git 