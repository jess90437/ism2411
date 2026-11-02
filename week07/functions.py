"""
1. First Bug Spotted (Exercise 5):
   The first bug spotted was a TypeError caused by trying to add/multiply string 
   and numeric types together, identified through reading the traceback error 
   message. This shows that reading error outputs carefully is a strong first 
   debugging step before adding print statements.

2. Plain English Explanation of apply_discount(price, tier):
   The apply_discount function takes a numerical price and a customer membership 
   tier (string) as inputs. It checks the tier against known levels ("gold", 
   "silver", "bronze") to apply the correct percentage reduction and returns 
   the discounted price as a float. A colleague could easily use this function 
   just by knowing the expected parameters without looking at the internal logic.

3. AI Disclosure:
   AI Disclosure: Assisted by AI for code structure review and concept explanation.
"""

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 7%: ${tax2:.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price - (price * 0.15)
    elif tier == "silver":
        return price - (price * 0.10)
    elif tier == "bronze":
        return price - (price * 0.05)
    else:
        return price

print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
gold_price = apply_discount(200, "gold")
tax_amount = calculate_tax(gold_price, 0.07)
final_val = gold_price + tax_amount

print(f"After gold discount: ${gold_price:.2f}")
print(f"After tax: ${final_val:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
def process_sales_data(sales_list):
    total_sales = 0
    for sale in sales_list:
        total_sales += float(sale)
    return total_sales

sample_sales = [100.50, "200.25", 50.00]
print(f"Fixed sales total: ${process_sales_data(sample_sales):.2f}")

# --- Exercise 6 ---
x = 100 # global varible

def double_it():
    x = 999 # loval variable - different from global x
    return x * 2

print(x) # prints 100
print(double_it()) # prints 1998
print(x) # prints 100, global x remains unchanged

# explaination: Global variables are accessible everywhere, 
# but variables created inside functions are local and only live during that function call.