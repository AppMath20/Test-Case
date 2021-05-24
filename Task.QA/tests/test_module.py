import pytest
from src.main import analyze_data


class CaseBuild:

    def __init__(self, check_case: bool):
        self.check_case = check_case
        self.name = ""

    def __str__(self) -> str:
        return 'test_{}'.format(self.name)


TEST_CASES_BUILD = list()

TEST_CASES_BUILD.append(
    CaseBuild(
        True
    )
)


@pytest.mark.parametrize(
    'case',
    TEST_CASES_BUILD,
    ids=bool
)
def test_build(case: CaseBuild) -> None:
    check_case = analyze_data()
    assert check_case == case.check_case


if __name__ == '__main__':
    pytest.main()
