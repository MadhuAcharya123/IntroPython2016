#!usr/bin/env python3

from codingbat import parrot_trouble

# tests for parrot_trouble

def test_parrot_true_6():
    assert parrot_trouble(True,6)


def test_parrot_true_7():
    assert parrot_trouble(True,7) is False


def test_parrot_false_6():
    assert parrot_trouble(False,6) is False


def test_parrot_true_21():
    assert parrot_trouble(True,21)


def test_parrot_false_21():
    assert parrot_trouble(False,21) is False


def test_parrot_false_20():
    assert parrot_trouble(False,20) is False


def test_parrot_true_20():
    assert parrot_trouble(True,20) is False


def test_parrot_false_12():
    assert parrot_trouble(False,12) is False
