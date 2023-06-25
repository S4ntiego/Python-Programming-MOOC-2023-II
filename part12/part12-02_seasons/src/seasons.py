# Write your solution here:
def sort_by_seasons(items: list):
    def order_by_seasons(item):
        return item["seasons"]

    return sorted(items, key=order_by_seasons)
