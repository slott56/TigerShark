from tigershark.facade import X12LoopBridge


claim_adjustment_reasons = {
    "1": "Deductible Amount",
    "2": "Coinsurance Amount",
    "3": "Co-payment Amount",
    "4": "The procedure code is inconsistent with the modifier used or " \
        "a required modifier is missing. Note: Refer to the 835 Healthcare " \
        "Policy Identification Segment (loop 2110 Service Payment " \
        "Information REF), if present.",
    "5": "The procedure code/bill type is inconsistent with the place " \
        "of service. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "6": "The procedure/revenue code is inconsistent with the " \
        "patient's age. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "7": "The procedure/revenue code is inconsistent with the " \
        "patient's gender. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "8": "The procedure code is inconsistent with the provider " \
        "type/specialty (taxonomy). Note: Refer to the 835 Healthcare " \
        "Policy Identification Segment (loop 2110 Service Payment " \
        "Information REF), if present.",
    "9": "The diagnosis is inconsistent with the patient's age. Note: " \
        "Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "10": "The diagnosis is inconsistent with the patient's gender. " \
        "Note: Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "11": "The diagnosis is inconsistent with the procedure. Note: " \
        "Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "12": "The diagnosis is inconsistent with the provider type. Note: " \
        "Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "13": "The date of death precedes the date of service.",
    "14": "The date of birth follows the date of service.",
    "15": "The authorization number is missing, invalid, or does not " \
        "apply to the billed services or provider.",
    "16": "Claim/service lacks information which is needed for " \
        "adjudication. At least one Remark Code must be provided (may be " \
        "comprised of either the NCPDP Reject Reason Code, or " \
        "Remittance Advice Remark Code that is not an ALERT.)",
    "18": "Duplicate claim/service. This change effective 1/1/2013: " \
        "Exact duplicate claim/service (Use with Group Code OA).",
    "19": "This is a work-related injury/illness and thus the " \
        "liability of the Worker's Compensation Carrier.",
    "20": "This injury/illness is covered by the liability carrier.",
    "21": "This injury/illness is the liability of the no-fault " \
        "carrier.",
    "22": "This care may be covered by another payer per coordination " \
        "of benefits.",
    "23": "The impact of prior payer(s) adjudication including " \
        "payments and/or adjustments.",
    "24": "Charges are covered under a capitation agreement/managed " \
        "care plan.",
    "26": "Expenses incurred prior to coverage.",
    "27": "Expenses incurred after coverage terminated.",
    "29": "The time limit for filing has expired.",
    "31": "Patient cannot be identified as our insured.",
    "32": "Our records indicate that this dependent is not an eligible " \
        "dependent as defined.",
    "33": "Insured has no dependent coverage.",
    "34": "Insured has no coverage for newborns.",
    "35": "Lifetime benefit maximum has been reached.",
    "38": "Services not provided or authorized by designated " \
        "(network/primary care) providers.",
    "39": "Services denied at the time authorization/pre-certification " \
        "was requested.",
    "40": "Charges do not meet qualifications for emergent/urgent " \
        "care. Note: Refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment Information REF), if present.",
    "44": "Prompt-pay discount.",
    "45": "Charge exceeds fee schedule/maximum allowable or " \
        "contracted/legislated fee arrangement. (Use Group Codes PR or CO " \
        "depending upon liability).",
    "49": "These are non-covered services because this is a routine " \
        "exam or screening procedure done in conjunction with a routine " \
        "exam. Note: Refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment Information REF), if present.",
    "50": "These are non-covered services because this is not deemed a " \
        "'medical necessity' by the payer. Note: Refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "51": "These are non-covered services because this is a " \
        "pre-existing condition. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "53": "Services by an immediate relative or a member of the same " \
        "household are not covered.",
    "54": "Multiple physicians/assistants are not covered in this " \
        "case. Note: Refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment Information REF), if present.",
    "55": "Procedure/treatment is deemed experimental/investigational " \
        "by the payer. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "56": "Procedure/treatment has not been deemed 'proven to be " \
        "effective' by the payer. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "58": "Treatment was deemed by the payer to have been rendered in " \
        "an inappropriate or invalid place of service. Note: Refer to the " \
        "835 Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "59": "Processed based on multiple or concurrent procedure rules. " \
        "(For example multiple surgery or diagnostic imaging, concurrent " \
        "anesthesia.) Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "60": "Charges for outpatient services are not covered when " \
        "performed within a period of time prior to or after inpatient " \
        "services.",
    "61": "Penalty for failure to obtain second surgical opinion. " \
        "Note: Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "66": "Blood Deductible.",
    "69": "Day outlier amount.",
    "70": "Cost outlier - Adjustment to compensate for additional " \
        "costs.",
    "74": "Indirect Medical Education Adjustment.",
    "75": "Direct Medical Education Adjustment.",
    "76": "Disproportionate Share Adjustment.",
    "78": "Non-Covered days/Room charge adjustment.",
    "85": "Patient Interest Adjustment (Use Only Group code PR) Notes: " \
        "Only use when the payment of interest is the responsibility of the " \
        "patient.",
    "89": "Professional fees removed from charges.",
    "90": "Ingredient cost adjustment. Note: To be used for " \
        "pharmaceuticals only.",
    "91": "Dispensing fee adjustment.",
    "94": "Processed in Excess of charges.",
    "95": "Plan procedures not followed.",
    "96": "Non-covered charge(s). At least one Remark Code must be " \
        "provided (may be comprised of either the NCPDP Reject Reason Code, " \
        "or Remittance Advice Remark Code that is not an ALERT.) Note: " \
        "Refer to the 835 Healthcare Policy Identification Segment (loop " \
        "2110 Service Payment Information REF), if present.",
    "97": "The benefit for this service is included in the " \
        "payment/allowance for another service/procedure that has already " \
        "been adjudicated. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "100": "Payment made to patient/insured/responsible " \
        "party/employer.",
    "101": "Predetermination: anticipated payment upon completion of " \
        "services or claim adjudication.",
    "102": "Major Medical Adjustment.",
    "103": "Provider promotional discount (e.g., Senior citizen " \
        "discount).",
    "104": "Managed care withholding.",
    "105": "Tax withholding.",
    "106": "Patient payment option/election not in effect.",
    "107": "The related or qualifying claim/service was not identified " \
        "on this claim. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "108": "Rent/purchase guidelines were not met. Note: Refer to the " \
        "835 Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "109": "Claim not covered by this payer/contractor. You must send " \
        "the claim to the correct payer/contractor. This change effective " \
        "11/1/2012: Claim/service not covered by this payer/contractor. You " \
        "must send the claim/service to the correct payer/contractor.",
    "110": "Billing date predates service date.",
    "111": "Not covered unless the provider accepts assignment.",
    "112": "Service not furnished directly to the patient and/or not " \
        "documented.",
    "114": "Procedure/product not approved by the Food and Drug " \
        "Administration.",
    "115": "Procedure postponed, canceled, or delayed.",
    "116": "The advance indemnification notice signed by the patient " \
        "did not comply with requirements.",
    "117": "Transportation is only covered to the closest facility " \
        "that can provide the necessary care.",
    "118": "ESRD network support adjustment.",
    "119": "Benefit maximum for this time period or occurrence has " \
        "been reached.",
    "121": "Indemnification adjustment - compensation for outstanding " \
        "member responsibility.",
    "122": "Psychiatric reduction.",
    "125": "Submission/billing error(s). At least one Remark Code must " \
        "be provided (may be comprised of either the NCPDP Reject Reason " \
        "Code, or Remittance Advice Remark Code that is not an ALERT.)",
    "128": "Newborn's services are covered in the mother's " \
        "Allowance.",
    "129": "Prior processing information appears incorrect. At least " \
        "one Remark Code must be provided (may be comprised of either the " \
        "NCPDP Reject Reason Code, or Remittance Advice Remark Code that is " \
        "not an ALERT.)",
    "130": "Claim submission fee.",
    "131": "Claim specific negotiated discount.",
    "132": "Prearranged demonstration project adjustment.",
    "133": "The disposition of this claim/service is pending further " \
        "review.",
    "134": "Technical fees removed from charges.",
    "135": "Interim bills cannot be processed.",
    "136": "Failure to follow prior payer's coverage rules. (Use Group " \
        "Code OA).",
    "137": "Regulatory Surcharges, Assessments, Allowances or Health " \
        "Related Taxes.",
    "138": "Appeal procedures not followed or time limits not met.",
    "139": "Contracted funding agreement - Subscriber is employed by " \
        "the provider of services.",
    "140": "Patient/Insured health identification number and name do " \
        "not match.",
    "141": "Claim spans eligible and ineligible periods of coverage.",
    "142": "Monthly Medicaid patient liability amount.",
    "143": "Portion of payment deferred.",
    "144": "Incentive adjustment, e.g. preferred product/service.",
    "146": "Diagnosis was invalid for the date(s) of service " \
        "reported.",
    "147": "Provider contracted/negotiated rate expired or not on " \
        "file.",
    "148": "Information from another provider was not provided or was " \
        "insufficient/incomplete. At least one Remark Code must be provided " \
        "(may be comprised of either the NCPDP Reject Reason Code, or " \
        "Remittance Advice Remark Code that is not an ALERT.)",
    "149": "Lifetime benefit maximum has been reached for this " \
        "service/benefit category.",
    "150": "Payer deems the information submitted does not support " \
        "this level of service.",
    "151": "Payment adjusted because the payer deems the information " \
        "submitted does not support this many/frequency of services.",
    "152": "Payer deems the information submitted does not support " \
        "this length of service. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "153": "Payer deems the information submitted does not support " \
        "this dosage.",
    "154": "Payer deems the information submitted does not support " \
        "this day's supply.",
    "155": "Patient refused the service/procedure.",
    "157": "Service/procedure was provided as a result of an act of " \
        "war.",
    "158": "Service/procedure was provided outside of the United " \
        "States.",
    "159": "Service/procedure was provided as a result of terrorism.",
    "160": "Injury/illness was the result of an activity that is a " \
        "benefit exclusion.",
    "161": "Provider performance bonus",
    "162": "State-mandated Requirement for Property and Casualty, see " \
        "Claim Payment Remarks Code for specific explanation.",
    "163": "Attachment referenced on the claim was not received.",
    "164": "Attachment referenced on the claim was not received in a " \
        "timely fashion.",
    "165": "Referral absent or exceeded.",
    "166": "These services were submitted after this payers " \
        "responsibility for processing claims under this plan ended.",
    "167": "This (these) diagnosis(es) is (are) not covered. Note: " \
        "Refer to the 835 Healthcare Policy Identification Segment (loop " \
        "2110 Service Payment Information REF), if present.",
    "168": "Service(s) have been considered under the patient's " \
        "medical plan. Benefits are not available under this dental plan.",
    "169": "Alternate benefit has been provided.",
    "170": "Payment is denied when performed/billed by this type of " \
        "provider. Note: Refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment Information REF), if present.",
    "171": "Payment is denied when performed/billed by this type of " \
        "provider in this type of facility. Note: Refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "172": "Payment is adjusted when performed/billed by a provider of " \
        "this specialty. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "173": "Service was not prescribed by a physician.",
    "174": "Service was not prescribed prior to delivery.",
    "175": "Prescription is incomplete.",
    "176": "Prescription is not current.",
    "177": "Patient has not met the required eligibility " \
        "requirements.",
    "178": "Patient has not met the required spend down " \
        "requirements.",
    "179": "Patient has not met the required waiting requirements. " \
        "Note: Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "180": "Patient has not met the required residency requirements.",
    "181": "Procedure code was invalid on the date of service.",
    "182": "Procedure modifier was invalid on the date of service.",
    "183": "The referring provider is not eligible to refer the " \
        "service billed. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "184": "The prescribing/ordering provider is not eligible to " \
        "prescribe/order the service billed. Note: Refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "185": "The rendering provider is not eligible to perform the " \
        "service billed. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "186": "Level of care change adjustment.",
    "187": "Consumer Spending Account payments (includes but is not " \
        "limited to Flexible Spending Account, Health Savings Account, " \
        "Health Reimbursement Account, etc.)",
    "188": "This product/procedure is only covered when used according " \
        "to FDA recommendations.",
    "189": "'Not otherwise classified' or 'unlisted' procedure code " \
        "(CPT/HCPCS) was billed when there is a specific procedure code for " \
        "this procedure/service",
    "190": "Payment is included in the allowance for a Skilled Nursing " \
        "Facility (SNF) qualified stay.",
    "191": "Not a work related injury/illness and thus not the " \
        "liability of the workers' compensation carrier Note: If adjustment " \
        "is at the Claim Level, the payer must send and the provider should " \
        "refer to the 835 Insurance Policy Number Segment (Loop 2100 Other " \
        "Claim Related Information REF qualifier 'IG') for the " \
        "jurisdictional regulation. If adjustment is at the Line Level, the " \
        "payer must send and the provider should refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment information REF)",
    "192": "Non standard adjustment code from paper remittance. Note: " \
        "This code is to be used by providers/payers providing Coordination " \
        "of Benefits information to another payer in the 837 transaction " \
        "only. This code is only used when the non-standard code cannot be " \
        "reasonably mapped to an existing Claims Adjustment Reason Code, " \
        "specifically Deductible, Coinsurance and Co-payment.",
    "193": "Original payment decision is being maintained. Upon " \
        "review, it was determined that this claim was processed " \
        "properly.",
    "194": "Anesthesia performed by the operating physician, the " \
        "assistant surgeon or the attending physician.",
    "195": "Refund issued to an erroneous priority payer for this " \
        "claim/service.",
    "197": "Precertification/authorization/notification absent.",
    "198": "Precertification/authorization exceeded.",
    "199": "Revenue code and Procedure code do not match.",
    "200": "Expenses incurred during lapse in coverage",
    "201": "Workers Compensation case settled. Patient is responsible " \
        "for amount of this claim/service through WC 'Medicare set aside " \
        "arrangement' or other agreement. (Use group code PR).",
    "202": "Non-covered personal comfort or convenience services.",
    "203": "Discontinued or reduced service.",
    "204": "This service/equipment/drug is not covered under the " \
        "patient's current benefit plan",
    "205": "Pharmacy discount card processing fee",
    "206": "National Provider Identifier - missing.",
    "207": "National Provider identifier - Invalid format",
    "208": "National Provider Identifier - Not matched.",
    "209": "Per regulatory or other agreement. The provider cannot " \
        "collect this amount from the patient. However, this amount may be " \
        "billed to subsequent payer. Refund to patient if collected. (Use " \
        "Group code OA)",
    "210": "Payment adjusted because pre-certification/authorization " \
        "not received in a timely fashion",
    "211": "National Drug Codes (NDC) not eligible for rebate, are not " \
        "covered.",
    "212": "Administrative surcharges are not covered",
    "213": "Non-compliance with the physician self referral " \
        "prohibition legislation or payer policy.",
    "214": "Workers' Compensation claim adjudicated as " \
        "non-compensable. This Payer not liable for claim or " \
        "service/treatment. Note: If adjustment is at the Claim Level, the " \
        "payer must send and the provider should refer to the 835 Insurance " \
        "Policy Number Segment (Loop 2100 Other Claim Related Information " \
        "REF qualifier 'IG') for the jurisdictional regulation. If " \
        "adjustment is at the Line Level, the payer must send and the " \
        "provider should refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment information REF). To be used " \
        "for Workers' Compensation only",
    "215": "Based on subrogation of a third party settlement",
    "216": "Based on the findings of a review organization",
    "217": "Based on payer reasonable and customary fees. No maximum " \
        "allowable defined by legislated fee arrangement. (Note: To be used " \
        "for Workers' Compensation only)",
    "218": "Based on entitlement to benefits. Note: If adjustment is " \
        "at the Claim Level, the payer must send and the provider should " \
        "refer to the 835 Insurance Policy Number Segment (Loop 2100 Other " \
        "Claim Related Information REF qualifier 'IG') for the " \
        "jurisdictional regulation. If adjustment is at the Line Level, the " \
        "payer must send and the provider should refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment information REF). To be used for Workers' Compensation " \
        "only",
    "219": "Based on extent of injury. Note: If adjustment is at the " \
        "Claim Level, the payer must send and the provider should refer to " \
        "the 835 Insurance Policy Number Segment (Loop 2100 Other Claim " \
        "Related Information REF qualifier 'IG') for the jurisdictional " \
        "regulation. If adjustment is at the Line Level, the payer must " \
        "send and the provider should refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment information " \
        "REF).",
    "220": "The applicable fee schedule does not contain the billed " \
        "code. Please resubmit a bill with the appropriate fee schedule " \
        "code(s) that best describe the service(s) provided and supporting " \
        "documentation if required. (Note: To be used for Workers' " \
        "Compensation only)",
    "221": "Workers' Compensation claim is under investigation. Note: " \
        "If adjustment is at the Claim Level, the payer must send and the " \
        "provider should refer to the 835 Insurance Policy Number Segment " \
        "(Loop 2100 Other Claim Related Information REF qualifier 'IG') for " \
        "the jurisdictional regulation. If adjustment is at the Line Level, " \
        "the payer must send and the provider should refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment information REF).",
    "222": "Exceeds the contracted maximum number of hours/days/units " \
        "by this provider for this period. This is not patient specific. " \
        "Note: Refer to the 835 Healthcare Policy Identification Segment " \
        "(loop 2110 Service Payment Information REF), if present.",
    "223": "Adjustment code for mandated federal, state or local " \
        "law/regulation that is not already covered by another code and is " \
        "mandated before a new code can be created.",
    "224": "Patient identification compromised by identity theft. " \
        "Identity verification required for processing this and future " \
        "claims.",
    "225": "Penalty or Interest Payment by Payer (Only used for plan " \
        "to plan encounter reporting within the 837)",
    "226": "Information requested from the Billing/Rendering Provider " \
        "was not provided or was insufficient/incomplete. At least one " \
        "Remark Code must be provided (may be comprised of either the NCPDP " \
        "Reject Reason Code, or Remittance Advice Remark Code that is not " \
        "an ALERT.)",
    "227": "Information requested from the patient/insured/responsible " \
        "party was not provided or was insufficient/incomplete. At least " \
        "one Remark Code must be provided (may be comprised of either the " \
        "NCPDP Reject Reason Code, or Remittance Advice Remark Code that is " \
        "not an ALERT.)",
    "228": "Denied for failure of this provider, another provider or " \
        "the subscriber to supply requested information to a previous payer " \
        "for their adjudication",
    "229": "Partial charge amount not considered by Medicare due to " \
        "the initial claim Type of Bill being 12X. Note: This code can only " \
        "be used in the 837 transaction to convey Coordination of Benefits " \
        "information when the secondary payer's cost avoidance policy " \
        "allows providers to bypass claim submission to a prior payer. Use " \
        "Group Code PR.",
    "230": "No available or correlating CPT/HCPCS code to describe " \
        "this service. Note: Used only by Property and Casualty.",
    "231": "Mutually exclusive procedures cannot be done in the same " \
        "day/setting. Note: Refer to the 835 Healthcare Policy " \
        "Identification Segment (loop 2110 Service Payment Information " \
        "REF), if present.",
    "232": "Institutional Transfer Amount. Note - Applies to " \
        "institutional claims only and explains the DRG amount difference " \
        "when the patient care crosses multiple institutions.",
    "233": "Services/charges related to the treatment of a " \
        "hospital-acquired condition or preventable medical error.",
    "234": "This procedure is not paid separately. At least one Remark " \
        "Code must be provided (may be comprised of either the NCPDP Reject " \
        "Reason Code, or Remittance Advice Remark Code that is not an " \
        "ALERT.)",
    "235": "Sales Tax",
    "236": "This procedure or procedure/modifier combination is not " \
        "compatible with another procedure or procedure/modifier " \
        "combination provided on the same day according to the National " \
        "Correct Coding Initiative.",
    "237": "Legislated/Regulatory Penalty. At least one Remark Code " \
        "must be provided (may be comprised of either the NCPDP Reject " \
        "Reason Code, or Remittance Advice Remark Code that is not an " \
        "ALERT.)",
    "238": "Claim spans eligible and ineligible periods of coverage, " \
        "this is the reduction for the ineligible period (use Group Code " \
        "PR).",
    "239": "Claim spans eligible and ineligible periods of coverage. " \
        "Rebill separate claims (use Group Code OA). This change effective " \
        "11/1/2012: Claim spans eligible and ineligible periods of " \
        "coverage. Rebill separate claims.",
    "A0": "Patient refund amount.",
    "A1": "Claim/Service denied. At least one Remark Code must be " \
        "provided (may be comprised of either the NCPDP Reject Reason Code, " \
        "or Remittance Advice Remark Code that is not an ALERT.)",
    "A5": "Medicare Claim PPS Capital Cost Outlier Amount.",
    "A6": "Prior hospitalization or 30 day transfer requirement not " \
        "met.",
    "A7": "Presumptive Payment Adjustment",
    "A8": "Ungroupable DRG.",
    "B1": "Non-covered visits.",
    "B4": "Late filing penalty.",
    "B5": "Coverage/program guidelines were not met or were " \
        "exceeded.",
    "B7": "This provider was not certified/eligible to be paid for " \
        "this procedure/service on this date of service. Note: Refer to the " \
        "835 Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment Information REF), if present.",
    "B8": "Alternative services were available, and should have been " \
        "utilized. Note: Refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment Information REF), if present.",
    "B9": "Patient is enrolled in a Hospice.",
    "B10": "Allowed amount has been reduced because a component of the " \
        "basic procedure/test was paid. The beneficiary is not liable for " \
        "more than the charge limit for the basic procedure/test.",
    "B11": "The claim/service has been transferred to the proper " \
        "payer/processor for processing. Claim/service not covered by this " \
        "payer/processor.",
    "B12": "Services not documented in patients' medical records.",
    "B13": "Previously paid. Payment for this claim/service may have " \
        "been provided in a previous payment.",
    "B14": "Only one visit or consultation per physician per day is " \
        "covered.",
    "B15": "This service/procedure requires that a qualifying " \
        "service/procedure be received and covered. The qualifying other " \
        "service/procedure has not been received/adjudicated. Note: Refer " \
        "to the 835 Healthcare Policy Identification Segment (loop 2110 " \
        "Service Payment Information REF), if present.",
    "B16": "'New Patient' qualifications were not met.",
    "B20": "Procedure/service was partially or fully furnished by " \
        "another provider.",
    "B22": "This payment is adjusted based on the diagnosis.",
    "B23": "Procedure billed is not authorized per your Clinical " \
        "Laboratory Improvement Amendment (CLIA) proficiency test.",
    "W1": "Workers' compensation jurisdictional fee schedule " \
        "adjustment. Note: If adjustment is at the Claim Level, the payer " \
        "must send and the provider should refer to the 835 Class of " \
        "Contract Code Identification Segment (Loop 2100 Other Claim " \
        "Related Information REF). If adjustment is at the Line Level, the " \
        "payer must send and the provider should refer to the 835 " \
        "Healthcare Policy Identification Segment (loop 2110 Service " \
        "Payment information REF).",
    "W2": "Payment reduced or denied based on workers' compensation " \
        "jurisdictional regulations or payment policies, use only if no " \
        "other code is applicable. Note: If adjustment is at the Claim " \
        "Level, the payer must send and the provider should refer to the " \
        "835 Insurance Policy Number Segment (Loop 2100 Other Claim Related " \
        "Information REF qualifier 'IG') for the jurisdictional regulation. " \
        "If adjustment is at the Line Level, the payer must send and the " \
        "provider should refer to the 835 Healthcare Policy Identification " \
        "Segment (loop 2110 Service Payment information REF). To be used " \
        "for Workers' Compensation only.",
}


class ClaimAdjustment(X12LoopBridge):

    def __init__(self, aLoop, qualifier):
        self.qualifier = qualifier
        super(ClaimAdjustment, self).__init__(aLoop)
