# JotForm - Preprocessing & Language Detection & PII Detection pipeline
 
## Implementation
I used Python 3.9 as the implementation language. In terms of frameworks I have used NumPy, pandas, spaCy, and Presidio.

## Running
This is not runnable as the API key for pulling the forms is not provided.

## Details
This project is for the JotForm regarding their concern on the exposure of "Personally Identifiable Information" (PII). This pipeline detects many of the PII categories according to GDPR. The resulting PII containing forms are transmitted to manual reviewers so that they can feed the system by annotating whether the PII detection is correct. I have also implemented the application for the manual reviewers and it is in the link below.
[JotForm - PII Detection Manual Review System](https://github.com/obince/pii_detection_site)
