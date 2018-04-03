from decimal import  Decimal
import locale as lc


def get_future_Value(monthly_investment, yearly_interest, years):
    monthly_interst_rate = yearly_interest/12/100
    months = years * 12
    future_value = Decimal("0.00")
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interst_rate
        future_value += monthly_interest
    future_value = future_value.quantize(Decimal("1.00"))
    return future_value




def main():
    choice = "y"
    while choice.lower()== "y":
        monthly_investment = Decimal(input("Monthly investment: "))
        yearly_interest = Decimal(input("Interest rate: "))
        years = int(input("Years : "))
        futureValue = get_future_Value(monthly_investment, yearly_interest, years)
        print()
        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        line = "{:20}   {:>10}"
        print(line.format("Monthly investment : ", lc.currency(monthly_investment, grouping= True)))
        print(line.format("Interest rate", yearly_interest))
        print(line.format("Years: ", years))
        print(line.format("Future value: ", lc.currency(futureValue, grouping= True)), "\n")

        choice = input("Continue? y/n:   ")
        print()
main()
