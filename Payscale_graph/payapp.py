
import tabula
import pprint

df = tabula.read_pdf("9693_Apr2018.pdf")
# in order to print first 5 lines of Table
print(df)

js = tabula.read_pdf("9693_Apr2018.pdf", output_format="json")
pprint.pprint(js)

xl = tabula.convert_into("9693_Apr2018.pdf", "9693_Apr 2018.xlsx", output_format="xlsx")
pprint.pprint(js)