from Bio.Seq import Seq
from Bio import motifs

seqs = [Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), 
        Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"),
        Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"), Seq("GCCAT"),
        Seq("CGCAT"), Seq("CGATT"), Seq("CCAAT"), Seq("CCTAT"), Seq("TCCAC")]

seq_to_search_in = "GAGCTCGACTAGCAGTCTCTTATGAGGCCATTCAGCGGCTATGCTAGGGGACCCATTTTTA"
