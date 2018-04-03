from decimal import Decimal
def process_Amount(principle_Amount, interest_Amount, number_Of_times, years):
    future_Amount = principle_Amount*(1+ interest_Amount/number_Of_times)**(years* number_Of_times)
    # future_Amount = future_Amount.quantize(Decimal("1.00"))
    return future_Amount


def get_input():
   principle_Amount = float(input("Enter principle amount $ : "))
   interest_Amount = float(input("Enter interest amount $ : "))
   interest_Amount = interest_Amount/100
   number_Of_times = int(input("Enter number of times: "))
   years = int(input("Number of years : "))
   calc_amount =process_Amount(principle_Amount, interest_Amount, number_Of_times, years)
   #print(calc_amount)
   return calc_amount


def main():
    asked_input = get_input()

    print("Future amount will be $", format(asked_input,".2f"))
main()