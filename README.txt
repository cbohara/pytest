Notes from Python Testing with pytest by Brian Okken

################################
Ch 1 Getting started with pytest
################################

testing strategy
    unit test   
        checks a small bit of code
        in isolation from the rest of the system
    integration test
        checks a subsystem - several classes or functions
    system test
        end-to-end
        test that checksa ll the system under test 
        in an environment as close to the end-user environment as possible
    functional test
        checks a single bit of functionality of a system
        ex: a test that checks how well we add or delete or update a task item in Tasks
    subcutaneous test
        a test that doesn't run against the final end-user interface
        runs again an interface just below the surface
        ex: test again the API layer, not the CLI 
    
pytest test discovery
    looks for files starting with test_ or ending with _test
    test methods and functions test_
    test classes TestSomething

    $ pytest --collect-only will show all tests

outcomes
    .   passed 
    F   failed 
    s   skipped 
        using @pytest.mark.skip()
    x   xfail 
        expect the test to fail
        ex: note a bug not yet fixed
        @pytest.mark.xfail()
    X   xpass
        still use @pytest.mark.xfail()
        you expected the test to fail but it passed = problematic response
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

######################################################
Appendix 4 Packaging and Distributing Python Projects
######################################################

Includes notes from official documentation
https://docs.python.org/3/tutorial/modules.html#packages

packages = collection of modules
module = python file

__init__.py 
    required to make Python treat the directory as a package
    allows you to import modules within the package
    can be an empty file
    can also execute initialization code
        ex: import things, load things into path, etc

setup.py
    setup script 
    builds, distributes, and installs modules using Distutils
    describe module distribution to Distutils

make a package (contains multiple modules) installable with pip
    need to add __init__.py in the same dir as the module
    
some_package_project
    setup.py                    # setup script makes it possible to build, distribute, and install python modules
    src
        some_package
            __init__.py         # required to treat directory as a package - allows you to import modules from package
            some_module.py

create source distribution
    create your own stash of local project packages for your team
        $ python setup.py sdist
    sdist 
        will create an archive file
        allows end user to install module 
        by downloading the archive file, unpacking it, and from the within the module directory run
        $ python setup.py install

        
###########################
Ch 2 Writing Test Functions
###########################

best practice = install modules locally using pip
    using -e allows me to modify the source code while tasks is installed
    $ pip install -e ./tasks_project/

exact line of failure is shown with >
# lines show you extra info about the assert failure

with pytest.raises(TypeError):
    whatever is in the next block of code should raise a TypeError exception
    if no exception is raised, the test fails
    if the test raises a different exception, it fails

smoke test 
    not all inclusive, thorough test suits
    subset of tests are run to ensure most important functionality works
    
fixture preview
    autouse = all tests in the file will use the fixture
    code before yield runs before each test
    the code after yield runs after each test

skipping tests
    @pytest.skip(reason='some reason')
    @pytest.skipif(any valid python expression, reason='why are we skipping for this reason')

    # display reason for skipping test
    $ pytest -rc module.py

marking tests as expecting to fail
    @pytest.mark.xfail()
    if it returns x then you marked a test you expected to fail and indeed failed
    if it returns X then you marked a test you expected to fail BUT it did not = problematic

#####################
Ch 3 pytest Fixtures
#####################

$ pytest --setup-show 
    shows all the setup and teardown of fixtures 

$ pytest -v --tb=no
    shows all the tests and their parameters
    without repetitive traceback errors

######################
Ch 4 Builtin Fixtures
######################

tmpdir and tmpdir_factory
    tmpdir
        create files or dirs used by a single test
        function scope
    tmpdir_factory
        setup a directory for many tests
        session scope

        default basetemp is in /private/var/...
        can override with pytest --basetemp=mydir

        basedir is left alone after a session
        pytest cleans them up 
