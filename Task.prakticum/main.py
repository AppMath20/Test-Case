import os
import re
import subprocess
import pytest
import regex as regex

"""
First you need to run the program.
A convenient function for this:
"""


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, shell=True)
    return iter(p.stdout.readline, b'')


"""
It will return iterability with all the output lines.
And you can access the strings.
"""

"""
The string was in binary format (and-string).
To convert it to a regular string,
we need to decode it with 'cp866'.
"""


def return_result(title):
    test = []
    for output_line in run_command(title):
        regex_num = re.compile('\d+')
        test.append(regex_num.findall(output_line.decode('cp866')))
    return test


def read_file():
    jar_decompiler_output = subprocess.Popen('_test_Java.jar', stdout=subprocess.PIPE, shell=True).communicate()[
        0].split(os.linesep)
    return iter(jar_decompiler_output.stdout.readline, b'')


"""
Code analysis to find dependencies.
We use regular expressions for this purpose.
"""


def analyze_code():
    A, B = False, False
    check_1 = "arr[i]"
    text = str(read_java())
    answer_1 = re.findall(r'\bSystem.out.println(.*)\b', text)

    rx = regex.compile(r'''
        \([^()]*\) (* SKIP)(* FAIL)  
        |                          
        arr                     
        ''', re.VERBOSE)
    answer_2 = rx.findall(text)

    if check_1 in answer_1:
        A = True
    if len(answer_2) != 0 and "for" in text:
        B = True
    return A and B


def read_java():
    with open('Student_code.java', 'r') as f:
        list = f.read().splitlines()
    return list


class MyPlugin:
    @staticmethod
    def pytest_sessionfinish():
        print("*** test run reporting finishing")


if __name__ == "__main__":
    # Starting code of student
    print(return_result('java -jar _Student_code.jar'))

    # Starting test module
    pytest.main(["-qq"], plugins=[MyPlugin()])
    pytest.main()
