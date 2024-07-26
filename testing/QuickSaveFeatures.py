import pythoncom
import win32com.client
from my_tree import MyNode, MyTree

# SolidWorks Version (write the year)
SWV = 2023
# API Version
SWAV = SWV - 1992

# Create a tree using the custom MyTree class
tree = MyTree()

##### SET OF EVERYTHING TO COMPLETELY SKIP #####
skip = {}
##### SET OF EVERYTHING TO COMPLETELY SKIP #####

##### SET OF EVERYTHING TO ADD ONE TO COUNT OF THAT NODE THEN SKIP, USING FEATURE TYPE THIS IS DUE TO REPEATS #####
repeat_node_feature_type = {"ReferencePattern"}
##### SET OF EVERYTHING TO ADD ONE TO COUNT OF THAT NODE THEN SKIP, USING FEATURE TYPE THIS IS DUE TO REPEATS #####

def SearchFeatureTree(swFeat, indentLevel):
    indent = " " * (indentLevel * 2)
    
    while swFeat is not None:
        # TODO: Change this to save the information in the tree
        # file.write(f'{indent}Feature Name: {swFeat.Name}, Feature Type: {swFeat.GetTypeName}\n')
        
        # This means it is something that has been counted before so we can add one to that node instead of searching it
        # IMPORTANT TODO: Make sure there are no issues with things like different leaf values
        if swFeat.GetTypeName in repeat_node_feature_type:
            swFeat = swFeat.GetNextFeature
            continue
        
        if swFeat.GetTypeName in skip:
            swFeat = swFeat.GetNextFeature
            continue

        swSubFeat = swFeat.GetFirstSubFeature
        if swSubFeat is not None:
            SearchFeatureTree(swSubFeat, indentLevel + 1)
        
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
        SearchFeatureTree(swFeat, 0, file)

if __name__ == "__main__":
    main()
