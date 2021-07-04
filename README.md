# ResConservScorePy
Pipeline writen in python to get a given protein's residues conservation JSD scores

---

## Description :
The pipeline is the following :
* First the user gives a protein name, and the code will look in [Uniprot](https://www.uniprot.org/) for an ID corresponding to this protein
* Then a [Blastp](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins) is run on the sequence of this protein ID using **UniProtKB/Swiss-Prot** database.
* A multiple sequence alignment is then proceeded using [MAFFT](https://mafft.cbrc.jp/alignment/server/).
* Finaly the residues conservation scores are calculated using the [JS Divergence](https://compbio.cs.princeton.edu/conservation/score.html) method.

## Requirements :

### System :
* Linux : 
The code has only been tested on Ubuntu.

### Browser :
The code has only been tested with firefox.

### Python packages :
In order to be able to run this code of course you need to have python3 but also some python packages :
* [`selenium`](https://selenium-python.readthedocs.io/)
* [`argparse`](https://docs.python.org/3/library/argparse.html)
* [`BioPython`](https://biopython.org/)
* [`pandas`](https://pandas.pydata.org/)

PyPi installation :
```shell
$pip install selenium
$pip install argparse
$pip install pandas
$pip install biopython
```

Conda installation :
```bash
$conda create -n resconsscore python
$source activate resconsscore
$conda install -c conda-forge selenium
$conda install -c conda-forge argparse
$conda install pandas
conda install -c conda-forge biopython
```
### Others :
selenium requires [geckodriver](https://github.com/mozilla/geckodriver/releases) for firefox, check this [link](https://selenium-python.readthedocs.io/installation.html#drivers) for the other browsers.

### Script files :

[`Conservation.py`](https://github.com/hocinebib/ResConsScorePipeline/blob/main/scr/Conservation.py)
[`Auto_Uniprot.py`](https://github.com/hocinebib/ResConsScorePipeline/blob/main/scr/Auto_Uniprot.py)
[`Blast_Align.py`](https://github.com/hocinebib/ResConsScorePipeline/blob/main/scr/Blast_Align.py)
[`Auto_Mafft.py`](https://github.com/hocinebib/ResConsScorePipeline/blob/main/scr/Auto_Mafft.py)
[`Res_Conserv_Score.py`](https://github.com/hocinebib/ResConsScorePipeline/blob/main/scr/Res_Conserv_Score.py)

## Usage :
1. First clone this repository :
```shell
$git clone https://github.com/hocinebib/ResConsScorePipeline.git
```
or [download](https://github.com/hocinebib/ResConsScorePipeline/archive/refs/heads/main.zip) it.

### Exemple of usage :

```shell
$cd ResConsScorePipeline/
$python src/Conservation.py "MexA MexB OprM"
```




