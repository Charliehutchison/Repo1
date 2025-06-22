import sensitive_terms.txt as sensitive_terms

with open("data/sensitive_terms.txt", "r") as f:
    sensitive_terms = f.read().splitlines()
    print(sensitive_terms)









