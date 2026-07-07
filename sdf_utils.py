# opens and reads the SDF file
def load_sdf(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

# ID/Barcode/chemical name mismatch validation
def check_sdf(sdf_contents):

    idNames = []
    barcodeNames = []
    chemNames = []

    for i, line in enumerate(sdf_contents):
        if line.strip() == ">  <ID>":
            idName = sdf_contents[i+1]
            idNames.append(idName)

        if line.strip() == ">  <Barcode>":
            barcodeName = sdf_contents[i+1]
            barcodeNames.append(barcodeName)

        if line.strip() == ">  <Chemical name>":
            chemName = sdf_contents[i+1]
            chemNames.append(chemName)

    for id_val, barcode_val, name_val in zip(idNames, barcodeNames, chemNames):
        if id_val != barcode_val:
            raise Exception(f"ID/Barcode mismatch found: ID '{id_val}' does not match Barcode '{barcode_val}' for chemical '{name_val}'.  Please correct before proceeding.")

# finds and validates project name
def extract_project_name(sdf_contents):
    projectNames = []

    for i, line in enumerate(sdf_contents):
        if line.strip() == ">  <Project name>":
            # projectName = line[i+1]
            projectName = sdf_contents[i+1]
            projectNames.append(projectName)
            # print(projectName)

    # print(projectNames)

    if len(set(projectNames)) == 1:
        projectName = projectNames[0]
        print(f"Project name found: {projectName}")
        return projectName
    else:
        raise Exception(f"Mixed project names found in SDF file: {set(projectNames)}")