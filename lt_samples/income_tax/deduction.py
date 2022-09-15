"""
医療費控除
基礎控除
"""

from abc import ABC, abstractclassmethod

from lt_samples.income_tax.information import SimpleInformationForTax


class Deduction(ABC):
    @abstractclassmethod
    def calculate_deduction_amount(self, information_for_tax: SimpleInformationForTax):
        pass


class MedicalDeduction(Deduction):
    def calculate_deduction_amount(self, information_for_tax: SimpleInformationForTax):
        if information_for_tax.annual_income > 2000000 and information_for_tax.annual_medical_fee > 100000:
            return min(2000000, information_for_tax.annual_medical_fee - 100000)
        if information_for_tax.annual_income <= 2000000 and information_for_tax.annual_medical_fee > information_for_tax.annual_income * 0.05:
            return min(2000000, information_for_tax.annual_medical_fee)
        return 0


class BaseDeduction(Deduction):
    def calculate_deduction_amount(self, information_for_tax: SimpleInformationForTax):
        if information_for_tax.annual_income > 25000000:
            return 0
        elif information_for_tax.annual_income > 24500000:
            return 160000
        elif information_for_tax.annual_income > 24000000:
            return 320000
        return 480000
