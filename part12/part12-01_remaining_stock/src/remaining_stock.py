# Write your solution here:
def sort_by_remaining_stock(items: list):
    def order_by_remaining_stock(item):
        return item[2]

    return sorted(items, key=order_by_remaining_stock)
