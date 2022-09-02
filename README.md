# bad-snakes-icse23-artifacts
The Artifacts for ICSE 2023 submission

This repository contains the source code and data for the ICSE 2023 submission titled "Bad Snakes: Understanding and Improving Python Package Index Malware Scanning"
The main objective is to evaluate the the malware detection tools on three datasets of malicious, popular and random PyPI packages.

You can find in this repository:
- [Package names](package_names/): malicous, popular and random package names and versions
- [Jupyter notebooks](notebooks/): three jupyter notebooks to download packages, run the malware detection tools on the datasets and analyze the results

At the moment, we cannot distribute the raw results nor the packages because there are code with licenses that forbid it (or requires to cite authors, etc.) and possibly ``including" (e.g., in the Metadata) names, email addresses, or other developers’ PII. The malicous packages cannot be distributed without the agreements of the authors. We are working on a solution to anonymize the code, so hopefully we can open-source both the data and code.

Please follow the instructions at the following links to install Python malware detection tools:
- OSSGadget OSS Detect Backdoor: https://github.com/microsoft/OSSGadget/wiki/OSS-Detect-Backdoor
- PyPI Malware Checks: https://github.com/pypi/warehouse/tree/main/warehouse/malware
- Bandit4Mal: https://github.com/lyvd/bandit4mal
