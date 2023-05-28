"""
Demo message building.
"""
import pytest
from x12.msg_271_4010_X092_A1 import *


def test_build_annotated() -> None:
    m = MSG271(
        isa_loop=[
            ISA_LOOP(
                isa=ISA_LOOP_ISA(
                    isa01="00",
                    isa02="          ",
                    isa03="00",
                    isa04="          ",
                    isa05="ZZ",
                    isa06="ZIRMED         ",
                    isa07="ZZ",
                    isa08="12345          ",
                    isa09="120605",
                    isa10="2324",
                    isa11="U",
                    isa12="00401",
                    isa13="000050033",
                    isa14="1",
                    isa15="P",
                    isa16="^",
                ),
                gs_loop=[
                    GS_LOOP(
                        gs=GS_LOOP_GS(
                            gs01="HB",
                            gs02="ZIRMED",
                            gs03="12345",
                            gs04="20120605",
                            gs05="2324",
                            gs06="50025",
                            gs07="X",
                            gs08="004010X092A1",
                        ),
                        st_loop=[
                            ST_LOOP(
                                st=ST_LOOP_ST(
                                    st01="271", st02="0001"
                                ),
                                header=[
                                    HEADER(
                                        bht=HEADER_BHT(
                                            bht01="0022",
                                            bht02="11",
                                            bht03="11111",
                                            bht04="20120605",
                                            bht05="232423",
                                        )
                                    )
                                ],
                                detail=[
                                    DETAIL(
                                        l2000a=[
                                            L2000A(
                                                hl=L2000A_HL(
                                                    hl01="1",
                                                    hl03="20",
                                                    hl04="0",
                                                ),
                                                l2100a=[
                                                    L2100A(
                                                        nm1=L2100A_NM1(
                                                            nm101="PR",
                                                            nm102="2",
                                                            nm103="Health Net Inc",
                                                            nm104="",
                                                            nm105="",
                                                            nm107="",
                                                            nm108="PI",
                                                            nm109="PI",
                                                        )
                                                    )
                                                ],
                                                l2000b=[
                                                    L2000B(
                                                        hl=L2000B_HL(
                                                            hl01="2",
                                                            hl02="1",
                                                            hl03="21",
                                                            hl04="1",
                                                        ),
                                                        l2100b=[
                                                            L2100B(
                                                                nm1=L2100B_NM1(
                                                                    nm101="1P",
                                                                    nm102="2",
                                                                    nm103="DR. ACULA",
                                                                    nm104="",
                                                                    nm105="",
                                                                    nm107="",
                                                                    nm108="XX",
                                                                    nm109="  ",
                                                                )
                                                            )
                                                        ],
                                                        l2000c=[
                                                            L2000C(
                                                                hl=L2000C_HL(
                                                                    hl01="3",
                                                                    hl02="2",
                                                                    hl03="22",
                                                                    hl04="0",
                                                                ),
                                                                trn=[
                                                                    L2000C_TRN(
                                                                        trn01="1",
                                                                        trn02="222222222",
                                                                        trn03="9ZIRMEDCOM",
                                                                        trn04="ELR ID",
                                                                    ),
                                                                    L2000C_TRN(
                                                                        trn01="2",
                                                                        trn02="333333333",
                                                                        trn03="9ZIRMEDCOM",
                                                                        trn04="ELI ID",
                                                                    ),
                                                                    L2000C_TRN(
                                                                        trn01="1",
                                                                        trn02="4444444444",
                                                                        trn03="9MEDDATACO",
                                                                        trn04=None,
                                                                    ),
                                                                ],
                                                                l2100c=[
                                                                    L2100C(
                                                                        nm1=L2100C_NM1(
                                                                            nm101="IL",
                                                                            nm102="1",
                                                                            nm103="",
                                                                            nm104="",
                                                                            nm105="",
                                                                            nm106="",
                                                                            nm107="",
                                                                            nm108="MI",
                                                                            nm109="R11111111",
                                                                        ),
                                                                        aaa=[
                                                                            L2100C_AAA(
                                                                                aaa01="N",
                                                                                aaa03="72",
                                                                            ),
                                                                            L2100C_AAA(
                                                                                aaa01="N",
                                                                                aaa03="73",
                                                                            ),
                                                                            L2100C_AAA(
                                                                                aaa01="N",
                                                                                aaa03="72",
                                                                            ),
                                                                            L2100C_AAA(
                                                                                aaa01="N",
                                                                                aaa03="58",
                                                                            ),
                                                                        ],
                                                                        dtp=[
                                                                            L2100C_DTP(
                                                                                dtp01="291",
                                                                                dtp02="D8",
                                                                                dtp03="20120408",
                                                                            )
                                                                        ],
                                                                    )
                                                                ],
                                                            )
                                                        ],
                                                    )
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                se=ST_LOOP_SE(
                                    se01="17", se02="0001"
                                ),
                            )
                        ],
                        ge=GS_LOOP_GE(
                            ge01="1", ge02="50025"
                        ),
                    )
                ],
                iea=ISA_LOOP_IEA(
                    iea01="1", iea02="000050033"
                ),
            )
        ]
    )
    # print(m)
    assert m.isa_loop[0].isa.isa12 == "00401"  # Interchange Control Version Number
    assert m.isa_loop[0].gs_loop[0].gs.gs08 == "004010X092A1"  # Version / Release / Industry Identifier Code
    assert m.isa_loop[0].gs_loop[0].gs.gs01 == "HB"  # Functional Identifier Code
    assert m.isa_loop[0].gs_loop[0].st_loop[0].st.st01 == "271"
