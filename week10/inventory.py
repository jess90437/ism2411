"""
Reflection:
1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
   Lists are surprisingly dynamic and flexible, allowing you to mix data types, modify items in place, 
   and use negative indexing, whereas static arrays in other languages are much more rigid.

2. Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
   During a retail inventory audit, copying and pasting SKU data across multiple sheets in Excel led to manual errors. 
   Using a Python script with list filtering would have automatically processed and flagged low-stock items in seconds.
"""

# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
print("-" * 40)


# --- Exercise 2 ---
first_item = inventory[0]
last_item = inventory[-1]
middle_index = len(inventory) // 2
middle_item = inventory[middle_index]

print(first_item)
print(last_item)
print(middle_item)
print("-" * 40)


# --- Exercise 3 ---
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])
print("-" * 40)


# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)
print("-" * 40)


# --- Exercise 5 ---
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught:", e)
    print("Explanation: Tuples are immutable, which makes them ideal for fixed geographic coordinates that should never accidentally change.")

print(coords)
print("-" * 40)


# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]

total_sales = sum(sales)
count_sales = len(sales)
average_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales}  |  Average: {average_sales}  |  Best: {best_day}  |  Worst: {worst_day}")
print("-" * 40)


# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)
print("-" * 40)


# --- Exercise 8 ---
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print(high_sales)
print(f"Count: {high_count}  |  Avg: ~{high_avg:.2f}")