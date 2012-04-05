#!/usr/bin/env python
# EXAMPLE IMPLEMENTATION - 278 Request Parser
from tigershark.X12.parse import Message
from tigershark.X12.parse import Loop
from tigershark.X12.parse import Segment
from tigershark.X12.parse import Composite
from tigershark.X12.parse import Element
from tigershark.X12.parse import Properties

loop2000A= Loop( "2000A", Properties( desc="2000A", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"20"), desc="Utilization Management Organization (UMO) Level", req_sit="R", repeat="1"),
        Element( "HL03", Properties(position=3,codes=["20"]) )
        ),
    Loop( "2010A", Properties( desc="2010A", req_sit="R", repeat=">1", ),
        Segment("NM1", Properties( qual=(1,"X3"), desc="Utilization Management Organization (UMO) Name", req_sit="R", repeat="1"),
            Element( "NM101", Properties(position=1,codes=["X3"]) ) ),
        ),
    )

loop2000B= Loop( "2000B", Properties( desc="2000B", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"21"), desc="Requester Level", req_sit="R", repeat="1"),
        Element( "HL03", Properties( position=3, codes=["21"]) )
        ),
    Loop( "2010B", Properties( desc="2010B", req_sit="R", repeat=">1", ),
        Segment("NM1", Properties( qual=(1,("1P","FA")), desc="Requester Name", req_sit="R", repeat="1"),
            Element( "NM101", Properties(position=1,codes=["1P", "FA"]) )
            ),
        Segment("REF", Properties( desc="Requester Supplemental Identification", req_sit="S", repeat="8") ),
        Segment("N3", Properties( desc="Requester Address", req_sit="S", repeat="1") ),
        Segment("N4", Properties( desc="Requester City/State/ZIP Code", req_sit="S", repeat="1")),
        Segment("PER", Properties( desc="Requester Contact Information", req_sit="S", repeat="1")),
        Segment("PRV", Properties( desc="Requester Provider Information", req_sit="S", repeat="1")),
        ),
    )

loop2000C= Loop( "2000C", Properties( desc="2000C", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"22"), desc="Subscriber Level", req_sit="R", repeat="1"),
        Element( "HL03", Properties( position=3, codes=["22"]) )
        ),
    Segment("DTP", Properties( desc="Accident Date", req_sit="S", repeat='1') ),
    Segment("DTP", Properties( desc="Last Menstrual Period Date", req_sit="S", repeat='1') ),
    Segment("DTP", Properties( desc="Estimated Date of Birth", req_sit="S", repeat='1') ),
    Segment("DTP", Properties( desc="Onset of Current Symptoms or Illness Date", req_sit="S", repeat='1') ),
    Segment("HI", Properties( desc="Subscriber Diagnosis", req_sit="S", repeat='1') ),
    Loop( "2010C", Properties( desc="2010C", req_sit="R", repeat=">1", ),
        Segment("NM1", Properties( qual=(1,"IL"), desc="Subscriber Name", req_sit="R", repeat='1'),
            Element( "NM101", Properties( position=1, codes=["IL"]) ),
            ),
        Segment("REF", Properties( desc="Subscriber Supplemental Identification", req_sit="S", repeat=9) ),
        Segment("DMG", Properties( desc="Subscriber Demographic Information", req_sit="S", repeat='1') ),
        ),
    )

loop2000D= Loop( "2000D", Properties( desc="2000D", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"23"), desc="Dependent Level", req_sit="S", repeat='1'),
        Element( "HL03", Properties( position=3, codes=["23"]) )
        ),
    Segment("DTP", Properties( desc="Accident Date", req_sit="S", repeat='1') ),
    Segment("DTP",Properties( desc="Last Menstrual Period Date", req_sit="S", repeat='1') ),
    Segment("DTP",Properties( desc="Estimated Date of Birth", req_sit="S", repeat='1') ),
    Segment("DTP",Properties( desc="Onset of Current Symptoms or Illness Date", req_sit="S", repeat='1') ),
    Segment("HI",Properties( desc="Dependent Diagnosis", req_sit="S", repeat='1') ),
    Loop( "2010D", Properties( desc="2010D", req_sit="R", repeat=">1", ),
        Segment("NM1", Properties( qual=(1,"QD"), desc="Dependent Name", req_sit="R", repeat='1'),
            Element( "NM101", Properties( position=1, codes=["QD"]) )
            ),
        Segment("REF",Properties( desc="Dependent Supplemental Identification",req_sit="S",repeat='3') ),
        Segment("DMG",Properties( desc="Dependent Demographic Information",req_sit="S",repeat='1') ),
        Segment("INS",Properties( desc="Dependent Relationship",req_sit="S",repeat='1') ),
        ),
    )

