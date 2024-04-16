README file for the data for which results are presented in:

Weber LA, Tomiello S, Schöbi D, Wellstein KV, Müller D, Iglesias S, Stephan KE (2021).
Auditory mismatch responses are differentially sensitive to changes in muscarinic 
acetylcholine versus dopamine receptor function. _bioRxiv_, doi:10.1101/2021.03.18.435979
=========================================================================================


This README contains information on the data of study 1 and study 2 presented in the paper 
"Auditory mismatch responses are differentially sensitive to changes in muscarinic 
acetylcholine versus dopamine receptor status". 
The analysis code for reproducing the results reported in the manuscript based on the raw
data provided here can be found at: https://gitlab.ethz.ch/tnu/code/weberetal-muscarinic-mmn-erp-2021

# Contributors / Roles
|                               |                                             |
| ----------------------------- | ------------------------------------------- |
| Analysis:     		| Lilian Weber (PhD)                          |
| Supervising Prof.:            | Prof. Klaas Enno Stephan (MD Dr. med., PhD) |
| Abbreviation:                 | DPRST (study acronym)                       |
| Date:                         | May, 2021                                   |

The project was conducted at the Translational Neuromodeling Unit (TNU).

# Reference
Weber LA, Tomiello S, Schöbi D, Wellstein KV, Müller D, Iglesias S, Stephan KE (2021).
Auditory mismatch responses are differentially sensitive to changes in muscarinic 
acetylcholine versus dopamine receptor function. _bioRxiv_, doi:10.1101/2021.03.18.435979


# Data Information

- folder `exp` contains mat files that hold design information about the paradigm (the tone sequence) used in the analysis
  - the file `volMMN_TaskDescription.pdf` contains a description of the experimental paradigm
  - this includes explanations for the behavioral output files that were created for each participant
- folder `pharma` contains mat files with information on drug groups, drug plasma levels, and genetic data
- folders `TNU_DPRST_xxxx` contain EEG and behavioral data for each participant
- EEG study1 (antagonist study)
    - subject IDs: DPRST_0101-DPRST_0181
    - no data available from eight subjects (see manuscript for reasons)
- EEG study2 (enhancing drugs)
    - subject IDs: DPRST_0201-DPRST_0280
    - no data available from three subjects (see manuscript for reasons)

# Participant data is stored in the following subfolders:

- raw behavioral data:        `TNU_DPRST_.../behavior/`
- raw EEG data:               `TNU_DPRST_.../eegdata/`

# Information behavioural data:

The behavioral data structure `MMN` contains the following entries:
`subjectID`, `expTask`, `stimuli`, `times`, `triggers`, `keys`, `responses`.

The meaning of these entries is explained in the task description file `volMMN_TaskDescription.pdf`
which is also contained in this repository.

# Information EEG data:

EEG data were collected at a sampling rate of 500Hz using an EASYCAP system with 64 scalp
electrodes including one electrooculography (EOG) channel (10-20 layout; EASYCAP GmbH,
https://www.easycap.de/wordpress/). Data were recorded with nose-reference. 
For a subset of participants, ECG and pulse oximetry data were additionally acquired via a bipolar
amplifier (BrainAmp ExG; Brain Products GmbH, https://www.brainproducts.com/index.php).

# Acronyms:
- DPRSt - project acronym
- MMN:  - mismatch negativity
