from facade import X12LoopBridge
#from facade import X12SegmentBridge
from facade import ElementAccess
#from facade import SegmentSequenceAccess
#from facade import SegmentConversion
#from facade import SequenceOf
#from facade import ElementSequenceAccess
#from facade import CompositeAccess
#from facade import CompositeSequenceAccess
#from facade import D8


class m835(object):
    class _Payer(X12LoopBridge):
        """Submitter Data derived from the 1000A loop."""
        loopName = "1000A"
        name = ElementAccess("N1", 2)
        qualifier = ElementAccess("NM1", 3)
        id = ElementAccess("NM1", 4)
        addr1 = ElementAccess("N3", 1)
        addr2 = ElementAccess("N3", 2)
        city = ElementAccess("N4", 1)
        state = ElementAccess("N4", 2)
        zip = ElementAccess("N4", 3)
        payer_id = ElementAccess("REF", 2, qualifier=(1, "2U"))
        submitter_id = ElementAccess("REF", 2, qualifier=(1, "EO"))
        # health industry number
        hin = ElementAccess("REF", 2, qualifier=(1, "HI"))
        naic_code = ElementAccess("REF", 2, qualifier=(1, "NF"))
        email = ElementAccess("PER", oneOf=("EM", (3, 4), (5, 6), (7, 8)))
        fax = ElementAccess("PER", oneOf=("FX", (3, 4), (5, 6), (7, 8)))
        phone = ElementAccess("PER", oneOf=("TE", (3, 4), (5, 6), (7, 8)))

        def __str__(self):
            return "%s, %s %s %s" % (self.last, self.first, self.mid,
                    self.suffix)

    def loops(self, theClass, anX12Message):
        return [theClass(loop) for loop in
                anX12Message.descendant("loop", theClass.loopName)]

    def __init__(self, anX12Message):
        """Examine the message and extract the relevant Loops."""
        self.payer = self.loops(self._Payer, anX12Message)
