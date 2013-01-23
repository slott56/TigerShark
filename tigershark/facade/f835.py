from decimal import Decimal

from tigershark.facade import X12LoopBridge
from tigershark.facade import X12SegmentBridge
from tigershark.facade import ElementAccess
from tigershark.facade import ElementSequenceAccess
from tigershark.facade import CompositeAccess
from tigershark.facade import SegmentSequenceAccess
from tigershark.facade import SegmentConversion
from tigershark.facade import D8
from tigershark.facade import Money
from tigershark.facade import Facade
from tigershark.facade import enum
from tigershark.facade.common import ClaimAdjustment
from tigershark.facade.common import ContactDetails
from tigershark.facade.common import NamedEntity
from tigershark.facade.enums.remittance import remittance_advice_codes
from tigershark.facade.utils import first


class Header(X12LoopBridge):
    loopName = "HEADER"

    class _FinancialInformation(X12LoopBridge):
        """ Use this to address a single payment to a single payee.

        A payee may represent a single provider, a provider group, or multiple
        providers in a chain. The BPR contains mandatory information, even
        when it is not being used to move funds electronically.
        """
        transaction_type = ElementAccess("BPR", 1, x12type=enum(
                {"C": "Payment Accompanies Remittance Advice",
                 "D": "Make Payment Only",
                 "H": "Notification Only",
                 "I": "Remittance Information Only",
                 "P": "Prenotification of Ruture Transfers",
                 "U": "Split Payment and Remittance",
                 "X": "Handling Party's Option to Split Payment and "\
                         "Remittance."}))
        amount = ElementAccess("BPR", 2, x12type=Money)
        credit_or_debit = ElementAccess("BPR", 3, x12type=enum(
                    {"C": "Credit",
                     "D": "Debit"}))
        payment_method = ElementAccess("BPR", 4, x12type=enum(
                {"ACH": "Automated Clearing House (ACH)",
                 "BOP": "Financial Institution Option",
                 "CHK": "Check",
                 "FWT": "Federal Reserve Funds/Wire Transfer - Nonrepetitive",
                 "NON": "Non-payment Data (only for transaction-type=H)"}))
        payment_format = ElementAccess("BPR", 5, x12type=enum(
                {"CCP": "Cash Concentration/Disbursement Plus Addenda",
                 "CTX": "Coporate Trade Exchange"}))
        sender_aba_transit_routing_number = ElementAccess("BPR", 7,
                qualifier=(6, "01"))
        sender_canadian_bank_branch_and_institution_number = ElementAccess(
                "BPR", 7, qualifier=(6, "04"))
        sender_account_type = ElementAccess("BPR", 8, x12type=enum(
                {"DA": "Demand Deposit"}))
        sender_bank_account_number = ElementAccess("BPR", 9)
        sender_id = ElementAccess("BPR", 10)
        sender_supplemental_id = ElementAccess("BPR", 11)

        receiver_aba_transit_routing_number = ElementAccess("BPR", 13,
                qualifier=(12, "01"))
        receiver_canadian_bank_branch_and_institution_number = ElementAccess(
                "BPR", 13, qualifier=(12, "04"))
        receiver_account_type = ElementAccess("BPR", 14, x12type=enum(
                {"DA": "Demand Deposit",
                 "SG": "Savings"}))
        receiver_bank_account_number = ElementAccess("BPR", 15)

        issue_date = ElementAccess("BPR", 16, x12type=D8)

    class _ReassociationTraceNumber(X12LoopBridge):
        """ Uniquely identify this transaction set.

        Also aid in reassociating payments and remittances that have been
        separated.
        """
        trace_type = ElementAccess("TRN", 1, x12type=enum({
                "1": "Current Transaction Trace Numbers"}))
        check_or_eft_trace_number = ElementAccess("TRN", 2)
        payer_id = ElementAccess("TRN", 3)
        originating_company_supplemental_code = ElementAccess("TRN", 4)

    # TODO tests
    class _CurrencyInformation(X12LoopBridge):
        """ Specify the currency and exchange rate, if applicable.

        Only used when the payment is not being made in United States Dollars
        or when the payment is made in a currency different from that in the
        original claim."""
        currency_code = ElementAccess("CUR", 2)
        exchange_rate = ElementAccess("CUR", 3)

    # TODO tests
    class _Receiver(X12LoopBridge):
        """ Used when the receiver of the transaction is not the payee. """
        id = ElementAccess("REF", 2, qualifier=(1, "EV"))

    # TODO tests
    class _Version(X12LoopBridge):
        """ Reports the version number of the adjudication system which
        generated the claim payments.

        This is *NOT* the version number reported in the GS segment of the
        underlying EDI file. This is sometimes used for customer service
        requests, to help track down where an error was introduced."""
        version_number = ElementAccess("REF", 2, qualifier=(1, "F2"))

    class _ProductionDate(X12LoopBridge):
        """ Production date of the claim.

        This *MUST* be supplied when the cutoff date of the adjudication
        system is different from the date of the 835."""
        date = ElementAccess("DTM", 2, qualifier=(1, "405"), x12type=D8)

    def __init__(self, aLoop, *args, **kwargs):
        super(Header, self).__init__(aLoop, *args, **kwargs)
        self.financial_information = Header._FinancialInformation(
                aLoop, *args, **kwargs)
        self.reassociation_trace_number = Header._ReassociationTraceNumber(
                aLoop, *args, **kwargs)
        self.currency_information = Header._CurrencyInformation(
                aLoop, *args, **kwargs)
        self.receiver = Header._Receiver(aLoop, *args, **kwargs)
        self.version = Header._Version(aLoop, *args, **kwargs)
        self.production_date = Header._ProductionDate(aLoop, *args, **kwargs)


