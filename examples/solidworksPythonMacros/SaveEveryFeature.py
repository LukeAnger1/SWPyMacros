import pythoncom
import win32com.client

# SolidWorks Version (write the year)
SWV = 2023
# API Version
SWAV = SWV - 1992

def PrintFeatureTree(swFeat, indentLevel, file):
    indent = " " * (indentLevel * 2)
    
    while swFeat is not None:
        file.write(f'{indent}Feature Name: {swFeat.Name}, Feature Type: {swFeat.GetTypeName}\n')
        
        swSubFeat = swFeat.GetFirstSubFeature
        if swSubFeat is not None:
            PrintFeatureTree(swSubFeat, indentLevel + 1, file)
        
        swFeat = swFeat.GetNextFeature

def main():
    print('testing macro')

    # TODO: test the below code to see if it is working
    try:
        # Attempt to get an existing SolidWorks instance
        swApp = win32com.client.DispatchEx("SldWorks.Application")
    except pythoncom.com_error:
        # If there is no existing instance, create a new one
        try:
            swApp = win32com.client.Dispatch("SldWorks.Application.{}".format(SWAV))
            swApp.Visible = True
        except pythoncom.com_error as e:
            print(f"Failed to connect to SolidWorks: {e}")
            return

    swModel = swApp.ActiveDoc
    if swModel is None:
        print("No active document found in SolidWorks.")
        return

    swFeat = swModel.FirstFeature
    
    with open("features.txt", "w") as file:
        PrintFeatureTree(swFeat, 0, file)

if __name__ == "__main__":
    main()
