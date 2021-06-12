#!/usr/bin/python3
"""
Main code of the pipeline to get the residues conservation scores of a protein
from a protein name

  How to use
  ----------
First you need to have the python packages selenium, 

Then you can run the script with the following command :

    python Conservation.py "MexA MexB OprM"

  Author
  ------
    Hocine Meraouna

"""

import argparse
import Auto_Uniprot as au
import Blast_Align as ba
import Auto_Mafft as am
import Res_Conser_Score as rcs


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("protein_names", help="list of protein names", type=str)

    ARGS = PARSER.parse_args()

    PROT_NAMES = ARGS.protein_names

    browser = start()

    for p in PROT_NAMES.split():

        PID = au.uniprot_id(browser, p)

        ba.run_blastp(ba.get_fasta(PID)[0].seq, PID)

    browser.close()
