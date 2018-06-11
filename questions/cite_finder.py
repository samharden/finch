#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re

def cite_finder(text):

    citation_list = []
    citation_list_0 = re.findall('(\d+)\s*([Ss][Oo]\.\s*(?:\s?\dd)?)\s*(\d+)', text)
    for cite in citation_list_0:
        print(type(cite))
        new_text = text.replace(str(cite), '<a href="">'+str(cite)+'</a>')

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


    print(new_text)

    return text


if __name__ == '__main__':

    sample_text = """
    Whether consent is voluntary is a question of fact to be determined
    from the totality of the circumstances. McDonnell v. State, 981 So.2d 585
    (Fla. 1st DCA 2008). The relevant factors include the age of the defendant,
    whether the defendant had a prior criminal history – the presumption being
    that one who has prior criminal arrests knows his legal rights – and whether
    there was evidence that the defendant was intoxicated or suffering from a
    mental deficiency that impaired his ability to make an intelligent decision.
    Wilson v. State, 952 So. 2d 564, 570 (Fla. 5th DCA 2007).

    IN THE CIRCUIT COURT OF THE SIXTH JUDICIAL CIRCUIT
    OF THE STATE OF FLORIDA, IN AND FOR PINELLAS COUNTY
    CIVIL DIVISION

    THE ESTATE OF HELENE JOY
    VAN DAMME by and through
    LYNETTE GORANSON,
    Personal Representative,

    Plaintiff,
    Case no.: 06-316-CI-21
    vs.

    WESTCHESTER GARDENS LIMITED
    PARTNERSHIP d/b/a WESTCHESTER
    GARDENS REHABILITATION AND
    CARE CENTER; AND JBGE/WESTCHESTER,
    INC., its General Partner,

    Defendants.
    _______________________________________________/

    DEFENDANT’S MOTION IN LIMINE TO ENFORCE
    COLLATERAL SOURCE SET-OFF

    COMES NOW the Defendant, WESTCHESTER GARDENS LIMITED PARTNERSHIP d/b/a WESTCHESTER GARDENS REHABILITATION and JBGE/WESTCHESTER, INC., its General Partner, (hereinafter “Defendant” or “Westchester Gardens”), by and through the undersigned counsel, and hereby moves this Court to grant this Motion in Limine to Enforce Collateral Source Set-Off, and in support thereof states as follows:
    INTRODUCTION
    This case arises from Helene Joy Van Damme’s residency at Westchester Gardens.  Ms. Van Damme’s residency began on December 2, 2003, and lasted until December 31, 2003.  On or about March 9, 2010, Plaintiff filed the Amended Complaint, including three counts: Count I – Non-Lethal Negligence; Count II – Lethal Negligence; and Count III – Wrongful Death.  The three counts turn to the Residents Rights provisions in Florida Statutes 400.022 and 400.023, to define the alleged duty Defendants owed to the Resident, Helene Joy Van Damme.
    LEGAL ARGUMENT
    1.	Helene Joy Van Damme was covered by Blue Cross and Blue Shield Insurance and Medicare during her admission to Westchester Gardens.
    2.	In anticipation of a claim for past medical expenses, any recovery must be limited to only those expenses actually paid by Blue Cross and Blue Shield Insurance and Medicare.
    3.	When presented with a plaintiff’s past medical expenses, a defendant is entitled to a setoff for the amount of the medical bills that medical providers discount in accordance with their contractual agreements with health maintenance organizations.  See Goble v. Frohman, 848 So. 2d 406, 410 (Fla. 2d DCA 1999), rev. granted, 865 So. 2d 480 (Fla. 2004).
    4.	Furthermore, with regard to Medicare setoffs, the Second District held that “the appropriate measure of compensatory damages for past medical expenses when a plaintiff has received Medicare benefits does not include the difference between the amount that the Medicare providers agreed to accept and the total amount of the plaintiff’s medical bills.” Cooperative Leasing, Inc. v. Johnson, 872 So. 2d 956, 960 (Fla. 2d DCA 2004), rev. granted, 884 So. 2d 22 (Fla. 2004). See also Thyssenkrupp Elevator Corporation v. Lasky, 868 So. 2d 547 (Fla. 4th DCA 2003) (holding that a defendant is entitled to a setoff for contractual discounts given by Medicare providers when the entire amount of the medical expenses covered by Medicare was introduced and awarded by the jury).
    5.	Defendants’ second affirmative defense states that Defendants are entitled to a set-off for any and all collateral sources or monies paid to or for the benefit of the Plaintiff.
    6.	Accordingly, Plaintiff’s claim for medical expenses should be limited to only that amount Blue Cross and Blue Shield Insurance and Medicare actually paid to medical providers on behalf of Helene Joy Van Damme as a result of Defendants’ alleged negligence.

    WHEREFORE, Defendant respectfully requests that this Court enter an order granting Defendant’s Motion in Limine to Enforce Collateral Source Set-Off, requiring Plaintiff’s claim for past medical expenses to include only amounts actually paid by Blue Cross and Blue Shield Insurance and Medicare and any such other relief as this Court deems just and appropriate.


    """

    link_grabber(sample_text)
