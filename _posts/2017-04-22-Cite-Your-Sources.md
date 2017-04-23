---
layout: post
title:  "Cite Your Sources"
date:   2017-04-23 8:10 -04:00
categories: blogging data-science journalism digging-into-data
excerpt: <p>Digging into a data point that has minimal citation finds it is more three years older than expected and came from a completely different source.</p>
---

Every week -- if not every day -- I come across reports that quote a data point with very little information about the source. Here is a recent one (the data point is also in the press release):
> A recent Forrester Research report called attention to open source’s preeminence in application development, with custom code comprising only 10% to 20% of applications.
> - Black Duck's [_2017 Open Source Security and Risk Analysis_](https://www.blackducksoftware.com/open-source-security-risk-analysis-2017), p. 5. 

The first problem I have with the data point is that there is no citation or link for the source of the data. The second problem I have is that -- and this took far more digging than is warranted -- the 10 to 20 percent number is **not even from Forrester Research**.

Now, this is not about picking on one company. Both in my role as a journalist, and as a data scientist helping companies analyze data to produce internal and public reports, I often run into this problem. I'm hoping by highlighting the issues that companies will be more careful. 

So lets track this one back. And a note on terminology: If the paper gives a full citation, then I will use the verb "cite;" if they give vague information, I will describe that as "sourcing;" and if they give no information, I will label that "unsourced."

### 1. Black Duck's report sourced a Forrester report but with no citation
While the press release used the data point without a source, the report itself referred to "Forrester Research." After a few searches, I found [this March 2017 article](https://www.bsminfo.com/doc/forrester-wave-report-highlights-the-clear-prominence-of-open-source-0001), which mentions the same data point and links to the [_The Forrester Wave™: Software Composition Analysis, Q1 2017_](https://www.forrester.com/report/The+Forrester+Wave+Software+Composition+Analysis+Q1+2017/-/E-RES136463). (Note: The article above essentially rewrites [a press release](http://www.businesswire.com/news/home/20170223006024/en/Open-Source-Security-Provider-Black-Duck-%E2%80%9CLeader%E2%80%9D) from a couple weeks before.)

### 2. Citing a non-public report generally does not help
The Forrester Report lists for $2,495. However, these reports are generally available publicly. Searching for the title and PDF filetype redirected me to [a Black Duck landing page](https://www.blackducksoftware.com/forrester-software-composition-analysis-q1-2017) that hosted the Forrester report. Turns out, Black Duck sponsored the Forrester report that named them a leader in the industry. This is not uncommon for any industry report.

> In their haste to create applications, developers use open source components as their foundation, creating applications using only 10% to 20% new code.
> - [_The Forrester Wave™: Software Composition Analysis, Q1 2017_](https://www.blackducksoftware.com/forrester-software-composition-analysis-q1-2017)

### 3. The Forrester report actually cites Sonatype research
So, here's the rub: The Forrester report is not the source for the data point. The report cites a Sonatype report from 2015 [with a link](http://cdn2.hubspot.net/hubfs/1958393/White_Papers/2015_State_of_the_Software_Supply_Chain_Report-.pdf?t=1466775053631). (Kudos to Forrester Research for the link.)

One problem, however, is that finding the number in the 33-page report is not easy. Searching for "10 to 20 percent" doesn't return anything, even searching through all the "10" entries does not work either. The reason is that the original data point is:
> [I]n the software supply chain, where an average of 106 components comprise 80-90% of the total application, few organizations have visibility into what components were used and where.
> - [2015 State of the Software Supply Chain Report](http://cdn2.hubspot.net/hubfs/1958393/White_Papers/2015_State_of_the_Software_Supply_Chain_Report-.pdf?t=1466775053631), p. 22.

The point is also mentioned on page 5. (It was around this point that I decided this would make a good blog post.) 

The trail did not stop here, of course. Sonatype cited older research in both instances.

### 4. Sonatype report cites ongoing Application Health Check data (circa 2013-2014)
The 33-page Sonatype report cited (in an endnote) its own data: For the citation on page 5, "Sonatype research including Application Health Checks and Open Source surveys, 2013 – 2014," and for the citation on page 22, "Sonatype, 2014 analysis of Application Health Check results."

Unfortunately, none of the Application Health Check results are contained in a standalone report. Some results are quoted in a slide deck, or what appears to be the notes to a slide deck. 

While there is no reason to doubt the veracity of the data, discovering its provenance was certainly a chore. 

Two final points:
- A data point that was supposed to be "recent" **actually came from data from 2013 or 2014**. The data might even be older, as a [2008 CNET News.com piece](https://www.cnet.com/news/forrester-survey-discovers-that-virtually-no-one-uses-open-source/) referred to a Gartner prediction:
> Earlier this year, Gartner's Mark Driver noted the following: By 2012, 80 percent or more of all commercial software will include elements of open-source technology.
> - Source is ComputerWorld UK (broken link), according to [CNET News.com](https://www.cnet.com/news/forrester-survey-discovers-that-virtually-no-one-uses-open-source/)
- Without more information, it is hard to decide what to make of, for example, Black Duck's finding that:
> On average, open source comprised 36% of the code base in these applications. This is a lower percentage than cited by Forrester, a reflection of the mature application codebases that are typically the focus of Black Duck audits.
> - Black Duck's [_2017 Open Source Security and Risk Analysis_](https://www.blackducksoftware.com/open-source-security-risk-analysis-2017), p. 5.

**Next week:** Heard that ransomware caused $209 million in losses in Q1 2016? It didn't.