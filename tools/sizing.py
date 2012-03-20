"""Get Sizing from Legacy Source.

"""
from __future__ import print_function, division
import os, csv, re

sqlPat = re.compile( r'strSQL\s*=\s*"(.*)"' )
def wcSQLComment( path, name ):
    """Gather "word count" statistics on a specific file:
    returns tuple of bytes, words, lines, SQL text, comment line count
    :param path: path
    :param name: file name
    :returns: tuple of bytes, words, lines, SQL text, comment line count
    """
    src= open( os.path.join( path, name ), "rU" )
    data= src.read()
    src.close()
    notes= []
    if "DesignerGenerated" in data:
        notes.append( "DesignerGenerated" )
    comments= 0
    for ln in data.splitlines():
        sqlMatch= sqlPat.search( ln )
        if sqlMatch:
            notes.append( sqlMatch.group(1) )
        if "'" in ln:
            pre, quote, postAll = ln.replace("''","@").partition( "'" )
            post= postAll.strip()
            if len(post) == 0: continue
            if post[0] == '"' or post[-1] == '"': continue
            if all( [ c == post[1] for c in post[2:] ] ): continue
            comments += 1
    return len(data), len(data.split()), len(data.splitlines()), notes, comments

vbClassPat = re.compile( r'^Public Class ([a-zA-Z_][a-zA-Z0-9_]*)$' )
def vbClass( path, name ):
    """Gather all VB class definitions in a specific file:
    returns tuple of comments and class headers
    :param path: path
    :param name: file name
    :returns: tuple of bytes, words, lines, SQL text, comment line count
    """
    src= open( os.path.join( path, name ), "rU" )
    data= src.read()
    src.close()
    notes= []
    count= 0
    for ln in data.splitlines():
        count += 1
        clsMatch= vbClassPat.search( ln )
        if clsMatch:
            notes.append( (count, clsMatch.group(0)) )
    return tuple(notes)

caseStmtPat= re.compile( r"\s*Case\s+([^\s']*)\s*(.*)" )
tableStmtPat= re.compile( r'\s*m_dtSegments.Rows.Add\s*\(\s*(.*)$' )
def segmentMapping( path, name ):
    """Gather all segment mapping definitions.
    returns tuple of segment element definitions.
    :param path: path
    :param name: file name
    """
    src= open( os.path.join( path, name ), "rU" )
    segDefs= []
    className= None
    caseName= None
    count= 0
    for line in src:
        count += 1
        clsMatch= vbClassPat.search( line )
        if clsMatch:
            className= clsMatch.group(1)
            continue
        caseMatch= caseStmtPat.match( line )
        if caseMatch:
            if caseMatch.group(1) == "Else":
                caseName= None
            else:
                caseName= caseMatch.group(1)
            continue
        segTable= tableStmtPat.match( line )
        if segTable:
            args= [ x.strip() for x in segTable.group(1).strip().split(',') ]
            if args[1] == 'cSegment.ID':
                args[1]= caseName
            segDefs.append( className )
            attrName= className+"."+args[3].replace('"','')
            print( "%-22s %5d %-35s %-6s %-4s" % ( name, count, attrName, args[1], args[2], ) )
            continue
    src.close()
    return tuple(segDefs)

def scanDirList( baseDir, apps, wc, destFile ):
    wtr= csv.writer( destFile )
    extSet= set()
    for nm in apps:
        dir= os.path.join( baseDir, nm )
        #print( dir )
        for path, dirList, fileList in os.walk( dir ):
            #print( path )
            subPath= path[len(baseDir)+1:]
            for name in fileList:
                base, ext = os.path.splitext( name )
                if ext in ( ".vb", ".cs" ):
                    wtr.writerow( ( subPath, name, ext, ) + wc( path, name ) )
                else:
                    extSet.add( ext )
    print( extSet )

if __name__ == "__main__":
    baseDir= "Legacy"
    apps= ( "ECL00017", "ECL00018", "ECL00019" )
    with open("segments.csv","wb") as destFile:
        scanDirList( baseDir, apps, segmentMapping, destFile )
