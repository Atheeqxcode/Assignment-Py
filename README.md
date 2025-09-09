# Assignment-Py

#shell script to extract Scheme Name and Asset Value from https://www.amfiindia.com/spages/NAVAll.txt and save as TSV.

# AMFI Scheme Extractor

This script downloads the **NAVAll.txt** file from the [AMFI India website](https://www.amfiindia.com/spages/NAVAll.txt) and extracts only the **Scheme Name** and **Asset Value**, saving them into a tab-separated values (TSV) file called `amfi_data.tsv`.

---

## Shell Script

```bash
#!/bin/bash
# Script to extract Scheme Name and Asset Value from AMFI NAVAll.txt
# Output is stored in amfi_data.tsv

# Download the NAVAll.txt file and extract the required columns
curl -s https://www.amfiindia.com/spages/NAVAll.txt | \
awk -F ';' 'NR>1 {print $4 "\t" $6}' > amfi_data.tsv

echo "Scheme Name and Asset Value saved to amfi_data.tsv"
