def load_sensitive_terms(file_path):
    with open("../data/sensitive_terms.txt", "r") as f:
        sensitive_terms = f.read().splitlines()
    return sensitive_terms
terms = load_sensitive_terms("../data/sensitive_terms.txt")
print(terms)

print("This is a test to practice version control")








