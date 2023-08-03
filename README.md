# Sonnet-Automation
Tools designed to extract Resonant Frequency &amp; Coupling Quality Factor for Microwave Kinetic Inductance Detector Simulations using a Sonnet .csv data file. 

The scripts in this repository allow the extraction of Resonant Frqeuency &amp; Qc from a .csv data file exported from the EM Simulation Software _Sonnet_.
The main purpose of these scripts is to automate the extraction of data from large Sonnet data sets and thus the scripts provided here will automate the extraction of Resonant Frequency and Qc for _any number of parameter sweeps_.

**Please Note:** These Scripts will only work with 1 single resonant dip to correctly extract f0 &amp; Qc.

Resonant Frequency (**f0**) is extracted by finding the minimum S21 value for a given frequency range.

**$Q_{C}$** is extracted by calculating the Full-Width Half-Max of the S21 dip. Normally, ($Q_{Total} = \frac{f0}{FWHM}$) & $\frac{1}{Q_{Total}}=\frac{1}{Q_{i}} + \frac{1}{Q_{C}}$, however $Q_{i} \rightarrow \infty$ in Sonnet and so $Q_{Total} \approx Q_{C}$.

## Outputting Data From Sonnet
**Please note:** Ensure the data exported from Sonnet is in the form of S-Paramter, Mag and Phase for accurate values.
For outputting simulation data from Sonnet to a .csv file, please refer to the Sonnet manual.

https://www.sonnetsoftware.com/support/manuals.asp

## How To Use The Automation Scripts

### Python Automation Script

For the Python Script, simply enter the file directory of the .csv data file to _line 44_ _(with open(file directory, "r") as csvfile)_. The script will output all Parameter names, Resonant Frequencies and Qc Factor for all Parameters into the Python console.

If you wish to plot data, each frequency range is stored in the _"b"_ variable and S-paramter data is stored in _S11_Mag, S11_Phase, S21_Mag &amp; S21_Phase variables_ respectively.

All Parameter names are stored in _title_
All f0 values are stored in _ac_res_freq_
All Qc values are stored in _Qual_Fac_


### MatLab Automation Script

For the Matlab Script, make sure the data file is on the correct path. Then use the function "ResExtract(filename)".
**For Example:** [ResonantFrequencies, QFactors]=ResExtract(filename).
