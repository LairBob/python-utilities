# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 21:49:22 2016

@author: lstanevich
"""

import re
from urllib.parse import urlparse, urlunparse


#%% Page-cleansing regexprs

regDivStrip = re.compile('^([\s\S]*)(\<div class="inner-html" id="body-content">)([\s\S]*)(\<!-- inner-html -->[\s]*\<\/div\>)([\s\S]*)$')
regAnchBold = re.compile('(\<a .*\>)[\s\S]*\<strong>([\s\S]*)\<\/strong>[\s\S]*(\<\/a[\s]*>)')
regH2Bold = re.compile('(\<h2[\s\S]*\>)[\s\S]*\<strong>([\s\S]*)\<\/strong>[\s\S]*(\<\/h2[\s\S]*>)')


#%% Regular expressions to compile

regNone = re.compile('[\u200b]')
regHyphen = re.compile('[\u2010\u2011\u2012\u2013\u2014\u23af]')
regSmartDblQuote = re.compile('&[lr]dquo;')
regSmartSnglQuote = re.compile('&[lr]squo;')
regRel2Abs = re.compile('(href=\")(\/)')
regPEmpty = re.compile('<p>[\s]*<\/p>')
regPComment = re.compile('(<p>)[\s]*(<!--.*-->)[\s]*(<\/p>)')
regPStrongEmpty = re.compile('<p>[\s]*<strong>[\s]*<\/strong>[\s]*<\/p>')


#%% Path-cleansing regexprs

def hasClass(cssClass):
    return cssClass is not None

def cleanseHTMLSoup(soupInnerHTML):

    soupInnerHTML = soupInnerHTML.find("div", class_="inner-html")

    for eachAnchor in soupInnerHTML.select("a > strong"):
        eachAnchor = eachAnchor.unwrap()

    for eachAnchor in soupInnerHTML.select("strong > a"):
        try:
            eachAnchor.parent.unwrap()
        except:
            print()
            print ("*** ERROR: "+str(eachAnchor.parent.prettify()))


    for eachH2 in soupInnerHTML.select("h2 > strong"):
        eachH2 = eachH2.unwrap()

    for eachH3 in soupInnerHTML.select("h3 > strong"):
        eachH3 = eachH3.unwrap()

    for eachLi in soupInnerHTML.select("li > p"):
        eachLi = eachLi.unwrap()

    for eachSpan in soupInnerHTML.select("span"):
        eachSpan = eachSpan.unwrap()

    # Bulk delete most attributes
    for tag in soupInnerHTML():
        for attribute in ["class", "dir", "width", "height", "valign", "cellpadding", "cellspacing", "border", "align", "style"]:
            del tag[attribute]

    return soupInnerHTML


def cleanseHTMLStr(strSourceHTML):

    strCleansedHTML = strSourceHTML

    strCleansedHTML = regDivStrip.search(strCleansedHTML).group(1)+regDivStrip.search(strCleansedHTML).group(3)+regDivStrip.search(strCleansedHTML).group(5)
    strCleansedHTML = strCleansedHTML.replace('<br/>', '')
    strCleansedHTML = regPEmpty.sub('', strCleansedHTML)
    strCleansedHTML = regPComment.sub('\g<2>', strCleansedHTML)
    strCleansedHTML = regPStrongEmpty.sub('', strCleansedHTML)
    strCleansedHTML = strCleansedHTML.strip()

    return strCleansedHTML


def cleanseHTML(soupInnerHTML):

    soupInnerHTML = cleanseHTMLSoup(soupInnerHTML)

    strInnerHTML = cleanseHTMLStr(soupInnerHTML.prettify())

    return strInnerHTML


#%% Main module

if __name__ == "__main__":
    print("ERROR: Just tried to run 'html_cleanse.py' as main module")