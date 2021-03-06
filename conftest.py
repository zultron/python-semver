import pytest
import semver
import sys

sys.path.insert(0, "docs")

from coerce import coerce  # noqa:E402


@pytest.fixture(autouse=True)
def add_semver(doctest_namespace):
    doctest_namespace["semver"] = semver
    doctest_namespace["coerce"] = coerce
