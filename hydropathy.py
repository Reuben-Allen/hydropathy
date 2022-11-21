"""
Reuben Allen
10/7/2021

This code produces a hydropathy plot for a polypeptide given the amino 
acid sequence, which is entered by the user as a string of single-letter
abbreviations from n-terminus to c-terminus. For instance, the sequence 
alanine-proline-tryptophan would be written as 'APW'. The hydropathy for
a particular residue number n is calculated by taking the mean of the
n-i to n+i residues, where i is supplied by the user. The hydropathy for 
the first and last i residues are not calculated.
"""

# import python libraries
from matplotlib import pyplot as plt
import statistics as stat
import numpy as np

def check_str(amine_dict):
    """This function fetches user inputs and checks them before proceeding."""
    print('Enter the amino acid sequence as a continuous string of single letter abbreviations:')
    sequence = input()
    sequence_check = 0
    for key in amine_dict:
        sequence_num = sequence.count(key) # will return the number of occurences of a particular amino acid in the sequence
        sequence_check += sequence_num
    if sequence_check != len(sequence): # 
        print("Invalid Characters Entered. Please Try Again!")
        check_str(amine_dict)
    else:
        while True:
            print('Enter the calculation window size (number of residues used per iteration will be two times this value plus one):')
            window_str= input()
            try:
                window = int(window_str)
                if window < 0:
                    print("Window size must be greater than zero. Please try again!")
                    continue
            except ValueError:
                print('Invalid Characters Entered. Please Try Again!')
                continue
            break
        return sequence, window

# Defining a dictionary containing hydropathy index values for all 20 common amino acids
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

if __name__ =='__main__':
    primary_structure, window = check_str(amine_dict) # Get user inputs
    hydropathy_raw = [amine_dict[key] for key in primary_structure] # generate list of hydropathy values for each amino acid
    hydropathy = [stat.mean(hydropathy_raw[n-window:n+window+1]) for n in range(window,len(primary_structure)-window-1)] # perform mean calculations

    #plotting
    x = np.arange(window,len(primary_structure)-window-1,1)
    y = np.array(hydropathy)
    fig, ax = plt.subplots()
    ax.plot(x,y,'k')
    ax.axhline(y=0,color ='k')
    ax.grid(color = 'k', linestyle = '--',axis='x')
    ax.fill_between(x,y,where=(y>0),color='coral',interpolate=True)
    ax.fill_between(x,y,where=(y<0),color='skyblue',interpolate=True)
    ax.set_title("Hydropathy Plot")
    ax.set_xlabel("Residue Number")
    ax.set_ylabel("Hydropathy Index")
    plt.show()