import sys
import time
import asyncio

import pythoncom

import win32com.client

# Solidworks Version (write the year) :
SWV = 2023
# API Version
SWAV = SWV-1992

def PrintFeatureTree(swFeat, indentLevel):
    # Dim swSubFeat As Feature
    # Dim indent As String
    indent = indentLevel * 2 * " "
    
    while swFeat is not None:
        print (f'{indent}Feature Name: {swFeat.Name}, Feature Type: {swFeat.GetTypeName}')
        
        swSubFeat = swFeat.GetFirstSubFeature
        if swSubFeat is not None:
            PrintFeatureTree (swSubFeat, indentLevel + 1)
        
        swFeat = swFeat.GetNextFeature

def main():
    print('testing macro')

    swApp = win32com.client.Dispatch("SldWorks.Application.{}".format(SWAV))
    swModel = swApp.ActiveDoc
    swFeat = swModel.FirstFeature
    
    PrintFeatureTree (swFeat, 0)

if __name__ == "__main__":
    main()

