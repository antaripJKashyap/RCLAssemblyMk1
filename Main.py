from docx import Document

class Address:
    def __init__(self, line1, line2, postalcode):
        self.line1 = line1
        self.line2 = line2
        self.postalcode = postalcode
        print("Address Created")

    def produceAddress(self, inputString):
        #split string into line1, line2, and postalcode
        self.line1 = inputString

class Skill:
    def __init__(self, skillTitle, skillBody):
        self.skillTitle = skillTitle
        self.skillBody = skillBody

class Date:
    def __init__(self, dateAsNum):
        self.dateAsNum = dateAsNum
        self.createDate()
    def createDate(self):
        print("Date fn accessible")


# Load the master document with all phrases
doc = Document("AA Cover Letter BASE.docx")

# Extract all paragraphs
paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]

#checking the data
# for parsed in paragraphs :
#         print("Current value: ", parsed, "\n")

#sampleDate = Date(123456)
companyName = paragraphs[1]
addressContainer = paragraphs[2], paragraphs[3], paragraphs[4]
#print(addressContainer)

skillsContainer = []
index = 0
for parsed in paragraphs :
    if (parsed[0] == "<") :
        # print("working on:", paragraphs[index], paragraphs[index + 1])
        skillsContainer.append(Skill(paragraphs[index], paragraphs[index + 1]))
    index += 1

residualContainer = []
# for currIndex in (index, len(paragraphs) - 1) :
#     residualContainer.append(paragraphs[currIndex])
#
# print(residualContainer)

# for skill in skillsContainer :
#     print(skill.skillBody)

#print(skillsContainer)
# var1 = paragraphs[24]
# var = type(paragraphs[2])
# print(var1)
# print(var)

