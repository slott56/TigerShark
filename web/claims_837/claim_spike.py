"""
A function which applies the :mod:`claims` module
to the :mod:`web.claims_837` structure.
This allows a developer to implement the user's view of a :mod:`Claim`
as navigation through the X12 message parsed by :func:`web.claims_837.parse_837i`.
"""
from __future__ import print_function
from claims import Claim
from parse import parse_837i


if __name__ == "__main__":
    with open( "../test/837I-Patient-NotSubscriber.txt", "rU" ) as claim:
        src= claim.read()
    msg= parse_837i.unmarshall( src )
    c= Claim(msg)
    print( c.patient[0].loop )
    print( c.patient[0] )
    print( c.patient[0].addr1, c.patient[0].addr2, c.patient[0].city, c.patient[0].state, c.patient[0].zip )
    print( 'DOB:', c.patient[0].dob, 'SEX:', c.patient[0].sex, 'SSN:', c.patient[0].ssn, 'REL:', c.patient[0].rel )
    print( c.provider[0], c.provider[0].phone )
    print( c.submitter[0].loop )
    print( c.submitter[0].last, c.submitter[0].first, c.submitter[0].phone )
    print( "Notes:", c.claimDetails[0].billNote, c.claimDetails[0].claimNotes )
    print( "prin diag code:", c.claimDetails[0].prinDiagCode )
    print( "admit     code:", c.claimDetails[0].admitDiagCd )
    print( "Cond Codes:", c.claimDetails[0].condCode )
    print( "Occr Codes:", c.claimDetails[0].occrCode )
    print( "Paperwork: ", c.claimDetails[0].paperwork )
