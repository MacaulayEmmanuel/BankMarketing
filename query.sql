
-- Which professions are the most popular among customers over 45 years old?
SELECT job,
       COUNT(*) as num_customers
FROM bank
WHERE age > 45
GROUP BY job
ORDER BY num_customers DESC;


-- For how many people with loans did the marketing campaign succeed?
SELECT COUNT(*) as num_successful_loans
FROM bank
WHERE loan = 'yes' AND poutcome = "success" ;


-- Does the success depend on the balance, deposit, or loan?
SELECT COUNT(*) as num_successful_loans,
       AVG(balance) AS avg_balance, 
       deposit, loan, 
       poutcome AS marketing_campaign_outcome
FROM bank
GROUP BY marketing_campaign_outcome;

-- the success depends on the balance