# Sonnet-Automation
Tools designed to extract Resonant Frequency &amp; Coupling Quality Factor for Microwave Kinetic Inductance Detector Simulations using a Sonnet .csv data file. 

The scripts in this repository allow the extraction of Resonant Frqeuency &amp; Qc from a .csv data file exported from the EM Simulation Software _Sonnet_.

Resonant Frequency (**f0**) is extracted by finding the minimum S21 value for a given frequency range.

**$Q_{C}$** is extracted by calculating the Full-Width Half-Max of the S21 dip. Normally, ($Q_{Total} = \frac{f0}{FWHM}$) & $\frac{1}{Q_{Total}}=\frac{1}{Q_{i}} + \frac{1}{Q_{C}}$
