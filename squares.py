def generate_squares():
    """Return squares of integers from 1 to 20."""
    return list(map(lambda x:x**2, range(1,21)))


if __name__ == "__main__":
    print(generate_squares())