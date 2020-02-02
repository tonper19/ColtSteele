"""Local function example."""
store = []

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)

if __name__ == "__main__":
    s = sort_by_last_letter(["hello", "from", "a", "local", "function"])
    print(s)
    s = sort_by_last_letter(["sorted", "by", "the", "last", "letter"])
    print(s)
