import subprocess
import sys

def run_ok_test(test_name):
    """Run ok --score and check the score for a specific test"""
    result = subprocess.run([sys.executable, 'ok', '--score'], capture_output=True, text=True)
    
    # Find score for specific test
    for line in result.stdout.split('\n'):
        if test_name in line and ': ' in line:
            score_part = line.split(': ')[1]
            actual_score, total_score = map(float, score_part.split('/'))
            assert actual_score == total_score, f"{test_name} received {actual_score}/{total_score} points instead of full credit"
            return
    
    # If we didn't find the test
    assert False, f"Could not find score for {test_name}"

def test_count_characters_0():
    run_ok_test("test_ses06_solution_count_characters_0")

def test_count_characters_1():
    run_ok_test("test_ses06_solution_count_characters_1")

def test_count_characters_2():
    run_ok_test("test_ses06_solution_count_characters_2")

def test_count_characters_3():
    run_ok_test("test_ses06_solution_count_characters_3")

def test_count_words_0():
    run_ok_test("test_ses06_solution_count_words_0")

def test_count_words_1():
    run_ok_test("test_ses06_solution_count_words_1")

def test_divide_0():
    run_ok_test("test_ses06_solution_divide_0")

def test_divide_1():
    run_ok_test("test_ses06_solution_divide_1")

def test_print_dict_values_0():
    run_ok_test("test_ses06_solution_print_dict_values_0")

def test_print_dict_values_1():
    run_ok_test("test_ses06_solution_print_dict_values_1")
