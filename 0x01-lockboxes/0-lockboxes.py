def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n  # Initially all boxes are locked except the first one
    unlocked[0] = True  # The first box is unlocked
    stack = [0]  # Start with the first box
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key >= 0 and key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
