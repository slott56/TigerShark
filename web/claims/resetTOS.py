#!/usr/bin/env python
"""Reset the Type of Service.
"""
from __future__ import print_function
from web.claims.models import Benefit, TypeOfService
import csv

def resetTOS( source= "sql/typeofservice.csv" ):
    print( "resetTOS.py", source )

    # Remove old Type Of Service definitions
    print( "Removing", TypeOfService.objects.count() )
    TypeOfService.objects.all().delete()

    # Open CSV file and load TOS's
    with open( source, "rb" ) as tosFile:
        tosRdr= csv.DictReader( tosFile )
        count= 0
        error= 0
        for row in tosRdr:
            try:
                benefit= Benefit.objects.get( benefit=row['benefit'] )
                tos= benefit.typeofservice_set.create(
                    typeOfService=row['typeofservice'],
                    description=row['description'])
                tos.save()
                count += 1
            except Benefit.DoesNotExist, e:
                print( "?", row['benefit'] )
                error += 1
            except Benefit.MultipleObjectsReturned, e:
                print( "*", row['benefit'] )
                error += 1

    # Final Counts
    print( "Loaded", count )
    if error > 0:
        print( "Errors on ", error )

    print( "There are now", TypeOfService.objects.count() )

if __name__ == "__main__":
    resetTOS()