class ProviderAdjustments(X12SegmentBridge):
    provider_id = ElementAccess("PLB", 1)
    date = ElementAccess("PLB", 2, x12type=D8)
    reason_1 = ElementAccess("PLB", 3)
    amount_1 = ElementAccess("PLB", 4, x12type=Money)
    reason_2 = ElementAccess("PLB", 5)
    amount_2 = ElementAccess("PLB", 6, x12type=Money)
    reason_3 = ElementAccess("PLB", 7)
    amount_3 = ElementAccess("PLB", 8, x12type=Money)
    reason_4 = ElementAccess("PLB", 9)
    amount_4 = ElementAccess("PLB", 10, x12type=Money)
    reason_5 = ElementAccess("PLB", 11)
    amount_5 = ElementAccess("PLB", 12, x12type=Money)
    reason_6 = ElementAccess("PLB", 13)
    amount_6 = ElementAccess("PLB", 14, x12type=Money)


class Footer(Facade, X12LoopBridge):
    loopName = "FOOTER"

    provider_adjustments = SegmentSequenceAccess("PLB",
            x12type=SegmentConversion(ProviderAdjustments))


class Payer(X12LoopBridge):
    """Payer information from the 1000A loop."""
    loopName = "1000A"
    payer_id = ElementAccess("REF", 2, qualifier=(1, "2U"))
    submitter_id = ElementAccess("REF", 2, qualifier=(1, "EO"))
    # health industry number
    hin = ElementAccess("REF", 2, qualifier=(1, "HI"))
    naic_code = ElementAccess("REF", 2, qualifier=(1, "NF"))

    def __str__(self):
        return "%s, %s %s %s" % (self.last, self.first, self.mid,
                self.suffix)

    def __init__(self, aLoop, *args, **kwargs):
        super(Payer, self).__init__(aLoop, *args, **kwargs)
        self.contact_details = ContactDetails(aLoop, *args, **kwargs)


class Payee(X12LoopBridge):
    """Payee information from 1000B loop."""
    loopName = "1000B"
    state_license = ElementAccess("REF", 2, qualifier=(1, "0B"))
    provider_UPIN = ElementAccess("REF", 2, qualifier=(1, "1G"))
    pharmacy_number = ElementAccess("REF", 2, qualifier=(1, "D3"))
    payee_id = ElementAccess("REF", 2, qualifier=(1, "PQ"))
    tax_id = ElementAccess("REF", 2, qualifier=(1, "TJ"))

    def __init__(self, aLoop, *args, **kwargs):
        super(Payee, self).__init__(aLoop, *args, **kwargs)
        self.contact_details = ContactDetails(aLoop, *args, **kwargs)


