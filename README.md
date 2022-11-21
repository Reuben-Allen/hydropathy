# Compute Hydropathy Plot for a Protein
Plotting the hydropathy of a protein along its sequence can give basic insight into the structure of a protein. Hydropathy plots are especially useful for quickly predicting transmembrane domains. The calculation is simple, the hydropathy for
a particular residue number n is calculated by taking the mean of the
n-i to n+i residues, where i is supplied by the user. The hydropathy of each amino acid is given in the following dictionary:
```
amine_dict = {
    "G": -0.4,
    "A": 1.8,
    "V": 4.2,
    "L": 3.8,
    "I": 4.5,
    "F": 2.8,
    "Y": -1.3,
    "W": -0.9,
    "S": -0.8,
    "T": -0.7,
    "P": 1.6,
    "Q": -3.5,
    "C": 2.5,
    "M": 1.9,
    "N": -3.5,
    "D": -3.5,
    "E": -3.5,
    "K": -3.9,
    "R": -4.5,
    "H": -3.2
    }
```
To get started, simply run the code and follow the prompts.
## Example:
To see how hydropathy plots can be used to predict structure, the following example will generate the plot for the protein rhodopsin from *Homo sapiens* (gene OPN2). As expected, the plot produces seven major peaks, which correspond to the seven transmembrane helices of rhodopsin.
```
Enter the amino acid sequence as a continuous string of single letter abbreviations:
MNGTEGPNFYVPFSNATGVVRSPFEYPQYYLAEPWQFSMLAAYMFLLIVLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVLGGFTSTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLAGWSRYIPEGLQCSCGIDYYTLKPEVNNESFVIYMFVVHFTIPMIIIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSNFGPIFMTIPAFFAKSAAIYNPVIYIMMNKQFRNCMLTTICCGKNPLGDDEASATVSKTETSQVAPA
Enter the calculation window size (number of residues used per iteration will be two times this value plus one):
4
```
![hydro](https://user-images.githubusercontent.com/47088251/202992108-a6ec78fa-b6c0-47ab-adb8-b2313748e3d2.jpg)
