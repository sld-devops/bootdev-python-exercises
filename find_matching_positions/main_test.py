from main import *

run_cases = [
    (["potion", "map", "potion", "rope", "potion"], "potion", [0, 2, 4]),
    (["red", "blue", "green", "blue"], "blue", [1, 3]),
    (["coin", "gem", "key"], "key", [2]),
]

submit_cases = run_cases + [
    ([], "potion", []),
    (["north", "south", "east", "west"], "up", []),
    (
        ["slime", "bat", "slime", "wolf", "slime", "bat", "slime"],
        "slime",
        [0, 2, 4, 6],
    ),
]


def test(items, target, expected_output):
    print("---------------------------------")
    print(f"Items:  {items}")
    print(f"Target: {target}")
    print("")
    result = find_matching_positions(items, target)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False



def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")



test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()