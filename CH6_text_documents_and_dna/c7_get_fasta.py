import urllib.request as web

def get_FASTA(id):
    """Fetch the DNA sequence with the given id from NCBI and return it as
    a string.

    Args:
        id (str): The identifier of a DNA sequence in the NCBI database.

    Returns:
        (str): String representing the sequence for the given id.
    """
    prefix1 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    prefix2 = '?db=nuccore&id='
    suffix = '&rettype=fasta&retmode=text'
    url = prefix1 + prefix2 + id + suffix
    read_file = web.urlopen(url)
    header = read_file.readline()
    dna = ''
    for line in read_file:
        line = line[:-1]
        dna = dna + line.decode('utf-8')
    read_file.close()
    return dna

id = 'AEQU02000001'
print(get_FASTA(id))
