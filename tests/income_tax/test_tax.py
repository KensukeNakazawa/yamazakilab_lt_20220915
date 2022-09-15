from lt_samples.income_tax.information import SimpleInformationForTax
from lt_samples.income_tax.tax import single_progressive_tax, calculate_progressive_tax, calculate_income_tax


def test_single_progressive_tax():
    result = single_progressive_tax(15000000, 3000000, 0.1, 0)
    expect_value = 300000
    assert expect_value == result


def test_single_progressive_tax_2():
    result = single_progressive_tax(9000000, 10000000, 0.15, 3000000)
    expect_value = 6000000 * 0.15
    assert expect_value == result


def test_single_progressive_tax_3():
    result = single_progressive_tax(10000001, 15000000, 0.3, 10000000)
    expect_value = 0
    assert expect_value == result


def test_calculate_progressive_tax():
    result = calculate_progressive_tax(9000000)
    expect_value = (3000000 * 0.1) + (6000000 * 0.15)
    assert expect_value == result


def test_calculate_income_tax():
    information = SimpleInformationForTax(
        annual_income=9000000,
        annual_medical_fee=1000000
    )
    # calculate_progressive_tax(annual_income - (900000 + 480000))
    expect_value = (3000000 * 0.1) + (9000000 - (900000 + 480000) - 3000000) * 0.15
    result = calculate_income_tax(information)
    assert expect_value == result