class ClaimsOverview(X12LoopBridge):
    loopName = "2000"
    number = ElementAccess("LX", 1)
    provider_id = ElementAccess("TS3", 1)
    facility_type_code = ElementAccess("TS3", 2)
    fiscal_period_end = ElementAccess("TS3", 3, x12type=D8)
    claim_count = ElementAccess("TS3", 4)
    total_claim_charge = ElementAccess("TS3", 5, x12type=Money)
    # All of the below are optional and a 0/None value does not
    # neccessarily mean that value is *actually* 0
    total_covered_charge = ElementAccess("TS3", 6, x12type=Money)
    total_noncovered_charge = ElementAccess("TS3", 7, x12type=Money)
    total_denied_charge = ElementAccess("TS3", 8, x12type=Money)
    total_provider_payment = ElementAccess("TS3", 9, x12type=Money)
    total_interest = ElementAccess("TS3", 10, x12type=Money)
    total_contractual_adjustment = ElementAccess("TS3", 11, x12type=Money)
    total_gramm_rudman_reduction = ElementAccess("TS3", 12, x12type=Money)
    total_msp_payer = ElementAccess("TS3", 13, x12type=Money)
    total_blood_deductible = ElementAccess("TS3", 14, x12type=Money)
    total_non_lab_charge = ElementAccess("TS3", 15, x12type=Money)
    total_coinsurance = ElementAccess("TS3", 16, x12type=Money)
    total_hcpcs_reported_charge = ElementAccess("TS3", 17, x12type=Money)
    total_hspcs_payable = ElementAccess("TS3", 18, x12type=Money)
    total_deductible = ElementAccess("TS3", 19, x12type=Money)
    total_professional_component = ElementAccess("TS3", 20, x12type=Money)
    total_msp_patient_liability_met = ElementAccess("TS3", 21, x12type=Money)
    total_patient_reimbursement = ElementAccess("TS3", 22, x12type=Money)
    total_pip_claim = ElementAccess("TS3", 23, x12type=Money)
    total_pip_adjustment = ElementAccess("TS3", 24, x12type=Money)
    # TODO: TS2 segment


