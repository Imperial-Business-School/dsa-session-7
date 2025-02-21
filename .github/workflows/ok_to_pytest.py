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

def test_bfs_0():
    run_ok_test("test_ses07_solution_bfs_0")

def test_bfs_track_path_0():
    run_ok_test("test_ses07_solution_bfs_track_path_0")

def test_bfs_track_path_1():
    run_ok_test("test_ses07_solution_bfs_track_path_1")

def test_create_bfs_graph_0():
    run_ok_test("test_ses07_solution_create_bfs_graph_0")

def test_create_bfs_graph_1():
    run_ok_test("test_ses07_solution_create_bfs_graph_1")
