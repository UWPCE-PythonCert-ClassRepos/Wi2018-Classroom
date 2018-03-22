#!/usr/bin/env python3
import pytest


@pytest.fixture
def clean_database():
    from mailroom4 import init_database
    
    return init_database()


def test_init_database():
    db = clean_database()

    assert ('Mark Zuckerberg' and 'Jeff Bezos') in db.keys()
    assert len(db.keys()) == 5
    # Test that every initial entry has at least one donation
    assert min([len(v['donations']) for k, v in db.items()]) > 0


def test_prompt_for_amount(monkeypatch):
    from mailroom4 import prompt_for_amount
    
    monkeypatch.setattr('builtins.input', lambda x: "$5,501.39")
    
    i = prompt_for_amount("Smith")

    assert i == '5501.39'


def test_add_new_donor():
    from mailroom4 import add_new_donor

    db = clean_database()

    add_new_donor(db, 'Matt Smith', 0.50)

    assert len(db.keys()) == 6
    assert 'Matt Smith' in db.keys()
    assert db['Matt Smith']['latest_don'] == 0.5


def test_add_donation_to_history():
    from mailroom4 import add_donation_to_history

    db = clean_database()

    add_donation_to_history(db, 'John Ferrell', 0.50)

    assert db['John Ferrell']['donations'][-1] == 0.50
    assert len(db['John Ferrell']['donations']) > 1
    assert db['John Ferrell']['latest_don'] == 0.50


def test_verify_add_donor(monkeypatch):
    from mailroom4 import verify_add_donor

    monkeypatch.setattr('builtins.input', lambda x: "")
    assert verify_add_donor('Matt Smith') == 'y'

    monkeypatch.setattr('builtins.input', lambda x: "N")
    assert verify_add_donor('Matt Smith') == 'n'


def test_blank_lines():
    from mailroom4 import blank_lines

    assert blank_lines() == '\n' * 2
    assert blank_lines(3) == '\n' * 4


def test_letter_date():
    import datetime as dt
    from mailroom4 import letter_date

    assert letter_date() == dt.datetime.now().strftime('%d %B %Y')


def test_letter_preamble():
    from mailroom4 import letter_preamble, letter_date

    assert letter_preamble('Matt Smith') == \
        f'{letter_date()}\n\n\nDear Matt Smith,\n\n'


def test_letter_body():
    from mailroom4 import letter_body

    assert 'Thank you for your generous donation of $0.50.' in letter_body(0.50)
    assert 'Thank you for your generous donation of $100.00.' in letter_body(100)


def test_letter_closing():
    from mailroom4 import letter_closing

    assert letter_closing() == \
        '\n\nSincerely,\n\n\nMr. F\nActing Director\n(800) 555-1234'


def test_compose_letter():
    from mailroom4 import compose_letter, letter_preamble, letter_body, letter_closing

    assert compose_letter('Matt Smith', 0.50) == \
        letter_preamble('Matt Smith') + letter_body(0.50) + letter_closing()


def test_print_letter():
    from mailroom4 import print_letter

    brief_letter = 'Hello, world!'

    assert print_letter(brief_letter) == \
        print(f'<BEGIN EMAIL>\n{brief_letter}\n<END EMAIL>')


def test_send_letters_all():
    from mailroom4 import send_letters_all, letter_date
    import os.path

    db = clean_database()

    send_letters_all(db)

    for k, v in db.items():
        fpath = f'letters/{k.replace(",", "").replace(" ", "_")}.txt'
        assert os.path.isfile(fpath)

        with open(fpath, 'r') as file:
            start_file = 
