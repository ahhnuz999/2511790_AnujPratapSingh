def generate_permutations(s):
    if len(s) == 1:
        return [s]

    perms = []
    first = s[0]
    rest = s[1:]
    sub_perms = generate_permutations(rest)

    
    for perm in sub_perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + first + perm[i:]
            perms.append(new_perm)
    return list(set(perms))

print(generate_permutations("abc"))
print(generate_permutations("aab"))
