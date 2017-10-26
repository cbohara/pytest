Notes from Python Testing with pytest by Brian Okken

pytest test discovery
    looks for files starting with test_ or ending with _test
    test methods and functions test_
    test classes TestSomething

outcomes
    .   passed 
    F   failed 
    s   skipped 
        using @pytest.mark.skip()
    x   xfail 
        the test was not supposed to pass, ran, and failed as expected
        @pytest.mark.xfail()
    X   xpass
        the test was not supposed to pass, ran, and passed
    E   error
        exception happened outside the test function

run single test
    pytest filename.py::function
    pytest test_task.py::test_adict

options
    -k      only run tests that match the given substring expression
            ex: -k 'test_other' matches all test functions/classes whose name contains 'test_other'
    -x      exit instantly on first error or failed test
    --lf    rerun only the tests that failed last time
            or all if none failed last time
    --ff    run the test that failed first
            then the rest of the test
    -m      execute only specific markers
            @pytest.mark.some_marker_name
    -v      verbose
    -q      quiet
    -s      print everything that goes to stdout while running the test
    --tb=   traceback print mode 
            auto/long/short/line/native/no
    -collect-only
            shows which tests will be run
    -durations=N
            reports the slowest N number of tests
            -durations=0 will show all

pytest -k 'replace' --collect-only
    show all tests that contain replace

pytest -k 'replace or dict' --collect-only
    show all tests that contain replace or dict

pytest -m run_these_please
    will only run tests with the associated decorator @pytest.mark.run_these_please

pytest -m "magic or just_run_this" -v
    runs both @pytest.mark.run_these_please and @pytest.mark.magic

pytest -s
    can use print statements within code and they will be displayed during test execution

pytest --tb=line
    will just provide the line where the error occurred