class Claim(Facade, X12LoopBridge):
    class _ServiceInfo(X12LoopBridge):
        """ Oh jeez, I'm so sorry about this mess.

        Each claim has several nested 2110 loops that have additional
        information pertaining to a claim. This is usually when the
        insurance company doesn't want to pay the whole amount billed.
        The only way I could think of to implement this is to do this
        mess of multiple inheritance.

        Rest assured I did not come to this decision lightly."""
        loopName = "2110"
        hcpcs_code = CompositeAccess("SVC", "HC", 1)
        charge = ElementAccess("SVC", 2, x12type=Money)
        payment = ElementAccess("SVC", 3, x12type=Money)
        quantity = ElementAccess("SVC", 5)
        start_date = ElementAccess("DTM", 2, qualifier=(1, "150"),
                x12type=D8)
        end_date = ElementAccess("DTM", 2, qualifier=(1, "151"),
                x12type=D8)
        service_date = ElementAccess("DTM", 2, qualifier=(1, "472"),
                x12type=D8)

        # Identification
        apg_number = ElementAccess("REF", 2, qualifier=(1, "1S"))
        provider_control_number = ElementAccess("REF", 2,
                qualifier=(1, "6R"))
        authorization_number = ElementAccess("REF", 2,
                qualifier=(1, "BB"))
        attachment_code = ElementAccess("REF", 2, qualifier=(1, "E9"))
        prior_authorization_number = ElementAccess("REF", 2,
                qualifier=(1, "G1"))
        predetermination_of_benefits_id = ElementAccess("REF", 2,
                qualifier=(1, "G3"))
        location_number = ElementAccess("REF", 2, qualifier=(1, "LU"))
        rate_code_number = ElementAccess("REF", 2, qualifier=(1, "RB"))
        # TODO: Rendering provider info?

        # Line-item claim amounts
        allowed_amount = ElementAccess("AMT", 2, qualifier=(1, "B6"),
                x12type=Money)
        per_day_limit = ElementAccess("AMT", 2, qualifier=(1, "DY"),
                x12type=Money)
        deduction_amount = ElementAccess("AMT", 2, qualifier=(1, "KH"),
                x12type=Money)
        tax_amount = ElementAccess("AMT", 2, qualifier=(1, "T"),
                x12type=Money)
        total_claim_before_taxes = ElementAccess("AMT", 2,
                qualifier=(1, "T2"), x12type=Money)

        not_covered_quantity = ElementAccess("QTY", 2, qualifier=(1, "NE"))
        notes = ElementSequenceAccess("LQ", 2, qualPos=1, inList=("HE",),
                x12type=enum(remittance_advice_codes, raw_unknowns=True))

        def __init__(self, anX12Message, *args, **kwargs):
            super(Claim._ServiceInfo, self).__init__(anX12Message, *args,
                    **kwargs)
            # Claim adjustments
            self.claim_adjustments = Claim._ClaimAdjustments(anX12Message)

        def get_actual_allowed_amount(self):
            if self.allowed_amount == Decimal('0.00'):
                # Actually means that the allowed amount is the full billed amt
                return self.charge
            return self.allowed_amount

        def get_actual_deductible(self):
            return self.claim_adjustments.patient_responsibility.\
                    total_amount('1')

        def get_actual_coinsurance(self):
            return self.claim_adjustments.patient_responsibility.\
                    total_amount('2')

        def get_actual_copayment(self):
            return self.claim_adjustments.patient_responsibility.\
                    total_amount('3')

    class _ClaimPaymentInfo(X12LoopBridge):
        patient_control_number = ElementAccess("CLP", 1)
        status_code = ElementAccess("CLP", 2, x12type=enum({
                "1": "Processed as Primary",
                "2": "Processed as Secondary",
                "3": "Processed as Tertiary",
                "4": "Denied",
                "19": "Processed as Primary, Forwarded to Additional Payer(s)",
                "20": "Processed as Secondary, Forwarded to Additional "\
                        "Payer(s)",
                "21": "Processed as Tertiary, Forwarded to Additional "\
                        "Payer(s)",
                "22": "Reversal of Previous Payment",
                "23": "Not Our Claim, Forwarded to Additional Payer(s)",
                "25": "Predetermination Pricing Only - No Payment"}))
        total_charge = ElementAccess("CLP", 3, x12type=Money)
        payment = ElementAccess("CLP", 4, x12type=Money)
        patient_responsibility = ElementAccess("CLP", 5, x12type=Money)
        claim_type = ElementAccess("CLP", 6, x12type=enum({
                "12": "Preferred Provider Organization (PPO)",
                "13": "Point of Service (POS)",
                "14": "Exclusive Provider Organization (EPO)",
                "15": "Indemnity Insurance",
                "16": "Health Maintenance Organization (HMO) Medicare Risk",
                "AM": "Automobile Medical",
                "CH": "Champus",
                "DS": "Disability",
                "HM": "Health Maintenance Organization",
                "LM": "Liability Medical",
                "MA": "Medicare Part A",
                "MB": "Medicare Part B",
                "MC": "Medicaid",
                "OF": "Other Federal Program",
                "TV": "Title V",
                "VA": "Veteran Administration Plan",
                "WC": "Workers Compensation Health Claim"}))
        payer_claim_control_number = ElementAccess("CLP", 7)
        facility_type = ElementAccess("CLP", 8)
        frequency_code = ElementAccess("CLP", 9)
        diagnosis_related_group_weight = ElementAccess("CLP", 11)
        discharge_fraction = ElementAccess("CLP", 12)
        # TODO: Medicare inpatient/outpatient adjudication?

        total_covered_charge = ElementAccess("AMT", 2, qualifier=(1, "AU"),
                x12type=Money)
        discount_amount = ElementAccess("AMT", 2, qualifier=(1, "D8"),
                x12type=Money)
        per_day_limit = ElementAccess("AMT", 2, qualifier=(1, "DY"),
                x12type=Money)
        patient_amount_paid = ElementAccess("AMT", 2, qualifier=(1, "F5"),
                x12type=Money)
        interest = ElementAccess("AMT", 2, qualifier=(1, "I"), x12type=Money)
        negative_ledger = ElementAccess("AMT", 2, qualifier=(1, "NL"),
                x12type=Money)
        tax_amount = ElementAccess("AMT", 2, qualifier=(1, "T"), x12type=Money)
        total_claim_before_taxes = ElementAccess("AMT", 2,
                qualifier=(1, "T2"), x12type=Money)

    class _ClaimAdjustments(X12LoopBridge):
        def __init__(self, aLoop, *args, **kwargs):
            super(Claim._ClaimAdjustments, self).__init__(aLoop, *args,
                    **kwargs)
            self.contractual_obligation = ClaimAdjustment(aLoop,
                    qualifier=(1, "CO"))
            self.correction_and_reversal = ClaimAdjustment(aLoop,
                    qualifier=(1, "CR"))
            self.other = ClaimAdjustment(aLoop, qualifier=(1, "OA"))
            self.payor_initiated_reductions = ClaimAdjustment(aLoop,
                    qualifier=(1, "PI"))
            self.patient_responsibility = ClaimAdjustment(aLoop,
                    qualifier=(1, "PR"))

    loopName = "2100"

    # References
    group_or_policy_number = ElementAccess("REF", 2, qualifier=(1, "1L"))
    member_id = ElementAccess("REF", 2, qualifier=(1, "1W"))
    repriced_claim_reference_number = ElementAccess("REF", 2,
            qualifier=(1, "9A"))
    adjusted_repriced_claim_reference_number = ElementAccess("REF", 2,
            qualifier=(1, "9B"))
    employee_id = ElementAccess("REF", 2, qualifier=(1, "A6"))
    authorization_number = ElementAccess("REF", 2, qualifier=(1, "BB"))
    contract_class = ElementAccess("REF", 2, qualifier=(1, "CE"))
    medical_record_id = ElementAccess("REF", 2, qualifier=(1, "EA"))
    original_reference_number = ElementAccess("REF", 2,
            qualifier=(1, "F8"))
    prior_authorization_number = ElementAccess("REF", 2,
            qualifier=(1, "G1"))
    predetermination_of_benefits_number = ElementAccess("REF", 2,
            qualifier=(1, "G3"))
    insurance_policy_number = ElementAccess("REF", 2, qualifier=(1, "IG"))
    ssn = ElementAccess("REF", 2, qualifier=(1, "SY"))

    provider_commercial_number = ElementAccess("REF", 2,
            qualifier=(1, "G2"))

    # Dates
    date_expiration = ElementAccess("DTM", 2, qualifier=(1, "036"),
            x12type=D8)
    date_received = ElementAccess("DTM", 2, qualifier=(1, "050"),
            x12type=D8)
    date_statement_period_start = ElementAccess("DTM", 2,
            qualifier=(1, "232"), x12type=D8)
    date_statement_period_end = ElementAccess("DTM", 2,
            qualifier=(1, "233"), x12type=D8)

    def __init__(self, anX12Message, *args, **kwargs):
        super(Claim, self).__init__(anX12Message, *args,
                **kwargs)
        self.claim_adjustments = self._ClaimAdjustments(
                anX12Message)
        self.line_items = self.loops(self._ServiceInfo, anX12Message)
        # Take advantage of ElementAccess attributes inheriting their parent's
        # qualifier. This needs to be fixed someday.
        self.patient = NamedEntity(anX12Message, qualifier=(1, "QC"))
        self.insured = NamedEntity(anX12Message, qualifier=(1, "IL"))
        self.corrected_insured = NamedEntity(anX12Message,
                qualifier=(1, "74"))
        self.service_provider = NamedEntity(anX12Message,
                qualifier=(1, "82"))
        self.crossover_carrier = NamedEntity(anX12Message,
                qualifier=(1, "TT"))
        self.corrected_priority_payer = NamedEntity(anX12Message,
                qualifier=(1, "PR"))
        self.payment_info = self._ClaimPaymentInfo(anX12Message)

    def get_actual_allowed_amount(self):
        s = Decimal('0.00')
        for li in self.line_items:
            s += li.get_actual_allowed_amount()
        return s

    def get_actual_deductible(self):
        s = self.claim_adjustments.patient_responsibility.total_amount('1')
        for li in self.line_items:
            s += li.get_actual_deductible()
        return s

    def get_actual_coinsurance(self):
        s = self.claim_adjustments.patient_responsibility.total_amount('2')
        for li in self.line_items:
            s += li.get_actual_coinsurance()
        return s

    def get_actual_copayment(self):
        s = self.claim_adjustments.patient_responsibility.total_amount('3')
        for li in self.line_items:
            s += li.get_actual_copayment()
        return s


class F835_4010(Facade):
    def __init__(self, anX12Message):
        """Examine the message and extract the relevant Loops."""
        st_loops = anX12Message.descendant('LOOP', name='ST_LOOP')
        if len(st_loops) > 0:
            self.facades = []
            for loop in st_loops:
                self.facades.append(F835_4010(loop))
        else:
            self.header = first(self.loops(Header, anX12Message))
            self.payer = first(self.loops(Payer, anX12Message))
            self.payee = first(self.loops(Payee, anX12Message))
            self.claims_overview = first(self.loops(ClaimsOverview,
                anX12Message))
            self.claims = self.loops(Claim, anX12Message)
            self.footer = first(self.loops(Footer, anX12Message))
