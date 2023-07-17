# Sonnet-Automation
Tools designed to extract Resonant Frequency &amp; Coupling Quality Factor for Microwave Kinetic Inductance Detector Simulations using a Sonnet .csv data file. 

The scripts in this repository allow the extraction of Resonant Frqeuency &amp; Qc from a .csv data file exported from the EM Simulation Software _Sonnet_.

Resonant Frequency (f0) is extracted by finding the minimum S21 value for a given frequency range.
Qc is extracted by calculating the Full-Width Half-Max of the S21 dip ($Qc = \frac{f0}{FWHM}$). Normally, 
