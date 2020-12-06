def get_answers(lines, use_intersection=False):
    answers = list()
    group_set = set()
    first_line = True
    for li in lines:
        if not li:
            answers.append(group_set)
            group_set = set()
            first_line = True
        else:
            if use_intersection and not first_line:
                group_set.intersection_update(li)
            else:
                group_set.update(li)
            first_line = False
    if group_set:
        answers.append(group_set)
    return answers


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [s.strip() for s in f.readlines()]
    print(sum(len(ga) for ga in get_answers(lines)))
    print(sum(len(ga) for ga in get_answers(lines, use_intersection=True)))
