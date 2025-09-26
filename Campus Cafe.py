Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# -------- Functions -------- #

def format_currency(x: float) -> str:
    """Return a string formatted as currency with 2 decimals, like $2.25"""
    return f"${x:.2f}"

def line_total(unit_price: float, qty: int) -> float:
    """Return total price for one item (unit price * quantity)."""
    return unit_price * qty

def compute_totals(subtotal: float, tax_rate: float, tip_percent: float) -> tuple[float, float, float]:
    """Return tax, tip, and total based on subtotal."""
    tax = subtotal * tax_rate
    tip = subtotal * (tip_percent / 100)
    total = subtotal + tax + tip
    return tax, tip, total

def print_receipt(coffee_qty: int, muffin_qty: int, bagel_qty: int,
                  coffee_price: float, muffin_price: float, bagel_price: float,
                  subtotal: float, tax: float, tip: float, total: float) -> None:

    """Print receipt neatly formatted."""
    # Line items
    if coffee_qty > 0:
        print(
            f"Coffees {format_currency(coffee_price)} (ea)........... {coffee_qty} = {format_currency(line_total(coffee_price, coffee_qty))}")
    if muffin_qty > 0:
        print(
            f"Muffins {format_currency(muffin_price)} (ea)........... {muffin_qty} = {format_currency(line_total(muffin_price, muffin_qty))}")
    if bagel_qty > 0:
        print(
            f"Bagels {format_currency(coffee_price)} (ea)........... {bagel_qty} = {format_currency(line_total(bagel_price, bagel_qty))}")

    # Totals
    print(f"\nSubtotal: {format_currency(subtotal)}")
    print(f"Tax:      {format_currency(tax)}")
    print(f"Tip:      {format_currency(tip)}")
    print(f"Total:    {format_currency(total)}")


# -------- Main Program -------- #

# Prices for each item

coffee_price = 1.75
muffin_price = 2.50
bagel_price = 1.50
tax_rate = 0.08875   # 8.875% sales tax

... #the menu
... print('\nWelcome to the Campus Café!')
... print('Today on our menu:')
... print(f'Coffee..........{format_currency(coffee_price)}')
... print(f'Muffins..........{format_currency(muffin_price)}(ea)')
... print(f'Bagels..........{format_currency(bagel_price)}(ea)')
... print()
... 
... 
... coffee_qty = input('How many coffees would you like?: ')
... COFFEE = int(coffee_qty)
... muffin_qty = input('How many muffins would you like?: ')
... MUFFIN = int(muffin_qty)
... bagel_qty = input('How many bagels would you like?: ')
... BAGEL = int(bagel_qty)
... tip_percent = float(input("How much would you like to tip?(10 for 10%): "))
... print()
... 
... #the totals in prices
... print('Total amount of Coffees:', COFFEE)
... print('Total amount of Muffins:', MUFFIN)
... print('Total amount of Bagels:', BAGEL)
... print()
... 
... subtotal = (
...                 line_total(coffee_price, COFFEE) +
...                 line_total(muffin_price, MUFFIN) +
...                 line_total(bagel_price, BAGEL)
...         )
... 
... tax, tip, total = compute_totals(subtotal, tax_rate, tip_percent)
... 
... # Print Receipt
... print("\n------Thank you for coming! Have a wonderful day!-------")
... print('\n-----Receipt-----')
... print_receipt(COFFEE, MUFFIN, BAGEL,
...               coffee_price, muffin_price, bagel_price,
...               subtotal, tax, tip, total)
... 
