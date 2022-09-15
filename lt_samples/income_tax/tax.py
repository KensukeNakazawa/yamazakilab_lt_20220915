"""
~ 300 10%

300 ~ 1000 15%

1000 ~ 1500  30%
"""
from typing import List
from lt_samples.income_tax.deduction import Deduction, MedicalDeduction, BaseDeduction
from lt_samples.income_tax.information import SimpleInformationForTax


def single_progressive_tax(target_amount: int, target_tax_amount: int, tax_rate: float, total_target_tax_amount: int) -> int:
    if target_amount < total_target_tax_amount:
        return 0
    if target_amount - target_tax_amount >= 0:
        return int(target_tax_amount * tax_rate)
    else:
        return int((target_amount - total_target_tax_amount) * tax_rate)


def calculate_progressive_tax(deducted_amount: int) -> int:
    tax_amount = 0
    if deducted_amount < 10000:
        return 0

    progressive_tax_rules = [
        [3000000, 0.1],
        [10000000, 0.15],
        [15000000, 0.3],
    ]

    total_amount = 0
    for progressive_tax_rule in progressive_tax_rules:
        tax_amount += single_progressive_tax(deducted_amount, progressive_tax_rule[0], progressive_tax_rule[1], total_amount)
        total_amount += progressive_tax_rule[0]

    return tax_amount


def calculate_income_tax(information_for_tax: SimpleInformationForTax) -> int:
    deductions: List[Deduction] = [
        MedicalDeduction(), BaseDeduction()
    ]
    deducted_amount = sum([deduction.calculate_deduction_amount(information_for_tax) for deduction in deductions])
    income_tax = calculate_progressive_tax( information_for_tax.annual_income - deducted_amount)
    return income_tax
