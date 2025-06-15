# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
current_month_payment = payment
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 0
digits_to_show = 4

while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        current_month_payment = payment + extra_payment
    else:
        current_month_payment = payment

    principal = principal * (1 + rate / 12)
    if current_month_payment > principal:
        current_month_payment = principal
    principal -= current_month_payment
    total_paid = total_paid + current_month_payment
    print(f"{month} {total_paid:10.2f} {principal:10.2f}")

print(f"Total paid {total_paid:10.2f}")
print(f"Months {month}")
