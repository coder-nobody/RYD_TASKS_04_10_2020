from tabula import convert_into

ndml="https://nad.ndml.in/pdf/AI%20list%2031%20Jul,2020.pdf#page=6&zoom=120,0,0"
eklyan="http://ekalyan.cgg.gov.in/downloads/Outside_State_Colleges_Email_Details.pdf"
ndml2019="https://nad.ndml.in/pdf/AI_list_13_DEC_2019.pdf"
mhrddeemed="https://www.education.gov.in/sites/upload_files/mhrd/files/upload_document/DmdUniv.pdf"
dcmsme="http://www.dcmsme.gov.in/schemes/Institutions_Detail.pdf"
#docshare="http://docshare02.docshare.tips/files/18504/185043513.pdf"
dst="http://dst.gov.in/sites/default/files/ANNEXURE-I%20-List-of-Indian-institutions.pdf"
bangalore_uni="https://bangaloreuniversity.ac.in/wp-content/uploads/2014/11/Bangalore-Urban-Dist-Col-09072016405.pdf"
unipune="http://www.unipune.ac.in/affiliated_colleges_and_institutions/list_website_5-7-12.pdf"
mumbai="https://old.mu.ac.in/wp-content/uploads/2012/01/Updated-All-College-List-with-Course-Detailss.pdf"
ugc="https://www.ugc.ac.in/wro/pdf/College%20list.pdf"



convert_into(ndml,"ndml_college_list.csv",pages="all",output_format="csv")
convert_into(eklyan,"eklyan.csv",pages="all",output_format="csv")
convert_into(ndml2019,"ndml2019.csv",pages="all",output_format="csv")
convert_into(mhrddeemed,"mhrddeemed.csv",pages="all",output_format="csv")
convert_into(dcmsme,"dcmsme.csv",pages="all",output_format="csv")
#convert_into(docshare,"docshare.csv",pages="all",output_format="csv")
convert_into(dst,"dst.csv",pages="all",output_format="csv")
convert_into(bangalore_uni,"bangalore_uni.csv",pages="all",output_format="csv")
convert_into(unipune,"unipune.csv",pages="all",output_format="csv")
convert_into(mumbai,"mumbai.csv",pages="all",output_format="csv")
convert_into(ugc,"ugc.csv",pages="all",output_format="csv")
