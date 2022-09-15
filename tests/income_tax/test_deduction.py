from lt_samples.income_tax.deduction import BaseDeduction, MedicalDeduction
from lt_samples.income_tax.information import SimpleInformationForTax


def test_calculate_deduction_amount():
    information = SimpleInformationForTax(
        annual_income=2000001,
        annual_medical_fee=1000000
    )
    deduction = MedicalDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 900000
    assert expect_value == result


def test_calculate_deduction_amount_2():
    information = SimpleInformationForTax(
        annual_income=2000000,
        annual_medical_fee=1000000
    )
    deduction = MedicalDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 1000000
    assert expect_value == result


def test_calculate_deduction_amount_3():
    information = SimpleInformationForTax(
        annual_income=2000001,
        annual_medical_fee=50000
    )
    deduction = MedicalDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 0
    assert expect_value == result


def test_calculate_deduction_amount_4():
    information = SimpleInformationForTax(
        annual_income=2000000,
        annual_medical_fee=50000
    )
    deduction = MedicalDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 0
    assert expect_value == result


def test_calculate_base_deduction_amount():
    information = SimpleInformationForTax(
        annual_income=25000001,
        annual_medical_fee=50000
    )
    deduction = BaseDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 0
    assert expect_value == result


def test_calculate_base_deduction_amount_2():
    information = SimpleInformationForTax(
        annual_income=24500001,
        annual_medical_fee=50000
    )
    deduction = BaseDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 160000
    assert expect_value == result


def test_calculate_base_deduction_amount_3():
    information = SimpleInformationForTax(
        annual_income=24000001,
        annual_medical_fee=50000
    )
    deduction = BaseDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 320000
    assert expect_value == result


def test_calculate_base_deduction_amount_4():
    information = SimpleInformationForTax(
        annual_income=23000001,
        annual_medical_fee=50000
    )
    deduction = BaseDeduction()
    result = deduction.calculate_deduction_amount(information)
    expect_value = 480000
    assert expect_value == result
