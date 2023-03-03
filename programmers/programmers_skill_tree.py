def solution(skill, skill_trees):
    answer = 0

    def right_skill_tree(skill_tree):
        arr = [0]*len(skill)
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                if 1 in arr[skill.index(skill_tree[i]):len(skill)] or 0 in arr[0:skill.index(skill_tree[i])]:
                    return 0
                arr[skill.index(skill_tree[i])] =1
        return 1




    for i in range(len(skill_trees)):
        answer += right_skill_tree(skill_trees[i])
    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))