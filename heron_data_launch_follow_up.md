# SUBJ: Heron Data launch / follow up

Hi {first_name} – Congratulations on Bank of Small Business's first week with Heron!

As you may have seen on your Heron dashboard (dashboard.herondata.io), Heron processed 1000 end users and 4.9 million transactions in the last week.

I wanted to highlight some important metrics to show how Heron is working:

| Metric Label | Description | Metric Value |
|--------------|-------------|--------------|
| heron_id | # of end users created | 1000 |
| data_volume | # of Transactions Categorized | 4.9M |
| data_freshness | Recency of data | 0 days |
| category_coverage | % of transactions with a category | 100% |

This level of automation and analytics has already translated to approximately 400+ hours saved in your first week alone and is a 10x increase in your team's capacity to review loan applications and underwrite loans!

Also wanted to share a sample of the deep insights about your loan applicants that you now have access to with Heron:

* Median # of debt investments is 0, average is 2.8 —> most applicants do not have existing financing, but a few applicants have many debt investments (potential red flag)
* Median # of revenue sources is 1 —> most applicants have a single business / revenue source
* 25% of applicants had no tax payments in any time period —> applicants may be services businesses or set up as LLC
* 75%+ of applicants had 0 NSF fees during any time period (30-60-90, etc)

## Next Steps

Based on how top customers are using Heron, we've identified a set of best practices/next steps for how you and your teams can get the most value out of Heron:

### 1. Implement additional tools to drive operational improvements

Heron has a number of additional tools / settings to help streamline your underwriting process. For example:
* **Export data to custom excel template** — Configure an export format/schema on your Heron Dashboard that will match your existing underwriting template
* **Email auto-reply to request missing docs** — Set up an automated auto-reply email on your Heron Dashboard that will request missing docs from new applications
* **Daily CRM sync report** — Set up alerts on your Heron Dashboard for notifications of CRM syncing jobs
* **Industry categorization tool** — set up specific restricted industries on your Heron Dashboard, and Heron will automatically assess whether end users match industries
* **End user validation tool** — Validate and confirm end user information and surface any mismatches 

We're happy to help implement any of the above and more! Please contact support@herondata.io to set up time to configure the tools.

### 2. Set policies for auto rejection for end users with red flags or poor metrics

Heron provides rich data and metrics that help you easily identify risky and/or likely unprofitable end users. Our recommendation is to start with one (or more) metrics / data that disqualify an application entirely. For example:

* **# of NSFs (nsf_fees) > 2**: Frequent overdrafters
* **Revenue anomalies (revenue_anomalies) > 2**: Data integrity concerns
* **Debt collection agency amounts (debt_collection) > 1**: Past history of defaulting

Here's how to implement policies within Heron, so that Heron will immediately share a response with the applicant / broker and also prevent the application from even entering your CRM:
[link_to_support_article_policies]

### 3. Set policies for auto-offer for end users that are top applicants with no red flags and excellent metrics

Our recommendation is that you first start with discrete metrics which objectively qualify top candidates. For example:

* **DSCR (debt_service_coverage_ratio) > 1.5**: Strong approval candidate
* **Positive cash flow (net_operating_cashflow) for 90+ days**: Lower risk
* **Zero NSF fees (nsf_fees)**: Good financial management

Also we've recently launched the Heron Score, which is correlated with a number of key metrics including cash flow and various risk metrics that can be a powerful for you to quickly assess applicants. Here's a link to learn more about the Heron Score:

[link_to_support_article_heron_score]

### 4. Evaluate your existing customer base to proactively identify high-quality lending opportunities

Simply run banking records from your existing customer base through Heron to output the same rich categorization and metrics you get from new applicants.

You could first apply the same criteria as in #3 above to identify top 10% existing customers. Then segment customers if they have any existing loan products with you (or others) and use that data to create offers, for example:

* **Existing customer with checking account at BOSB but no loans** —> Use predicted_balance_daily_average metric to create offer for a new loan.
* **Existing customer with a loan from BOSB who may qualify for more financing** —> Analyze debt_service_coverage_ratio metric to create offer for increased loan limit / refinancing
* **Existing customer with one or more loans from other banks who you may be able consolidate at BOSB** —> Use last_debt_investment metric to identify amount of current loans and analyze debt_repayment metric to understand loan terms. Then offer the same or better terms.

## Expected Business Outcomes:
1. **Efficiency**: Reduce underwriting time by 30-40% through prioritization and standardization
2. **Consistency**: More uniform loan decisions based on objective metrics
3. **Scalability**: Process more applications with the same resources
4. **Risk Management**: Better identification of high-risk applications

Thanks again for your trust in Heron. We are excited about helping on your new data-driven journey ahead! We continue to update the platform with new features, please be on the lookout for info our team. 

I will plan to touch base the week after next, but please let us know at support@herondata.io of any questions in the meantime!

Regards,
[/signature]
