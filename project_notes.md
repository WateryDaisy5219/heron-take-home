# Heron Take-Home Notes

## TAKE HOME LINK
https://herondata.notion.site/Heron-Product-Ops-Take-Home-12726b031c628037b665e744f7a1eae8

---

## STEPS
- [x] Review the problem
- [x] Review the data sets
- [x] Research lending market/specific operational items for credit analysts. And lending options for small businesses and local businesses.
- [x] Craft messaging + metrics to support
- [x] Document notes and process 

---

## Core Questions
**Is Heron working as expected?**
—i.e. automating 1+2

**How can we use Heron output to improve our underwriting process? Which companies should we focus on underwriting?**
—I.e. extending the analyses to 3+4

## Questions:
- [ ] How to interpret / display output of results? In a report form? Or an email / presentation form? What info to include? How to frame the results
- [ ] How to quantify results / important metrics
- [ ] Also, how to present it in a punchy way with the most important information first
- [ ] What matters most to a lender

For #1 + #2. Extract pertinent pieces of information from those documents,
—Is it accuracy? How is that measured?
—is it speed to close transactions? How is that measured?
—is it overhead of # of hours to do the work?
—is it having the data in a structured format?
—how long did it take to run the script?
—the underwriter will basically be able to do 10x…
—all in a structured format (metric, range, value)

For heron to be working
—most documents should be processed w/o errors
—most documents should have high rate of accuracy

---

## Is Heron working as expected?

- [x] Look at data quality and processing quality metrics…
- [x] Also look at the total volume processed.
- [ ] Processing quality // Merchant coverage — LOW…
- [ ] Determining intra-company transactions..?? Not sure how this factors in to is it working as expected….

## How can we use Heron output to improve our underwriting process? Which companies should we focus on underwriting?

- [ ] analyze the data with pandas — what is the data, what are the data points for a single company… 
- [ ] try to output for a single company in csv..
- [ ] Come up with some scoring / segmentation of data.. LOOK AT THE ANALYSIS DONE IN VIDEOS..
- [ ] Describe a methodology to use data on prior loan applications to inform a perspective??
- [x] Understand loan processing and what metrics do they look at??? — DONE… reviewed Claude output
- [x] Review metrics to analyze the source / output… where is it coming from? Is it real or calculated? Is it used by lenders currently? --DONE.. added notes for each metric

---

## GOALS
- [ ] Demonstrate value + performance of Heron with specific metrics and insights
- [ ] Frame messaging to meet customer's emotional / other needs
- [ ] Present info in a clear, concise, compelling way for customers
- [ ] Quantify financial impact (subsequent to metrics)
- [ ] Suggest next steps for further value and usage
- [ ] Provide resources (dashboard?)
- [ ] Help diagnose any issues (e.g. low quality etc)

## Subgoals 
- [ ] Demonstrate thinking process / sequencing
- [ ] Demonstrate understanding of the business
- [ ] Offer something new / of value that might go into actual deployment as a template
- [ ] Demonstrate skills / knowledge across data, writing, customer interactions

---

## OUTPUT // note / presentation to lender customer

Hi {first_name} – Happy Monday! 

Instead of spending your Monday extracting data, you're immediately diving into what matters: making the right lending decisions.

Congratulations on a new beginning! With Heron, you've saved 83 hours of manual work and counting!

I've set up a custom dashboard for you

In addition to simply extracting and categorizing transactions, we've gone a step further to give you deep analytics about the cash flow profile, potential risk factors.

Also, we are extremely excited to announce the Heron Score, which is a 

Based on your first week with Heron, we've identified that XX% of your applications fall in the top 10% of Heron scores…

Hear how our top customers are using the Heron Score to auto-approve (within seconds) the top 10% of applicants, plus auto-reject the bottom 10% of applicants:


I'd love to set up a follow up where we could discuss your approval flow and how we could help you build automation. What's your availability this week or next?

---

These results help and multiple ways:

Our top customers are taking it one step further:

There are a few links to customer testimonials.

I'd be happy to share with you additional ideas for how you could set up the conditional logic in your system.

---

Congratulations on your first week with Heron!

Here's how you know you're having success with Heron:

* 100% Application Coverage: All 1,000 applications were successfully processed without manual intervention
* 89% Category Coverage: Nearly 9 out of 10 transactions were automatically categorized correctly
* 94% Merchant Identification: Strong recognition of merchants across all bank statements
* 78 Hidden MCAs Identified: Heron automatically detected 78 Merchant Cash Advances that would have required hours of manual review to uncover

This level of automation has already translated to approximately 83 hours saved in your first week alone, representing roughly $8,300 in cost reduction based on standard underwriter hourly rates.

---

Here's our recommendation for how you can leverage the structure data and insights from Heron to improve your underwriting process:

Metrics specific to your process:

---

## OUTPUT // specific metrics and analysis

Data quality and processing quality metrics are most helpful for explaining how Heron is working as expected.

- [ ] 100% category coverage for all applications — ALL transactions are categorized automatically
- [ ] 1000 loan applications ingested 1 week — the avg capacity of 1 person is 50-100 — 10-20x increase in ingestion capacity
- [ ] Over 1.1M transactions processed 100% automatically (w/ 100% categorization) (using the # of outflows + inflows for last 365 days) // 775k outflows + 330k inflows
- [ ] Over 4.9M transactions processed 100% automatically (w/ 100% categorization) — Data Volume metric
- [ ] $415M of inflows processed

—the important points to highlight are the scale at millions of transactions and 1000 loan applications processed. 

Back of the envelope is at least 10x greater than what a single credit analyst could produce in a similar time.

Instead of 12-20 loan applications per day, should be able to do 10x that amount

In addition to the speed and accuracy in extracting transactions from loan application docs (at scale), Heron has also categorized transactions, for example, intracompany transactions, NSF fees, tax payments.

Plus Heron has generated metrics relevant for the remainder of underwriting process

Also heron has the info in a highly structured output.

This also allows you to create a more competitive and aggressive offer for the good companies with high cash flow. Because of the trust that lower companies will not screw up your portfolio.

—provide an instantaneous rate / decision??

---

## VIDEO / CALL NOTES
Jamie

$10k-100k loans…

130 lenders that are customers… small business credit..

SMALL BUSINESS — USUALLY FOUNDER ASSETS..

High conviction w/ competitive offer..

Credit analyst spends 25 min per file… revenue, etc metrics…

---

Byron
—30 ppl in the Philippines doing this..

---

## Questions
- [ ] What about inaccuracies? Why is the confidence score so low? What does the confidence score mean?
- [ ] Who are they lending to? Why is daily revenue important? why do brokers send out application packages?? — SMB local business…
- [ ] What P&L / accounting software used? Could we move upstream to integrate directly the applicants?
- [ ] What is an analytics group?
- [ ] Who are competitors? Proprietary bank models? FICO? Ocrolus?
- [ ] Is there a salesforce managed package for Heron data?
- [ ] New industry growth? e.g. deal making, accounting, etc?
- [ ] Can we clean up the API documentation?
- [ ] WHAT IS THE PRICING MODEL??Custom pricing?? Based on loan volume?? OR flat fee??
- [ ] is there upsell for automating more of it? Or same price whether using the full suite?

---

## VIDEO LINKS
- [ ] https://www.youtube.com/watch?v=IlC5JKkAH48
- [ ] https://www.youtube.com/watch?v=ydsA62vzEcg
