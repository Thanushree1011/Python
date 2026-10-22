def remove_duplicates(values):
    """Removes duplicates from a list while preserving the order of elements. """
    seen = set()
    result = []


    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    num = [12,24,35,24,88,120,155,88,120,155]
    print(remove_duplicates(num))