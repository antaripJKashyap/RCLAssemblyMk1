from docx import Document

class Address:
    def __init__(self, line1, line2, postalcode):
        self.line1 = line1
        self.line2 = line2
        self.postalcode = postalcode
        print("Address Created") ##TODO

    def produceAddress(self, inputString):
        #split string into line1, line2, and postalcode
        self.line1 = inputString ##TODO

class Skill:
    def __init__(self, skillTitle, skillBody):
        self.skillTitle = skillTitle
        self.body = skillBody
        print("Skil Created") ##TODOtst

class Date:
    def __init__(self, dateAsNum):
        self.dateAsNum = dateAsNum
        self.createDate()
    def createDate(self):
        print("Date fn accessible") ##TODO


# Load the master document with all phrases
doc = Document("AA Cover Letter BASE.docx")

# Extract all paragraphs
paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]

#sampleDate = Date(123456)


# var1 = paragraphs[24]
# var = type(paragraphs[2])
# print(var1)
# print(var)

