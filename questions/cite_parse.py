import json
import re
from questions.fastcase_cite_get import get_citation

def link_grabber(text):
    citation_list = []
    citation_list_0 = re.findall('(\d+)\s*([Ss][Oo]\.\s*(?:\s?\dd)?)\s*(\d+)', text)
    for cite in citation_list_0:
        citation_list.append(cite)
    citation_list_1 = re.findall('(\d+)\s*([Ss]\.\s?[C][t]\.\s*(?:\s?\dd)?)\s*(\d+)', text)
    for cite in citation_list_1:
        citation_list.append(cite)
    citation_list_2 = re.findall('(\d+)\s*([Ss]\.?\s*[Ee]\.?\s*(?:\dd)?\.?)\s*(\d+)', text)
    for cite in citation_list_2:
        citation_list.append(cite)
    citation_list_3 = re.findall('(\d+)\s*([Ss]\.?\s*[Ww]\.?\s*(?:\dd)?\.?)\s*(\d+)', text)
    for cite in citation_list_3:
        citation_list.append(cite)
    citation_list_4 = re.findall('(\d+)\s*([Nn]\.?\s*[Ee]\.?\s*(?:\dd)?)\s*(\d+)', text)
    for cite in citation_list_4:
        citation_list.append(cite)
    citation_list_5 = re.findall('(\d+)\s*([Nn]\.?\s*[Ww]\.?\s*(?:\dd)?)\s*(\d+)', text)
    for cite in citation_list_5:
        citation_list.append(cite)
    citation_list_6 = re.findall('(\d+)\s*([Pp]\.?\s*(?:\s?\dd)?)\s*(\d+)', text)
    for cite in citation_list_6:
        citation_list.append(cite)
    citation_list_7 = re.findall('(\d+)\s*([Aa]\.?\s*(?:\s?\dd)?)\s*(\d+)', text)
    for cite in citation_list_7:
        citation_list.append(cite)
    citation_list_8 = re.findall('(\d+)\s*([Ff]\.?\s*[Ss][Uu][Pp][Pp]\.?)\s*(\d+)', text)
    for cite in citation_list_8:
        citation_list.append(cite)
    citation_list_9 = re.findall('(\d+)\s*([Uu]\.?[Ss])\.?\s*(\d+)', text)
    for cite in citation_list_9:
        citation_list.append(cite)

    for x in citation_list:
            first = x[0]
            middle = x[1]
            last = x[2]

            print("Cite = ",citation_list)
            # get_citation(first, middle, last)
    return get_citation(first, middle, last)
