from copy import deepcopy

def main():
    ingredient_set = set()
    allergen_set = set()
    match_lookup = dict()
    ingredient_history = list()

    #fn = 'test.txt'
    fn = 'input.txt'
    with open(fn, 'r') as f:
        for li in f.read().splitlines():
            s1, s2 = li.split(' (contains ')
            s2 = s2[:-1]
            row_ingredients = set(s1.split())
            ingredient_history.extend(row_ingredients)
            row_allergens = set(s2.split(', '))
            ingredient_set.update(row_ingredients)
            allergen_set.update(row_allergens)

            for allergen in row_allergens:
                matches = match_lookup.get(allergen, None)
                if matches is None:
                    match_lookup[allergen] = deepcopy(row_ingredients)
                else:
                    matches.intersection_update(row_ingredients)

    print('#ingredients: %d'%len(ingredient_set))
    print('#allergens: %d'%len(allergen_set))

    changed = True
    while changed:
        changed = False
        for allergen, matches in match_lookup.items():
            if len(matches) == 1:
                ing = list(matches)[0]
                for other_allergen, other_matches in match_lookup.items():
                    if other_allergen is allergen:
                        continue
                    try:
                        other_matches.remove(ing)
                        changed = True
                    except KeyError:
                        pass

    bad_ingredients = set()
    for allergen, matches in match_lookup.items():
        bad_ingredients.update(matches)

    n = 0
    for ingredient in ingredient_history:
        if ingredient not in bad_ingredients:
            n += 1
    print(n)

    bad_pairs = print(','.join([x[1].pop() for x in sorted(list(match_lookup.items()))]))


if __name__ == '__main__':
    main()
