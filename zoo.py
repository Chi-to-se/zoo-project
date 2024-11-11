class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: # bug fix
            return 50
        elif 13 <= age <= 20: # bug fix
            return 100
        elif 21 <= age <= 60: # bug fix
            return 150
        elif age >= 60:
            return 100
        else: # <0 bug fix
            return 'Invalid'