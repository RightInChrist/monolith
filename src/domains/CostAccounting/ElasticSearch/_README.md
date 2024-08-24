# ElasticSearch
I want to allow people to use ElasticSearch to query data.

# Options Considered
- run ElasticSearch on my computer at my house using my electricity
    - depends on the cost and reliability of my electricity
    - depends on the cost and reliability of my computers
    - depends on the cost and reliability of my internet
- run ElasticSearch on a cloud computer
    - always on
        - costs generally increase as demand and reliability increase
        - with on demand pricing
        - with reserved pricing
    - on demand
        - how long to get it up and running and ready?
            - AWS Lambda (or Google Cloud Function)
                - lambda function to start the thing
                - lambda function to stop the thing
                - pay for duration and requests to lambda function
                    - $0.000017 per GB-second
                    - $0.20 per 1M requests
            - AWS OpenSearch (AWS managed ElasticSearch)
                - https://aws.amazon.com/opensearch-service/pricing/
                - free tier
                    - typically used for testing
                    - 750 hours per month of t2.small.search or t3.small.search
                    - 10 GB per month of optional EBS
                - t3.small.search (2 vCPU and 2 GiB Memory)
                    - $0.036 per hour
                - m7g.2xlarge.search (8 vCPU and 32 GiB Memory)
                    - $0.542 per hour
                - m7g.16xlarge.search (64 vCPU and 256 GiB Memory)
                    - $4.335 per hour