loop2000E= Loop( "2000E", Properties( desc="2000E", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"19"), desc="Service Provider Level", req_sit="R", repeat='1'),
        Element( "HL03", Properties( position=3, codes=["19"]) )
        ),
    Segment("MSG", Properties( desc="Message Text", req_sit="S", repeat='1') ),
    Loop( "2010E", Properties( desc="2010E", req_sit="R", repeat=">1", ),
        Segment("NM1", Properties( qual=(1,("1T","FA","SJ")),desc="Service Provider Name",req_sit="R",repeat='1'),
            Element( "NM101", Properties( position=1, codes=["1T","FA","SJ"]))
            ),
        Segment("REF", Properties( desc="Service Provider Supplemental Identification", req_sit="S", repeat=7) ),
        Segment("N3", Properties( desc="Service Provider Address", req_sit="S", repeat='1') ),
        Segment("N4", Properties( desc="Service Provider City/State/ZIP Code", req_sit="S", repeat='1')),
        Segment("PER", Properties( desc="Service Provider Contact Information", req_sit="S", repeat='1')),
        Segment("PRV", Properties( desc="Service Provider Information", req_sit="S", repeat='1')),
        ),
    )

loop2000F= Loop( "2000F", Properties( desc="2000F", req_sit="R", repeat="1", ),
    Segment("HL", Properties( qual=(3,"SS"), desc="Service Level", req_sit="R", repeat='1'),
        Element( "HL03", Properties( position=3, codes=["SS"]) )
        ),
    Segment("TRN", Properties( desc="Service Trace Number",req_sit="S",repeat='2') ),
    Segment("UM", Properties( desc="Health Care Services Review Information",req_sit="R",repeat='1') ),
    Segment("REF", Properties( desc="Previous Certification Identification",req_sit="S",repeat='1') ),
    Segment("DTP", Properties( desc="Service Date",req_sit="S",repeat='1') ),
    Segment("DTP", Properties( desc="Admission Date",req_sit="S",repeat='1') ),
    Segment("DTP", Properties( desc="Discharge Date",req_sit="S",repeat='1') ),
    Segment("DTP", Properties( desc="Surgery Date",req_sit="S",repeat='1') ),
    Segment("HI", Properties( desc="Procedures",req_sit="S",repeat='1') ),
    Segment("HSD", Properties( desc="Health Care Services Delivery",req_sit="S",repeat='1') ),
    Segment("CRC", Properties( desc="Patient Condition Information",req_sit="S",repeat='1') ),
    Segment("CL1", Properties( desc="Institutional Claim Code",req_sit="S",repeat='1') ),
    Segment("CR1", Properties( desc="Ambulance Transport Information",req_sit="S",repeat='1') ),
    Segment("CR2", Properties( desc="Spinal Manipulation Service Information",req_sit="S",repeat='1') ),
    Segment("CR5", Properties( desc="Home Oxygen Therapy Information",req_sit="S",repeat='1') ),
    Segment("CR6", Properties( desc="Home Health Care Information",req_sit="S",repeat='1') ),
    Segment("MSG", Properties( desc="Message Text",req_sit="S",repeat='1') ),
    )

parse_278 = Message(
    "278", Properties(desc="HIPAA Health Care Services Review: Request X094A1-278",),
    Loop( "ISA", Properties(desc="ISA", req_sit="R", repeat="1",),
        Segment("ISA", Properties() ),
        Loop( "GS", Properties(desc="GS", req_sit="R", repeat="1",),
            Segment("GS", Properties() ),
            Loop( "ST", Properties(desc="ST", req_sit="R", repeat="1",),
                Segment("ST", Properties( qual=(1,"278"), desc="Transaction Set Header", req_sit="R", repeat='1'),
                    Element( "ST01", Properties(position=1,codes=["278"]))
                ),
                Segment("BHT", Properties( desc="Beginning of Hierarchical Transaction", req_sit="R", repeat='1') ),
                loop2000A, loop2000B, loop2000C, loop2000D, loop2000E, loop2000F,
            ),
            Loop( "SE", Properties(desc="SE", req_sit="R", repeat="1",),
                Segment("SE", Properties() )
            ),
        ),
        Loop( "GE", Properties(desc="GE",req_sit="R",repeat="1",),
            Segment("GE", Properties() )
        ),
    ),
    Loop( "IEA", Properties(desc="IEA", req_sit="R", repeat="1"),
        Segment("IEA", Properties() ),
    ),
)
