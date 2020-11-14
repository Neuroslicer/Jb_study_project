import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--payment')
parser.add_argument('--interest')
args = parser.parse_args()
if args.type == "annuity" and args.principal is not None and args.payment is not None and args.interest is not None:
    if float(args.principal) > 0 and float(args.payment) > 0 and float(args.interest) > 0:
        loan_principal = int(args.principal)
        monthly_payment = int(args.payment)
        loan_interest = float(args.interest)
        nominal_rate = loan_interest / (12 * 100)
        months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_rate * loan_principal),
                                    1 + nominal_rate))
        overpayment = months * monthly_payment - loan_principal
        if months % 12 != 0 and months > 12:
            years = months // 12
            months = months % 12
            print(f'It will take {years} years and {months} months to repay this loan!')
        elif months % 12 == 0:
            if months > 12:
                years = months // 12
                print(f'It will take {years} years to repay this loan!')
            else:
                print('It will take 1 year to repay this loan!')
        else:
            print(f'It will take {months} months to repay this loan!')
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')
elif args.type == "annuity" and args.principal is not None and args.periods is not None and args.interest is not None:
    if float(args.principal) > 0 and float(args.periods) > 0 and float(args.interest) > 0:
        loan_principal = int(args.principal)
        periods_number = int(args.periods)
        loan_interest = float(args.interest)
        nominal_rate = loan_interest / (12 * 100)
        annuity_payment = loan_principal * nominal_rate * pow(1 + nominal_rate, periods_number) \
                       / (pow(1 + nominal_rate, periods_number) - 1)
        overpayment = math.ceil(annuity_payment) * periods_number - loan_principal
        print(f'Your monthly payment = {math.ceil(annuity_payment)}!')
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')

elif args.type == "annuity" and args.payment is not None and args.periods is not None and args.interest is not None:
    if float(args.payment) > 0 and float(args.periods) > 0 and float(args.interest) > 0:
        annuity_payment = float(args.payment)
        periods_number = int(args.periods)
        loan_interest = float(args.interest)
        nominal_rate = loan_interest / (12 * 100)
        loan_principal = annuity_payment / (nominal_rate * pow(1 + nominal_rate, periods_number)
                                        / (pow(1 + nominal_rate, periods_number) - 1))
        overpayment = math.ceil(annuity_payment * periods_number - loan_principal)
        print(f'Your loan principal = {round(loan_principal)}!')
        print(f'Overpayment = {overpayment}')
    else:
        print('Incorrect parameters')

elif args.type == "diff" and args.principal is not None and args.periods is not None and args.interest is not None:
    if float(args.principal) > 0 and float(args.periods) > 0 and float(args.interest) > 0:
        loan_principal = int(args.principal)
        periods_number = int(args.periods)
        loan_interest = float(args.interest)
        nominal_rate = loan_interest / (12 * 100)
        current_month = 1
        sum_of_payments = 0
        while current_month <= periods_number:
            dif_payment = loan_principal / periods_number + nominal_rate * \
                          (loan_principal - (loan_principal * (current_month - 1) / periods_number))
            print(f'Month {current_month}: payment is {math.ceil(dif_payment)}')
            current_month += 1
            sum_of_payments += math.ceil(dif_payment)
        print(f'Overpayment = {round(sum_of_payments - loan_principal)}')

else:
    print('Incorrect parameters')
