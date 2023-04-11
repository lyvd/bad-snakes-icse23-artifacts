# bad-snakes-icse23-artifacts

# Authors
Duc-Ly Vu, Zack Newman, John Speed Meyers


The Artifacts for ICSE 2023 submission

This repository contains the source code and data for the ICSE 2023 submission titled "Bad Snakes: Understanding and Improving Python Package Index Malware Scanning".
The main objective is to evaluate the malware detection tools on three datasets of malicious, popular and random PyPI packages.

You can find in this repository:
- [Package names](package_names/): malicous, popular and random package names and versions
- [Jupyter notebooks](notebooks/): there are Jupyter notebooks that we use to download PyPI packages, run the malware detection tools on the datasets, and analyze the results
- [src](src/): there is a couple of scripts to run the malware detection tools if you do not want to use the Jupiter notebooks.

At the moment, we cannot distribute the raw results nor the packages because there are code with licenses that forbid it (or requires to cite authors, etc.) and possibly `include (e.g., in the Metadata) names, email addresses, or other developers’ PII. The malicous packages cannot be distributed without the agreements of the authors. We are working on a solution to anonymize the code, so hopefully we can open-source both the data and code.

Please follow the instructions at the following links to install these Python malware detection tools:
- OSSGadget OSS Detect Backdoor: https://github.com/microsoft/OSSGadget/wiki/OSS-Detect-Backdoor
- PyPI Malware Checks: https://github.com/pypi/warehouse/tree/main/warehouse/malware
- Bandit4Mal: https://github.com/lyvd/bandit4mal

You can cite the Artifact by the following Bibtex

@software{ly_vu_duc_2023_7578941,
  author       = {Ly Vu Duc and
                  Zack Newman and
                  John Speed Meyers},
  title        = {{Bad Snakes: Understanding and Improving Python 
                   Package Index Malware Scanning}},
  month        = jan,
  year         = 2023,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.7578941},
  url          = {https://doi.org/10.5281/zenodo.7578941}
}

Please consier citing out paper

@inproceedings{vu2023bad,
  title={Bad Snakes: Understanding and Improving Python Package Index Malware Scanning},
  author={Vu, Duc-Ly and Newman, Zack  and Meyers, John Speed},
  booktitle={Proceedings of the ACM/IEEE 45th International Conference on Software Engineering: Companion Proceedings},
  year={2023}
}

License
Apache License Version 2.0
